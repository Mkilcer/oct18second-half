#!/usr/bin/env python3
"""
JSON Information Extractor
Extracts specific information from JSON files
Date: October 18, 2025
"""

import json
import os
from typing import Any, Dict, List, Union

def load_json_file(filename: str) -> Dict[str, Any]:
    """Load and parse a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"✓ Successfully loaded JSON file: {filename}")
            return data
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found!")
        return {}
    except json.JSONDecodeError as e:
        print(f"✗ Error: Invalid JSON format in '{filename}': {e}")
        return {}
    except Exception as e:
        print(f"✗ Error reading file '{filename}': {e}")
        return {}

def extract_specific_keys(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Extract specific keys from JSON data"""
    extracted = {}
    for key in keys:
        if key in data:
            extracted[key] = data[key]
            print(f"✓ Found key '{key}': {data[key]}")
        else:
            print(f"✗ Key '{key}' not found in JSON data")
    return extracted

def extract_nested_value(data: Dict[str, Any], path: str) -> Any:
    """Extract nested value using dot notation (e.g., 'user.profile.name')"""
    keys = path.split('.')
    current = data
    
    try:
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                print(f"✗ Path '{path}' not found in JSON data")
                return None
        print(f"✓ Found nested value at '{path}': {current}")
        return current
    except Exception as e:
        print(f"✗ Error extracting path '{path}': {e}")
        return None

def search_by_value(data: Dict[str, Any], search_value: Any) -> List[str]:
    """Find all keys that contain a specific value"""
    found_keys = []
    
    def recursive_search(obj: Any, parent_key: str = ""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{parent_key}.{key}" if parent_key else key
                if value == search_value:
                    found_keys.append(current_path)
                elif isinstance(value, (dict, list)):
                    recursive_search(value, current_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                current_path = f"{parent_key}[{i}]" if parent_key else f"[{i}]"
                if item == search_value:
                    found_keys.append(current_path)
                elif isinstance(item, (dict, list)):
                    recursive_search(item, current_path)
    
    recursive_search(data)
    return found_keys

def filter_by_criteria(data: List[Dict[str, Any]], field: str, value: Any) -> List[Dict[str, Any]]:
    """Filter a list of objects by a specific field value"""
    filtered = []
    for item in data:
        if isinstance(item, dict) and field in item and item[field] == value:
            filtered.append(item)
    return filtered

def display_json_structure(data: Any, indent: int = 0) -> None:
    """Display the structure of JSON data"""
    prefix = "  " * indent
    
    if isinstance(data, dict):
        print(f"{prefix}Dictionary with {len(data)} keys:")
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}  {key}: ", end="")
                display_json_structure(value, indent + 2)
            else:
                print(f"{prefix}  {key}: {type(value).__name__} = {value}")
    elif isinstance(data, list):
        print(f"List with {len(data)} items")
        if data:
            print(f"{prefix}  Sample item type: {type(data[0]).__name__}")
            if isinstance(data[0], (dict, list)):
                display_json_structure(data[0], indent + 1)
    else:
        print(f"{type(data).__name__} = {data}")

def save_extracted_data(data: Dict[str, Any], filename: str) -> None:
    """Save extracted data to a new JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"✓ Extracted data saved to: {filename}")
    except Exception as e:
        print(f"✗ Error saving to '{filename}': {e}")

def interactive_extraction(data: Dict[str, Any]) -> None:
    """Interactive mode for extracting data"""
    while True:
        print("\n" + "="*50)
        print("JSON EXTRACTION OPTIONS:")
        print("1. Extract specific keys")
        print("2. Extract nested value (dot notation)")
        print("3. Search by value")
        print("4. Display JSON structure")
        print("5. Save current data to file")
        print("6. Exit")
        print("="*50)
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            keys_input = input("Enter keys to extract (comma-separated): ").strip()
            keys = [key.strip() for key in keys_input.split(",") if key.strip()]
            if keys:
                extracted = extract_specific_keys(data, keys)
                if extracted:
                    print("\nExtracted data:")
                    print(json.dumps(extracted, indent=2))
        
        elif choice == "2":
            path = input("Enter nested path (e.g., user.profile.name): ").strip()
            if path:
                value = extract_nested_value(data, path)
                if value is not None:
                    print(f"Value: {value}")
        
        elif choice == "3":
            search_value = input("Enter value to search for: ").strip()
            # Try to convert to appropriate type
            try:
                if search_value.isdigit():
                    search_value = int(search_value)
                elif search_value.replace('.', '', 1).isdigit():
                    search_value = float(search_value)
                elif search_value.lower() in ['true', 'false']:
                    search_value = search_value.lower() == 'true'
            except:
                pass  # Keep as string
            
            found_keys = search_by_value(data, search_value)
            if found_keys:
                print(f"Found '{search_value}' at:")
                for key in found_keys:
                    print(f"  - {key}")
            else:
                print(f"Value '{search_value}' not found in JSON data")
        
        elif choice == "4":
            print("\nJSON Structure:")
            display_json_structure(data)
        
        elif choice == "5":
            filename = input("Enter filename to save (with .json extension): ").strip()
            if filename:
                save_extracted_data(data, filename)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

def main():
    """Main function"""
    print("JSON Information Extractor")
    print("="*50)
    
    # Default to sample.json in current directory
    filename = "sample.json"
    
    # Check if file exists
    if not os.path.exists(filename):
        filename = input("Enter JSON filename: ").strip()
        if not filename:
            print("No filename provided. Exiting...")
            return
    
    # Load JSON data
    json_data = load_json_file(filename)
    if not json_data:
        return
    
    print(f"\nLoaded JSON data from '{filename}':")
    print(json.dumps(json_data, indent=2))
    
    # Start interactive extraction
    interactive_extraction(json_data)

if __name__ == "__main__":
    main()