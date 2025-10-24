#!/usr/bin/env python3
"""
Extract Specific Information from sample.json
Practical example using the actual JSON file in the workspace
"""

import json
import os

def load_sample_json():
    """Load the sample.json file"""
    try:
        with open('sample.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: sample.json not found!")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
        return None

def extract_specific_info():
    """Extract specific information from the JSON file"""
    
    print("EXTRACTING SPECIFIC INFORMATION FROM JSON FILE")
    print("="*50)
    
    # Load the JSON data
    data = load_sample_json()
    if not data:
        return
    
    print("Original JSON content:")
    print(json.dumps(data, indent=2))
    print("\n" + "-"*50)
    
    # Extract specific fields you want
    print("EXTRACTED INFORMATION:")
    print("-"*30)
    
    # Method 1: Direct key access
    try:
        name = data['name']
        print(f"Name: {name}")
    except KeyError:
        print("Name: Not found")
    
    # Method 2: Safe access with get()
    age = data.get('age', 'Unknown')
    city = data.get('city', 'Unknown')
    
    print(f"Age: {age}")
    print(f"City: {city}")
    
    # Extract only specific fields
    extracted_data = {
        'person_name': data.get('name'),
        'location': data.get('city'),
        'age_info': data.get('age')
    }
    
    print(f"\nExtracted Data Structure:")
    print(json.dumps(extracted_data, indent=2))
    
    # Save extracted information
    with open('extracted_info.json', 'w') as file:
        json.dump(extracted_data, file, indent=2)
    
    print("\n✓ Extracted information saved to 'extracted_info.json'")
    
    # Create different extraction scenarios
    print("\n" + "-"*50)
    print("DIFFERENT EXTRACTION SCENARIOS:")
    print("-"*50)
    
    # Scenario 1: Only name and city
    name_city = {k: data[k] for k in ['name', 'city'] if k in data}
    print("1. Name and City only:")
    print(json.dumps(name_city, indent=2))
    
    # Scenario 2: All fields as a list
    all_values = list(data.values())
    print(f"\n2. All values as list: {all_values}")
    
    # Scenario 3: Check if specific information exists
    has_email = 'email' in data
    has_phone = 'phone' in data
    print(f"\n3. Has email: {has_email}")
    print(f"   Has phone: {has_phone}")
    
    # Scenario 4: Data validation and transformation
    print(f"\n4. Data Analysis:")
    print(f"   Total fields: {len(data)}")
    print(f"   Field names: {list(data.keys())}")
    
    # Try to convert age to number
    try:
        age_number = int(data.get('age', 0))
        print(f"   Age as number: {age_number}")
        if age_number >= 65:
            print(f"   Age category: Senior")
        elif age_number >= 18:
            print(f"   Age category: Adult")
        else:
            print(f"   Age category: Minor")
    except (ValueError, TypeError):
        print(f"   Age: Cannot convert to number")
    
    # Scenario 5: Create summary report
    summary = {
        "extraction_date": "2025-10-18",
        "source_file": "sample.json",
        "extracted_fields": {
            "name": data.get('name'),
            "city": data.get('city')
        },
        "metadata": {
            "total_original_fields": len(data),
            "fields_extracted": 2,
            "success": True
        }
    }
    
    print(f"\n5. Summary Report:")
    print(json.dumps(summary, indent=2))
    
    # Save summary
    with open('extraction_summary.json', 'w') as file:
        json.dump(summary, file, indent=2)
    
    print("\n✓ Summary saved to 'extraction_summary.json'")

def create_extraction_template():
    """Create a template for extracting different types of information"""
    
    template = {
        "instructions": "Modify this template to extract the specific information you need",
        "extraction_rules": {
            "required_fields": ["name", "city"],
            "optional_fields": ["age", "email", "phone"],
            "transformations": {
                "name": "convert to uppercase",
                "age": "convert to integer",
                "city": "convert to title case"
            }
        },
        "output_format": {
            "extracted_data": {},
            "metadata": {
                "extraction_date": "",
                "source_file": "",
                "success": False
            }
        }
    }
    
    with open('extraction_template.json', 'w') as file:
        json.dump(template, file, indent=2)
    
    print("✓ Extraction template saved to 'extraction_template.json'")

def main():
    """Main execution function"""
    print("JSON Information Extraction Tool")
    print("Working with sample.json file")
    print("="*50)
    
    # Check if sample.json exists
    if not os.path.exists('sample.json'):
        print("Creating sample.json file for demonstration...")
        sample_data = {"name": "mk", "age": "89", "city": "hihus"}
        with open('sample.json', 'w') as file:
            json.dump(sample_data, file, indent=2)
        print("✓ Created sample.json")
    
    # Extract information
    extract_specific_info()
    
    # Create template
    print(f"\n{'-'*50}")
    print("CREATING EXTRACTION TEMPLATE:")
    print(f"{'-'*50}")
    create_extraction_template()
    
    print(f"\n{'='*50}")
    print("EXTRACTION COMPLETED!")
    print("Generated files:")
    print("- extracted_info.json")
    print("- extraction_summary.json") 
    print("- extraction_template.json")
    print("="*50)

if __name__ == "__main__":
    main()