#!/usr/bin/env python3
"""
Interactive Age Extraction from JSON
Asks for user input and extracts age information
Date: October 18, 2025
"""

import json
import os

def load_json_file(filename):
    """Load JSON file and return data"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"✓ Successfully loaded: {filename}")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found!")
        return None
    except json.JSONDecodeError:
        print(f"✗ Error: Invalid JSON format in '{filename}'")
        return None
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return None

def extract_age_from_data(data, person_name=None):
    """Extract age information from JSON data"""
    print("\n" + "="*50)
    print("AGE EXTRACTION RESULTS")
    print("="*50)
    
    if person_name:
        print(f"Looking for age information for: {person_name}")
    
    # Check if data is a dictionary with direct age field
    if isinstance(data, dict):
        if 'age' in data:
            age_value = data['age']
            name = data.get('name', 'Unknown person')
            
            print(f"Found age information:")
            print(f"  Name: {name}")
            print(f"  Age: {age_value}")
            
            # Try to convert age to number for analysis
            try:
                age_num = int(age_value)
                print(f"  Age as number: {age_num}")
                
                # Age category analysis
                if age_num >= 65:
                    category = "Senior"
                elif age_num >= 18:
                    category = "Adult"
                else:
                    category = "Minor"
                
                print(f"  Age category: {category}")
                
                # Additional age analysis
                birth_year = 2025 - age_num
                print(f"  Approximate birth year: {birth_year}")
                
                return {
                    'name': name,
                    'age': age_value,
                    'age_numeric': age_num,
                    'category': category,
                    'birth_year': birth_year
                }
                
            except ValueError:
                print(f"  Note: Age '{age_value}' is not a valid number")
                return {
                    'name': name,
                    'age': age_value,
                    'age_numeric': None,
                    'category': 'Unknown',
                    'birth_year': None
                }
        else:
            print("✗ No 'age' field found in the JSON data")
            print("Available fields:", list(data.keys()))
            return None
    
    # Check if data is a list of people
    elif isinstance(data, list):
        print(f"Found list with {len(data)} items")
        ages_found = []
        
        for i, item in enumerate(data):
            if isinstance(item, dict) and 'age' in item:
                name = item.get('name', f'Person {i+1}')
                age = item['age']
                ages_found.append({'name': name, 'age': age})
        
        if ages_found:
            print(f"Found {len(ages_found)} people with age information:")
            for person in ages_found:
                print(f"  - {person['name']}: {person['age']}")
            return ages_found
        else:
            print("✗ No age information found in the list")
            return None
    
    else:
        print("✗ Unexpected data format - expected dictionary or list")
        return None

def interactive_age_extraction():
    """Interactive function to get user input and extract age"""
    print("INTERACTIVE AGE EXTRACTION TOOL")
    print("="*50)
    
    # Ask user for JSON file name
    print("\nStep 1: Select JSON file")
    print("Available options:")
    print("1. Use sample.json (default)")
    print("2. Enter custom filename")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        filename = input("Enter JSON filename: ").strip()
        if not filename:
            filename = "sample.json"
    else:
        filename = "sample.json"
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"\nFile '{filename}' not found.")
        create_choice = input("Create a sample file? (y/n): ").strip().lower()
        
        if create_choice == 'y':
            # Create sample data
            sample_data = {
                "name": "mk",
                "age": "89",
                "city": "hihus",
                "email": "mk@example.com"
            }
            
            with open(filename, 'w') as file:
                json.dump(sample_data, file, indent=2)
            
            print(f"✓ Created sample file: {filename}")
        else:
            print("Exiting...")
            return
    
    # Load the JSON file
    print(f"\nStep 2: Loading JSON file '{filename}'...")
    data = load_json_file(filename)
    
    if not data:
        return
    
    # Show the JSON content
    print(f"\nJSON content:")
    print(json.dumps(data, indent=2))
    
    # Ask user what they want to extract
    print(f"\nStep 3: Extract age information")
    extract_choice = input("Extract age for specific person? (y/n): ").strip().lower()
    
    person_name = None
    if extract_choice == 'y':
        person_name = input("Enter person's name: ").strip()
    
    # Extract age information
    result = extract_age_from_data(data, person_name)
    
    if result:
        # Ask if user wants to save the extracted information
        save_choice = input("\nSave extracted age information? (y/n): ").strip().lower()
        
        if save_choice == 'y':
            output_filename = input("Enter output filename (default: extracted_age.json): ").strip()
            if not output_filename:
                output_filename = "extracted_age.json"
            
            # Create output data
            output_data = {
                "extraction_date": "2025-10-18",
                "source_file": filename,
                "extracted_age_info": result,
                "user_request": {
                    "person_name": person_name,
                    "extraction_type": "age_information"
                }
            }
            
            try:
                with open(output_filename, 'w') as file:
                    json.dump(output_data, file, indent=2)
                print(f"✓ Age information saved to: {output_filename}")
            except Exception as e:
                print(f"✗ Error saving file: {e}")
    
    # Ask if user wants to continue
    continue_choice = input("\nExtract age from another file? (y/n): ").strip().lower()
    if continue_choice == 'y':
        interactive_age_extraction()

def quick_age_extraction():
    """Quick extraction without many prompts"""
    print("QUICK AGE EXTRACTION")
    print("="*30)
    
    # Ask for name to look up
    person_name = input("Enter person's name to find their age: ").strip()
    
    # Default to sample.json
    filename = "sample.json"
    
    # Load and extract
    data = load_json_file(filename)
    if data:
        result = extract_age_from_data(data, person_name)
        
        if result and isinstance(result, dict):
            print(f"\nQuick Result:")
            print(f"Name: {result.get('name', 'Unknown')}")
            print(f"Age: {result.get('age', 'Unknown')}")
            print(f"Category: {result.get('category', 'Unknown')}")

def main():
    """Main function with menu options"""
    print("AGE EXTRACTION TOOL")
    print("Date: October 18, 2025")
    print("="*50)
    
    while True:
        print("\nSelect an option:")
        print("1. Interactive age extraction (detailed)")
        print("2. Quick age extraction")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            interactive_age_extraction()
        elif choice == "2":
            quick_age_extraction()
        elif choice == "3":
            print("Thank you for using the Age Extraction Tool!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()