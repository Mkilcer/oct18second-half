#!/usr/bin/env python3
"""
Simple JSON Information Extraction Example
Demonstrates extracting specific information from the sample.json file
"""

import json

def extract_from_sample_json():
    """Extract specific information from sample.json"""
    
    print("JSON Information Extraction Example")
    print("="*40)
    
    try:
        # Load the JSON file
        with open('sample.json', 'r') as file:
            data = json.load(file)
        
        print("Original JSON data:")
        print(json.dumps(data, indent=2))
        print("\n" + "-"*40)
        
        # Extract specific fields
        print("EXTRACTING SPECIFIC INFORMATION:")
        print("-"*40)
        
        # Extract name
        if 'name' in data:
            name = data['name']
            print(f"Name: {name}")
        
        # Extract age
        if 'age' in data:
            age = data['age']
            print(f"Age: {age}")
        
        # Extract city
        if 'city' in data:
            city = data['city']
            print(f"City: {city}")
        
        print("\n" + "-"*40)
        
        # Create a filtered version with only specific fields
        specific_fields = ['name', 'city']  # Only extract name and city
        filtered_data = {}
        
        for field in specific_fields:
            if field in data:
                filtered_data[field] = data[field]
        
        print("FILTERED DATA (name and city only):")
        print(json.dumps(filtered_data, indent=2))
        
        # Save filtered data to a new file
        with open('filtered_info.json', 'w') as file:
            json.dump(filtered_data, file, indent=2)
        
        print("\nFiltered data saved to 'filtered_info.json'")
        
        # Demonstrate searching and validation
        print("\n" + "-"*40)
        print("DATA VALIDATION AND ANALYSIS:")
        print("-"*40)
        
        # Check if age is numeric
        if 'age' in data:
            try:
                age_numeric = int(data['age'])
                print(f"Age as number: {age_numeric}")
                if age_numeric >= 18:
                    print("Status: Adult")
                else:
                    print("Status: Minor")
            except ValueError:
                print("Age is not a valid number")
        
        # Check name length
        if 'name' in data:
            name_length = len(data['name'])
            print(f"Name length: {name_length} characters")
        
        # Create summary report
        summary = {
            "total_fields": len(data),
            "fields_present": list(data.keys()),
            "person_name": data.get('name', 'Unknown'),
            "location": data.get('city', 'Unknown'),
            "has_age_info": 'age' in data
        }
        
        print("\nSUMMARY REPORT:")
        print(json.dumps(summary, indent=2))
        
        # Save summary
        with open('summary_report.json', 'w') as file:
            json.dump(summary, file, indent=2)
        
        print("Summary report saved to 'summary_report.json'")
        
    except FileNotFoundError:
        print("Error: sample.json file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_from_sample_json()