#!/usr/bin/env python3
"""
Simple Age Extractor with User Input
Asks user for input and extracts age from JSON
"""

import json

def get_user_input():
    """Get user input for person's name"""
    print("AGE EXTRACTION TOOL")
    print("="*30)
    
    # Ask user for the person's name
    person_name = input("Enter the person's name to find their age: ").strip()
    
    if not person_name:
        print("No name provided. Using default search...")
        return None
    
    return person_name

def extract_age_by_name(data, search_name):
    """Extract age for a specific person by name"""
    
    if isinstance(data, dict):
        # Single person data
        stored_name = data.get('name', '').lower()
        if search_name.lower() in stored_name or stored_name in search_name.lower():
            return data.get('age')
    
    elif isinstance(data, list):
        # Multiple people data
        for person in data:
            if isinstance(person, dict):
                stored_name = person.get('name', '').lower()
                if search_name.lower() in stored_name or stored_name in search_name.lower():
                    return person.get('age')
    
    return None

def extract_any_age(data):
    """Extract any available age from the data"""
    
    if isinstance(data, dict) and 'age' in data:
        return data['age'], data.get('name', 'Unknown')
    
    elif isinstance(data, list):
        for person in data:
            if isinstance(person, dict) and 'age' in person:
                return person['age'], person.get('name', 'Unknown')
    
    return None, None

def main():
    """Main function"""
    
    # Step 1: Get user input
    search_name = get_user_input()
    
    # Step 2: Load JSON data
    try:
        with open('sample.json', 'r') as file:
            data = json.load(file)
        print(f"\n✓ Loaded data from sample.json")
    except FileNotFoundError:
        print("\n✗ sample.json not found!")
        return
    except json.JSONDecodeError:
        print("\n✗ Invalid JSON format!")
        return
    
    # Step 3: Display original data
    print(f"\nOriginal JSON data:")
    print(json.dumps(data, indent=2))
    
    # Step 4: Extract age based on user input
    print(f"\n" + "="*40)
    print("AGE EXTRACTION RESULTS")
    print("="*40)
    
    if search_name:
        # Search for specific person
        print(f"Searching for: {search_name}")
        age = extract_age_by_name(data, search_name)
        
        if age:
            print(f"✓ Found age for {search_name}: {age}")
            
            # Additional analysis
            try:
                age_num = int(age)
                print(f"Age as number: {age_num}")
                
                if age_num >= 65:
                    category = "Senior"
                elif age_num >= 18:
                    category = "Adult"
                else:
                    category = "Minor"
                
                print(f"Age category: {category}")
                birth_year = 2025 - age_num
                print(f"Approximate birth year: {birth_year}")
                
            except ValueError:
                print(f"Age '{age}' is not a valid number")
        else:
            print(f"✗ No age found for {search_name}")
            print("Extracting any available age...")
            
            # Fall back to any available age
            age, name = extract_any_age(data)
            if age:
                print(f"Found age for {name}: {age}")
            else:
                print("No age information found in the data")
    else:
        # Extract any available age
        print("Extracting any available age...")
        age, name = extract_any_age(data)
        
        if age:
            print(f"Found age for {name}: {age}")
            
            # Additional analysis
            try:
                age_num = int(age)
                print(f"Age as number: {age_num}")
                
                if age_num >= 65:
                    category = "Senior"
                elif age_num >= 18:
                    category = "Adult"
                else:
                    category = "Minor"
                
                print(f"Age category: {category}")
                
            except ValueError:
                print(f"Age '{age}' is not a valid number")
        else:
            print("No age information found in the data")
    
    # Step 5: Ask if user wants to try again
    print(f"\n" + "-"*40)
    try_again = input("Try with another name? (y/n): ").strip().lower()
    if try_again == 'y':
        main()  # Restart the process
    else:
        print("Thank you for using the Age Extractor!")

if __name__ == "__main__":
    main()