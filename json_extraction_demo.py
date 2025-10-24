#!/usr/bin/env python3
"""
Comprehensive JSON Extraction Demo
Shows various ways to extract specific information from JSON files
"""

import json

# Sample JSON data for demonstration
sample_data = {
    "name": "mk",
    "age": "89", 
    "city": "hihus",
    "email": "mk@example.com",
    "hobbies": ["reading", "coding", "music"],
    "profile": {
        "isActive": True,
        "lastLogin": "2025-10-18",
        "preferences": {
            "theme": "dark",
            "language": "en"
        }
    },
    "projects": [
        {"name": "Project A", "status": "completed", "budget": 5000},
        {"name": "Project B", "status": "in-progress", "budget": 7500},
        {"name": "Project C", "status": "planned", "budget": 3000}
    ]
}

def demo_basic_extraction():
    """Demonstrate basic key extraction"""
    print("="*60)
    print("1. BASIC KEY EXTRACTION")
    print("="*60)
    
    # Extract individual fields
    name = sample_data.get("name", "Unknown")
    age = sample_data.get("age", "Unknown")
    city = sample_data.get("city", "Unknown")
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
    # Extract multiple fields at once
    basic_info = {key: sample_data[key] for key in ["name", "age", "city"] if key in sample_data}
    print(f"\nBasic Info: {json.dumps(basic_info, indent=2)}")

def demo_nested_extraction():
    """Demonstrate nested data extraction"""
    print("\n" + "="*60)
    print("2. NESTED DATA EXTRACTION")
    print("="*60)
    
    # Extract nested values
    theme = sample_data["profile"]["preferences"]["theme"]
    language = sample_data["profile"]["preferences"]["language"]
    is_active = sample_data["profile"]["isActive"]
    
    print(f"Theme: {theme}")
    print(f"Language: {language}")
    print(f"Is Active: {is_active}")
    
    # Extract entire nested object
    preferences = sample_data["profile"]["preferences"]
    print(f"\nAll Preferences: {json.dumps(preferences, indent=2)}")

def demo_list_extraction():
    """Demonstrate extracting data from lists"""
    print("\n" + "="*60)
    print("3. LIST DATA EXTRACTION")
    print("="*60)
    
    # Extract hobbies (simple list)
    hobbies = sample_data["hobbies"]
    print(f"Hobbies: {', '.join(hobbies)}")
    print(f"Number of hobbies: {len(hobbies)}")
    print(f"First hobby: {hobbies[0]}")
    
    # Extract from list of objects
    projects = sample_data["projects"]
    print(f"\nProjects:")
    for i, project in enumerate(projects):
        print(f"  {i+1}. {project['name']} - Status: {project['status']} - Budget: ${project['budget']}")
    
    # Extract specific project data
    completed_projects = [p for p in projects if p["status"] == "completed"]
    total_budget = sum(p["budget"] for p in projects)
    
    print(f"\nCompleted projects: {len(completed_projects)}")
    print(f"Total budget: ${total_budget}")

def demo_conditional_extraction():
    """Demonstrate conditional data extraction"""
    print("\n" + "="*60)
    print("4. CONDITIONAL EXTRACTION")
    print("="*60)
    
    # Extract data based on conditions
    age_num = int(sample_data["age"])
    age_category = "Senior" if age_num >= 65 else "Adult" if age_num >= 18 else "Minor"
    print(f"Age Category: {age_category}")
    
    # Extract projects based on budget
    expensive_projects = [p for p in sample_data["projects"] if p["budget"] > 5000]
    print(f"\nExpensive projects (>$5000):")
    for project in expensive_projects:
        print(f"  - {project['name']}: ${project['budget']}")
    
    # Extract based on multiple conditions
    active_with_preferences = sample_data["profile"]["isActive"] and sample_data["profile"]["preferences"]
    print(f"\nUser is active with preferences: {active_with_preferences}")

