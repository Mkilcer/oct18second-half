#!/usr/bin/env python3
"""
Multi-Person Age Extractor
Demonstrates extracting age from JSON with multiple people
"""

import json

def create_sample_multi_person_data():
    """Create a sample JSON file with multiple people"""
    sample_data = {
        "people": [
            {"name": "mk", "age": "89", "city": "hihus", "email": "mk@example.com"},
            {"name": "John Smith", "age": "45", "city": "New York", "email": "john@example.com"},
            {"name": "Sarah Johnson", "age": "32", "city": "Los Angeles", "email": "sarah@example.com"},
            {"name": "Michael Brown", "age": "67", "city": "Chicago", "email": "michael@example.com"}
        ],
        "metadata": {
            "total_people": 4,
            "created_date": "2025-10-18"
        }
    }
    
    with open('multi_person_data.json', 'w') as file:
        json.dump(sample_data, file, indent=2)
    
    print("✓ Created multi_person_data.json with sample data")
    return sample_data

def get_user_input_for_search():
    """Get user input for searching"""
    print("MULTI-PERSON AGE EXTRACTOR")
    print("="*40)
    
    print("\nSearch options:")
    print("1. Search by exact name")
    print("2. Search by partial name")
    print("3. Show all people")
    print("4. Find people in age range")
    
    choice = input("Select option (1-4): ").strip()
    
    if choice == "1":
        name = input("Enter exact name: ").strip()
        return "exact", name
    elif choice == "2":
        name = input("Enter partial name: ").strip()
        return "partial", name
    elif choice == "3":
        return "all", None
    elif choice == "4":
        try:
            min_age = int(input("Enter minimum age: ").strip())
            max_age = int(input("Enter maximum age: ").strip())
            return "range", (min_age, max_age)
        except ValueError:
            print("Invalid age range. Using default search.")
            return "all", None
    else:
        print("Invalid choice. Showing all people.")
        return "all", None

def extract_age_by_exact_name(people_list, search_name):
    """Extract age by exact name match"""
    for person in people_list:
        if person.get('name', '').lower() == search_name.lower():
            return person
    return None

def extract_age_by_partial_name(people_list, search_name):
    """Extract age by partial name match"""
    matches = []
    for person in people_list:
        name = person.get('name', '').lower()
        if search_name.lower() in name:
            matches.append(person)
    return matches

def extract_age_by_range(people_list, age_range):
    """Extract people within age range"""
    min_age, max_age = age_range
    matches = []
    
    for person in people_list:
        try:
            age = int(person.get('age', 0))
            if min_age <= age <= max_age:
                matches.append(person)
        except ValueError:
            continue  # Skip invalid ages
    
    return matches

def display_person_info(person):
    """Display information for a single person"""
    name = person.get('name', 'Unknown')
    age = person.get('age', 'Unknown')
    city = person.get('city', 'Unknown')
    
    print(f"  Name: {name}")
    print(f"  Age: {age}")
    print(f"  City: {city}")
    
    # Age analysis
    try:
        age_num = int(age)
        if age_num >= 65:
            category = "Senior"
        elif age_num >= 18:
            category = "Adult"
        else:
            category = "Minor"
        print(f"  Category: {category}")
        
        birth_year = 2025 - age_num
        print(f"  Birth Year: ~{birth_year}")
    except ValueError:
        print(f"  Category: Unknown (invalid age)")

def main():
    """Main function"""
    
    # Step 1: Get user input
    search_type, search_value = get_user_input_for_search()
    
    # Step 2: Load or create JSON data
    try:
        with open('multi_person_data.json', 'r') as file:
            data = json.load(file)
        print(f"\n✓ Loaded data from multi_person_data.json")
    except FileNotFoundError:
        print(f"\n✗ multi_person_data.json not found. Creating sample data...")
        data = create_sample_multi_person_data()
    except json.JSONDecodeError:
        print(f"\n✗ Invalid JSON format!")
        return
    
    # Step 3: Extract people list
    if 'people' in data:
        people_list = data['people']
    else:
        # Handle single person format or list format
        if isinstance(data, list):
            people_list = data
        else:
            people_list = [data]  # Single person
    
    print(f"\nTotal people in database: {len(people_list)}")
    
    # Step 4: Process based on search type
    print(f"\n" + "="*50)
    print("AGE EXTRACTION RESULTS")
    print("="*50)
    
    if search_type == "exact":
        result = extract_age_by_exact_name(people_list, search_value)
        if result:
            print(f"Found exact match for '{search_value}':")
            display_person_info(result)
        else:
            print(f"✗ No exact match found for '{search_value}'")
            print("Available names:")
            for person in people_list:
                print(f"  - {person.get('name', 'Unknown')}")
    
    elif search_type == "partial":
        results = extract_age_by_partial_name(people_list, search_value)
        if results:
            print(f"Found {len(results)} partial match(es) for '{search_value}':")
            for i, person in enumerate(results, 1):
                print(f"\n{i}. Match:")
                display_person_info(person)
        else:
            print(f"✗ No partial matches found for '{search_value}'")
    
    elif search_type == "range":
        min_age, max_age = search_value
        results = extract_age_by_range(people_list, search_value)
        if results:
            print(f"Found {len(results)} people aged {min_age}-{max_age}:")
            for i, person in enumerate(results, 1):
                print(f"\n{i}. Person:")
                display_person_info(person)
        else:
            print(f"✗ No people found in age range {min_age}-{max_age}")
    
    elif search_type == "all":
        print(f"All people in database:")
        for i, person in enumerate(people_list, 1):
            print(f"\n{i}. Person:")
            display_person_info(person)
    
    # Step 5: Statistics
    print(f"\n" + "-"*50)
    print("DATABASE STATISTICS")
    print("-"*50)
    
    ages = []
    for person in people_list:
        try:
            age = int(person.get('age', 0))
            ages.append(age)
        except ValueError:
            continue
    
    if ages:
        print(f"Total people with valid ages: {len(ages)}")
        print(f"Average age: {sum(ages) / len(ages):.1f}")
        print(f"Youngest: {min(ages)}")
        print(f"Oldest: {max(ages)}")
        
        # Age categories
        seniors = sum(1 for age in ages if age >= 65)
        adults = sum(1 for age in ages if 18 <= age < 65)
        minors = sum(1 for age in ages if age < 18)
        
        print(f"Seniors (65+): {seniors}")
        print(f"Adults (18-64): {adults}")
        print(f"Minors (<18): {minors}")
    
    # Step 6: Ask if user wants to try again
    print(f"\n" + "-"*50)
    try_again = input("Search again? (y/n): ").strip().lower()
    if try_again == 'y':
        main()  # Restart
    else:
        print("Thank you for using the Multi-Person Age Extractor!")

if __name__ == "__main__":
    main()