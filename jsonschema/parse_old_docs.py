#!/usr/bin/env python3
"""
Historical script to parse DCAT-US HTML documentation and add metadata to JSON schemas.

This script loads the DCAT-US HTML documentation (defaulting to the local
repository copy at DEPRECATED/docs/index.html),
extracts class and property metadata, and adds an '_oldDocs' object to the
corresponding JSON schema files.

It was primarily used for a one-time bootstrap import. The imported metadata was
manually corrected and refined afterward, so re-running this script is not a
reliable validation step for the current repository state.

The script uses algorithmic matching to find corresponding classes and properties:
- Classes are matched by normalizing names (removing spaces, case-insensitive)
- Properties are matched by: exact name, normalized name, or RDF URI local name

Usage:
    python parse_old_docs.py [--dry-run] [--verbose]

Options:
    --dry-run   Print what would be changed without modifying files
    --verbose   Print detailed information about extracted metadata
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass, field, asdict
from urllib.request import urlopen
from urllib.error import URLError

from bs4 import BeautifulSoup, Tag


# ============================================================================
# Data Classes for Structured Metadata
# ============================================================================

@dataclass
class PropertyMetadata:
    """Metadata for a single property extracted from documentation."""
    requirementLevel: str | None = None
    uri: str | None = None
    range: str | None = None
    definition: str | None = None
    usageNote: str | None = None
    alignment: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dict, excluding None values."""
        return {k: v for k, v in asdict(self).items() if v is not None}
    
    def get_uri_local_name(self) -> str | None:
        """Extract the local name from the RDF URI (e.g., 'skos:prefLabel' -> 'prefLabel')."""
        if not self.uri:
            return None
        # Handle prefixed URIs like "dcterms:title" or "skos:prefLabel"
        if ':' in self.uri:
            return self.uri.split(':')[-1]
        # Handle full URIs
        if '#' in self.uri:
            return self.uri.split('#')[-1]
        if '/' in self.uri:
            return self.uri.split('/')[-1]
        return self.uri