def demo_data_transformation():
    """Demonstrate transforming extracted data"""
    print("\n" + "="*60)
    print("5. DATA TRANSFORMATION")
    print("="*60)
    
    # Transform and format data
    user_summary = {
        "full_name": sample_data["name"].upper(),
        "age_in_years": int(sample_data["age"]),
        "location": sample_data["city"].title(),
        "contact": sample_data.get("email", "No email provided"),
        "hobby_count": len(sample_data["hobbies"]),
        "is_premium_user": int(sample_data["age"]) > 50,
        "total_project_value": sum(p["budget"] for p in sample_data["projects"])
    }
    
    print("Transformed User Summary:")
    print(json.dumps(user_summary, indent=2))

def demo_search_and_filter():
    """Demonstrate searching and filtering JSON data"""
    print("\n" + "="*60)
    print("6. SEARCH AND FILTER")
    print("="*60)
    
    # Search for keys containing specific text
    def find_keys_with_text(data, search_text):
        found = []
        def search_recursive(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    current_path = f"{path}.{key}" if path else key
                    if search_text.lower() in key.lower():
                        found.append(current_path)
                    if isinstance(value, (dict, list)):
                        search_recursive(value, current_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    if isinstance(item, (dict, list)):
                        search_recursive(item, f"{path}[{i}]")
        
        search_recursive(data)
        return found
    
    # Find all keys containing "name"
    name_keys = find_keys_with_text(sample_data, "name")
    print(f"Keys containing 'name': {name_keys}")
    
    # Find values containing specific text
    def find_values_with_text(data, search_text):
        found = []
        def search_recursive(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    current_path = f"{path}.{key}" if path else key
                    if isinstance(value, str) and search_text.lower() in value.lower():
                        found.append((current_path, value))
                    elif isinstance(value, (dict, list)):
                        search_recursive(value, current_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    current_path = f"{path}[{i}]"
                    if isinstance(item, str) and search_text.lower() in item.lower():
                        found.append((current_path, item))
                    elif isinstance(item, (dict, list)):
                        search_recursive(item, current_path)
        
        search_recursive(data)
        return found
    
    # Find all values containing "pro"
    pro_values = find_values_with_text(sample_data, "pro")
    print(f"Values containing 'pro': {pro_values}")

def demo_export_extracted_data():
    """Demonstrate exporting extracted data"""
    print("\n" + "="*60)
    print("7. EXPORT EXTRACTED DATA")
    print("="*60)
    
    # Create different export formats
    exports = {
        "basic_info": {
            "name": sample_data["name"],
            "age": sample_data["age"],
            "city": sample_data["city"]
        },
        "preferences_only": sample_data["profile"]["preferences"],
        "project_summary": [
            {
                "name": p["name"],
                "budget": p["budget"]
            } for p in sample_data["projects"]
        ],
        "metadata": {
            "total_keys": len(sample_data),
            "has_projects": "projects" in sample_data,
            "project_count": len(sample_data["projects"]),
            "extraction_date": "2025-10-18"
        }
    }
    
    # Save each export
    for export_name, export_data in exports.items():
        filename = f"extracted_{export_name}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            print(f"✓ Saved: {filename}")
        except Exception as e:
            print(f"✗ Error saving {filename}: {e}")

def main():
    """Run all demonstrations"""
    print("JSON INFORMATION EXTRACTION DEMONSTRATION")
    print("Date: October 18, 2025")
    print("\nOriginal JSON Data:")
    print(json.dumps(sample_data, indent=2))
    
    # Run all demos
    demo_basic_extraction()
    demo_nested_extraction()
    demo_list_extraction()
    demo_conditional_extraction()
    demo_data_transformation()
    demo_search_and_filter()
    demo_export_extracted_data()
    
    print("\n" + "="*60)
    print("DEMONSTRATION COMPLETED!")
    print("="*60)
    print("Check the 'extracted_*.json' files for exported data.")

if __name__ == "__main__":
    main()