@dataclass
class ClassMetadata:
    """Metadata for a class extracted from documentation."""
    rdfClass: str | None = None
    definition: str | None = None
    usageNote: str | None = None
    rationale: str | None = None
    subclassOf: str | None = None
    alignment: str | None = None
    properties: dict[str, PropertyMetadata] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dict, excluding None values and empty properties."""
        result = {}
        for k, v in asdict(self).items():
            if k == 'properties':
                continue  # Properties are handled separately
            if v is not None:
                result[k] = v
        return result
    
    def get_rdf_local_name(self) -> str | None:
        """Extract the local name from the RDF class URI."""
        if not self.rdfClass:
            return None
        if ':' in self.rdfClass:
            return self.rdfClass.split(':')[-1]
        if '#' in self.rdfClass:
            return self.rdfClass.split('#')[-1]
        if '/' in self.rdfClass:
            return self.rdfClass.split('/')[-1]
        return self.rdfClass


# ============================================================================
# Name Normalization and Matching Functions
# ============================================================================

def normalize_name(name: str) -> str:
    """
    Normalize a name for comparison by:
    - Converting to lowercase
    - Removing spaces, hyphens, underscores
    - Removing parenthetical content like "(Contact Point)"
    """
    # Remove parenthetical content
    name = re.sub(r'\s*\([^)]*\)', '', name)
    # Remove spaces, hyphens, underscores and convert to lowercase
    return re.sub(r'[\s\-_]', '', name).lower()


def extract_local_name_from_uri(uri: str) -> str | None:
    """Extract the local name from an RDF URI."""
    if not uri:
        return None
    # Handle prefixed URIs like "dcterms:title" or "skos:prefLabel"
    if ':' in uri and not uri.startswith('http'):
        return uri.split(':')[-1]
    # Handle full URIs with fragment
    if '#' in uri:
        return uri.split('#')[-1]
    # Handle full URIs with path
    if '/' in uri:
        return uri.split('/')[-1]
    return uri


def find_matching_schema_file(class_name: str, schema_files: dict[str, Path], class_metadata: ClassMetadata) -> str | None:
    """
    Find the matching JSON schema file for a documentation class.
    
    Matching strategies (in order):
    1. Exact filename match (case-insensitive)
    2. Normalized name match (remove spaces, hyphens)
    3. RDF class local name match
    
    Returns the schema file key (name) if found, None otherwise.
    """
    normalized_class = normalize_name(class_name)
    rdf_local = class_metadata.get_rdf_local_name()
    
    for schema_name in schema_files.keys():
        normalized_schema = normalize_name(schema_name)
        
        # Strategy 1: Exact match (case-insensitive)
        if schema_name.lower() == class_name.lower():
            return schema_name
        
        # Strategy 2: Normalized name match
        if normalized_schema == normalized_class:
            return schema_name
        
        # Strategy 3: RDF local name match
        if rdf_local and normalized_schema == normalize_name(rdf_local):
            return schema_name
    
    return None


def find_matching_schema_property(
    doc_prop_name: str,
    prop_metadata: PropertyMetadata,
    schema_properties: dict[str, Any],
    verbose: bool = False
) -> str | None:
    """
    Find the matching JSON schema property for a documentation property.
    
    Matching strategies (in order):
    1. Exact name match
    2. Normalized name match (remove spaces, case-insensitive)
    3. Schema property title match
    4. RDF URI local name match (e.g., 'skos:prefLabel' -> 'prefLabel')
    5. CamelCase conversion
    """
    normalized_doc = normalize_name(doc_prop_name)
    uri_local = prop_metadata.get_uri_local_name()
    
    for schema_prop, schema_def in schema_properties.items():
        normalized_schema = normalize_name(schema_prop)
        
        # Strategy 1: Exact match
        if schema_prop == doc_prop_name:
            return schema_prop
        
        # Strategy 2: Normalized name match
        if normalized_schema == normalized_doc:
            return schema_prop
        
        # Strategy 3: Match against schema property's title field
        if isinstance(schema_def, dict) and 'title' in schema_def:
            schema_title = schema_def['title']
            if schema_title.lower() == doc_prop_name.lower():
                return schema_prop
            if normalize_name(schema_title) == normalized_doc:
                return schema_prop
        
        # Strategy 4: RDF URI local name match
        if uri_local and schema_prop.lower() == uri_local.lower():
            return schema_prop
        
        # Strategy 4b: Normalized RDF URI match
        if uri_local and normalized_schema == normalize_name(uri_local):
            return schema_prop
    
    # Strategy 5: Try camelCase conversion of doc property name
    # e.g., "access URL" -> "accessURL", "release date" -> "releaseDate"
    words = doc_prop_name.lower().split()
    if len(words) > 1:
        camel_case = words[0] + ''.join(w.capitalize() for w in words[1:])
        for schema_prop in schema_properties.keys():
            if schema_prop.lower() == camel_case.lower():
                return schema_prop
    
    # Strategy 6: Check if URI local name partially matches
    if uri_local:
        uri_normalized = normalize_name(uri_local)
        for schema_prop in schema_properties.keys():
            if normalize_name(schema_prop) == uri_normalized:
                return schema_prop
    
    return None


# ============================================================================
# HTML Parsing Functions
# ============================================================================

def load_html_source(source: str) -> str:
    """Load HTML content from a local file path or URL."""
    if source.startswith(('http://', 'https://')):
        print(f"Fetching HTML from {source}...")
        try:
            with urlopen(source, timeout=30) as response:
                return response.read().decode('utf-8')
        except URLError as e:
            print(f"Error fetching URL: {e}")
            sys.exit(1)

    source_path = Path(source).expanduser().resolve()
    print(f"Loading HTML from {source_path}...")
    try:
        return source_path.read_text(encoding='utf-8')
    except OSError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def normalize_text(text: str | None) -> str | None:
    """Normalize whitespace in text."""
    if text is None:
        return None
    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text.strip())
    return text if text else None


def parse_property_table(table: Tag) -> PropertyMetadata:
    """Parse a property definition table and extract metadata."""
    metadata = PropertyMetadata()
    
    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        if len(cells) >= 2:
            key = normalize_text(cells[0].get_text())
            value = normalize_text(cells[1].get_text())
            
            if not key or not value:
                continue
                
            key_lower = key.lower()
            
            if 'requirement level' in key_lower:
                metadata.requirementLevel = value
            elif key_lower == 'uri':
                metadata.uri = value
            elif key_lower == 'range':
                metadata.range = value
            elif 'definition' in key_lower:
                metadata.definition = value
            elif 'usage note' in key_lower or 'usage' == key_lower:
                if metadata.usageNote:
                    metadata.usageNote += " " + value
                else:
                    metadata.usageNote = value
    
    return metadata


def parse_class_note_table(table: Tag) -> dict[str, str]:
    """Parse a class NOTE table and extract class-level metadata."""
    data = {}
    
    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        if len(cells) >= 2:
            key = normalize_text(cells[0].get_text())
            value = normalize_text(cells[1].get_text())
            
            if not key or not value:
                continue
                
            key_lower = key.lower()
            
            if 'rdf class' in key_lower:
                data['rdfClass'] = value
            elif 'definition' in key_lower:
                data['definition'] = value
            elif 'usage note' in key_lower or 'usage' == key_lower:
                if 'usageNote' in data:
                    data['usageNote'] += " " + value
                else:
                    data['usageNote'] = value
            elif 'rationale' in key_lower:
                data['rationale'] = value
            elif 'sub-class of' in key_lower or 'subclass of' in key_lower:
                data['subclassOf'] = value
    
    return data


def extract_alignment_from_header(section: Tag) -> str | None:
    """Extract alignment status (New!, Aligned, No Change) from section header or nearby text."""
    # Look for NOTE sections that indicate alignment
    note_divs = section.find_all('div', class_='note')
    for note in note_divs:
        text = note.get_text()
        if 'New in DCAT-US' in text or 'New!' in text:
            return "New"
        elif 'Aligned with DCAT' in text:
            return "Aligned"
        elif 'No Change' in text:
            return "No Change"
    
    # Also check direct text
    header = section.find(['h3', 'h4', 'h5'])
    if header:
        text = header.get_text()
        if 'New!' in text:
            return "New"
    
    return None


def slug_to_class_name(slug: str) -> str:
    """Convert a section ID slug to a class display name.
    
    Examples:
        'access_restriction' -> 'Access Restriction'
        'data-service' -> 'Data Service'
        'catalog-record' -> 'Catalog Record'
        'address-contact_point' -> 'Address'  (strip variant suffixes)
        'address-location' -> 'Address'
    """
    # Handle variant suffixes like "address-contact_point", "address-location"
    # by taking only the first part if there's a variant indicator
    variant_patterns = ['-contact_point', '-location', '_point']
    for pattern in variant_patterns:
        if pattern in slug:
            slug = slug.split(pattern)[0]
    
    # Convert underscores and hyphens to spaces, then title case
    name = slug.replace('_', ' ').replace('-', ' ')
    # Title case each word
    name = ' '.join(word.capitalize() for word in name.split())
    return name


def parse_documentation(html: str) -> dict[str, ClassMetadata]:
    """Parse the HTML documentation and extract all class metadata."""
    soup = BeautifulSoup(html, 'html.parser')
    classes: dict[str, ClassMetadata] = {}
    
    # Find all class sections - they have IDs like "properties-for-{class}"
    class_sections = soup.find_all('section', id=re.compile(r'^properties-for-'))
    
    for section in class_sections:
        section_id = section.get('id', '')
        
        # Extract class slug from ID like "properties-for-dataset"
        match = re.match(r'^properties-for-(.+)$', section_id)
        if not match:
            continue
            
        class_slug = match.group(1)
        
        # Derive class name from the slug (not from h3 which may be "Mandatory Properties")
        class_name = slug_to_class_name(class_slug)
        
        if not class_name:
            continue
        
        # Use normalized name as key to avoid duplicates like "Address (Contact Point)" and "Address (Location)"
        normalized_key = normalize_name(class_name)
        
        # Skip if we already have this class (use existing or create new)
        if normalized_key in [normalize_name(k) for k in classes.keys()]:
            # Find the existing key and merge properties
            existing_key = next(k for k in classes.keys() if normalize_name(k) == normalized_key)
            class_metadata = classes[existing_key]
        else:
            class_metadata = ClassMetadata()
        
        # Extract alignment from nearby notes
        alignment = extract_alignment_from_header(section)
        if alignment:
            class_metadata.alignment = alignment
        
        # Look for the NOTE table with class definition (contains "RDF Class:" row)
        for table in section.find_all('table'):
            table_text = table.get_text()
            if 'RDF Class:' in table_text or 'RDF Class' in table_text:
                class_data = parse_class_note_table(table)
                if class_data.get('rdfClass'):
                    class_metadata.rdfClass = class_data.get('rdfClass')
                if class_data.get('definition'):
                    class_metadata.definition = class_data.get('definition')
                if class_data.get('usageNote'):
                    class_metadata.usageNote = class_data.get('usageNote')
                if class_data.get('rationale'):
                    class_metadata.rationale = class_data.get('rationale')
                if class_data.get('subclassOf'):
                    class_metadata.subclassOf = class_data.get('subclassOf')
                break
        
        # Find all property subsections within this class section
        # They have IDs like "{class-slug}-{property-name}" e.g., "catalog-title"
        # Some use underscores instead of hyphens, e.g., "quality_measurement_value"
        # Some use shortened slug prefixes, e.g., "period_start-date" for "period-of-time"
        class_slug_patterns = [
            class_slug,
            class_slug.replace('_', '-'),
            class_slug.replace('-', '_'),
        ]
        # Also try the first segment of the slug (e.g., "period" from "period-of-time")
        first_segment = class_slug.split('-')[0].split('_')[0]
        if first_segment != class_slug:
            class_slug_patterns.append(first_segment)
        
        for prop_section in section.find_all('section', id=True):
            prop_id = prop_section.get('id', '')
            
            # Skip non-property sections (like "catalog-mandatory-props")
            if any(x in prop_id for x in ['-mandatory-props', '-recommended-props', 
                                           '-optional-props', '-example', '-examples']):
                continue
            
            # Check if this is a property section for this class
            prop_slug = None
            for slug in class_slug_patterns:
                # Try both hyphen and underscore as separators
                for sep in ['-', '_']:
                    pattern = f'^{re.escape(slug)}{sep}(.+)$'
                    prop_match = re.match(pattern, prop_id)
                    if prop_match:
                        prop_slug = prop_match.group(1)
                        break
                if prop_slug:
                    break
            
            if not prop_slug:
                continue
            
            # Get the display name from the header if available
            prop_header = prop_section.find(['h4', 'h5'])
            if prop_header:
                prop_text = prop_header.get_text().strip()
                prop_text = re.sub(r'\s*Permalink.*$', '', prop_text)
                # Remove "Property:" prefix if present
                prop_name = re.sub(r'^Property:\s*', '', prop_text).strip()
            else:
                # Convert slug to display name (e.g., "access-url" -> "access url")
                prop_name = prop_slug.replace('-', ' ').replace('_', ' ')
            
            # Find the property definition table
            prop_table = prop_section.find('table')
            
            if prop_table:
                prop_metadata = parse_property_table(prop_table)
                
                # Check for NOTE alignment in property section
                note_div = prop_section.find('div', class_='note')
                if note_div:
                    note_text = note_div.get_text()
                    if 'New in DCAT-US' in note_text:
                        prop_metadata.alignment = "New"
                    elif 'Aligned with DCAT' in note_text:
                        prop_metadata.alignment = "Aligned"
                    elif 'No Change' in note_text:
                        prop_metadata.alignment = "No Change"
                
                # Use the section ID slug as key (e.g., "prefLabel", "altLabel")
                # This matches schema property names and avoids collisions
                # when multiple properties have the same display name
                class_metadata.properties[prop_slug] = prop_metadata
        
        # Store using the display name
        if normalized_key not in [normalize_name(k) for k in classes.keys()]:
            classes[class_name] = class_metadata
    
    return classes


# ============================================================================
# JSON Schema Update Functions
# ============================================================================

def collect_schema_files(schema_dir: Path) -> dict[str, Path]:
    """Collect all JSON schema files and return mapping of name -> path."""
    schema_files: dict[str, Path] = {}
    
    # All schemas are in definitions directory
    definitions_dir = schema_dir / "definitions"
    if definitions_dir.exists():
        for json_file in definitions_dir.glob("*.json"):
            name = json_file.stem  # Get filename without extension
            schema_files[name] = json_file
    
    return schema_files


def update_schema_with_metadata(
    schema_path: Path,
    class_metadata: ClassMetadata,
    dry_run: bool = False,
    verbose: bool = False
) -> bool:
    """Update a JSON schema file with extracted metadata."""
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"  Error reading {schema_path}: {e}")
        return False
    
    modified = False
    
    # Add class-level _oldDocs
    class_docs = class_metadata.to_dict()
    if class_docs:
        schema['_oldDocs'] = class_docs
        modified = True
        if verbose:
            print(f"  Added class-level _oldDocs: {list(class_docs.keys())}")
    
    # Add property-level _oldDocs using algorithmic matching
    if 'properties' in schema and class_metadata.properties:
        schema_properties = schema['properties']
        matched_props = set()
        unmatched_props = []
        
        for doc_prop_name, prop_metadata in class_metadata.properties.items():
            # Use algorithmic matching to find the schema property
            schema_prop = find_matching_schema_property(doc_prop_name, prop_metadata, schema_properties)
            
            if schema_prop:
                prop_docs = prop_metadata.to_dict()
                if prop_docs:
                    schema['properties'][schema_prop]['_oldDocs'] = prop_docs
                    modified = True
                    matched_props.add(schema_prop)
                    if verbose:
                        if schema_prop.lower() != doc_prop_name.lower():
                            print(f"  Added property _oldDocs for '{schema_prop}' (matched from '{doc_prop_name}')")
                        else:
                            print(f"  Added property _oldDocs for '{schema_prop}'")
            else:
                unmatched_props.append(doc_prop_name)
        
        if verbose and unmatched_props:
            print(f"  Unmatched properties from docs: {unmatched_props}")
    
    if modified and not dry_run:
        try:
            with open(schema_path, 'w', encoding='utf-8') as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
                f.write('\n')  # Add trailing newline
            print(f"  Updated {schema_path}")
        except IOError as e:
            print(f"  Error writing {schema_path}: {e}")
            return False
    elif modified and dry_run:
        print(f"  Would update {schema_path}")
    
    return modified


# ============================================================================
# Main Function
# ============================================================================

def main():
    default_source = (Path(__file__).parent.parent / "DEPRECATED" / "docs" / "index.html").resolve()

    parser = argparse.ArgumentParser(
        description='Parse DCAT-US HTML documentation and add metadata to JSON schemas.'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print what would be changed without modifying files'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed information about extracted metadata'
    )
    parser.add_argument(
        '--source',
        default=str(default_source),
        help='Path or URL of the HTML documentation to parse (default: local DEPRECATED/docs/index.html)'
    )
    parser.add_argument(
        '--schema-dir',
        type=Path,
        default=Path(__file__).parent,
        help='Directory containing JSON schema files'
    )
    
    args = parser.parse_args()
    
    # Load and parse HTML
    html = load_html_source(args.source)
    print(f"Fetched {len(html)} bytes of HTML")
    
    # Collect schema files first
    print("\nCollecting JSON schema files...")
    schema_files = collect_schema_files(args.schema_dir)
    print(f"Found {len(schema_files)} schema files: {list(schema_files.keys())}")
    
    # Parse documentation
    print("\nParsing documentation...")
    classes = parse_documentation(html)
    print(f"Found {len(classes)} classes in documentation")
    
    if args.verbose:
        for class_name, metadata in classes.items():
            print(f"\n  {class_name}:")
            print(f"    RDF Class: {metadata.rdfClass}")
            print(f"    Definition: {metadata.definition[:80] if metadata.definition else None}...")
            print(f"    Properties: {len(metadata.properties)}")
            for prop_name, prop_meta in metadata.properties.items():
                print(f"      - {prop_name}: {prop_meta.requirementLevel}")
    
    # Update schemas using algorithmic matching
    print("\nMatching and updating JSON schemas...")
    updated_count = 0
    skipped_count = 0
    
    for class_name, metadata in classes.items():
        # Use algorithmic matching to find schema file
        schema_file_name = find_matching_schema_file(class_name, schema_files, metadata)
        
        if schema_file_name is None:
            if args.verbose:
                print(f"  Skipping '{class_name}' - no matching schema file found")
            skipped_count += 1
            continue
        
        schema_path = schema_files[schema_file_name]
        print(f"\nProcessing '{class_name}' -> {schema_path.name}")
        
        if update_schema_with_metadata(schema_path, metadata, args.dry_run, args.verbose):
            updated_count += 1
    
    # Summary
    print(f"\n{'=' * 50}")
    print(f"Summary:")
    print(f"  Classes found in documentation: {len(classes)}")
    print(f"  Schema files available: {len(schema_files)}")
    print(f"  Schemas updated: {updated_count}")
    print(f"  Classes skipped (no matching schema): {skipped_count}")
    
    if args.dry_run:
        print("\n[DRY RUN] No files were modified.")


if __name__ == '__main__':
    main()
