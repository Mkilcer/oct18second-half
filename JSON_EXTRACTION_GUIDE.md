# JSON Information Extraction Guide

This project demonstrates various methods to extract specific information from JSON files.

## Files

- `sample.json` - Sample JSON data file
- `extract_from_sample.py` - Practical extraction example using sample.json
- `json_extraction_demo.py` - Comprehensive demonstration of extraction techniques
- `json_extractor.py` - Interactive tool for exploring JSON data
- `simple_json_extract.py` - Simple example focused on basic extraction
- `run_json_extractor.ps1` - PowerShell script to run all tools

## JSON Extraction Methods

### 1. Basic Key Extraction

```python
import json

# Load JSON file
with open('sample.json', 'r') as file:
    data = json.load(file)

# Extract specific fields
name = data.get('name', 'Unknown')
age = data.get('age', 'Unknown')
city = data.get('city', 'Unknown')

print(f"Name: {name}, Age: {age}, City: {city}")
```

### 2. Multiple Field Extraction

```python
# Extract multiple fields at once
fields_to_extract = ['name', 'age', 'city']
extracted = {key: data[key] for key in fields_to_extract if key in data}
```

### 3. Nested Data Extraction

```python
# For nested JSON structures
theme = data['profile']['preferences']['theme']
# Or safely:
theme = data.get('profile', {}).get('preferences', {}).get('theme', 'default')
```

### 4. List/Array Extraction

```python
# Extract from arrays
hobbies = data.get('hobbies', [])
first_hobby = hobbies[0] if hobbies else 'None'

# Extract from array of objects
projects = data.get('projects', [])
project_names = [p['name'] for p in projects]
```

### 5. Conditional Extraction

```python
# Extract based on conditions
expensive_projects = [p for p in projects if p.get('budget', 0) > 5000]
active_users = [u for u in users if u.get('isActive', False)]
```

## How to Run

### Quick Start

1. **Run the practical example:**
   ```powershell
   py extract_from_sample.py
   ```

2. **Run the comprehensive demo:**
   ```powershell
   py json_extraction_demo.py
   ```

3. **Use the interactive tool:**
   ```powershell
   py json_extractor.py
   ```

### PowerShell Automation

Run all tools at once:
```powershell
.\run_json_extractor.ps1
```

## Common Use Cases

### Extract User Information
```python
user_info = {
    'name': data.get('name'),
    'email': data.get('email'),
    'location': data.get('city')
}
```

### Extract Configuration Settings
```python
settings = data.get('profile', {}).get('preferences', {})
theme = settings.get('theme', 'default')
language = settings.get('language', 'en')
```

### Extract Financial Data
```python
total_budget = sum(p.get('budget', 0) for p in data.get('projects', []))
completed_value = sum(p.get('budget', 0) for p in data.get('projects', []) 
                     if p.get('status') == 'completed')
```

### Filter and Transform Data
```python
# Transform while extracting
transformed_data = {
    'full_name': data.get('name', '').upper(),
    'age_category': 'Senior' if int(data.get('age', 0)) >= 65 else 'Adult',
    'location': data.get('city', '').title()
}
```

## Output Files

The scripts generate several output files:

- `extracted_info.json` - Basic extracted information
- `extraction_summary.json` - Summary report with metadata
- `extraction_template.json` - Template for custom extractions
- `filtered_info.json` - Filtered subset of data
- `extracted_*.json` - Various specialized extractions

## Sample JSON Structure

```json
{
    "name": "mk",
    "age": "89",
    "city": "hihus",
    "email": "mk@example.com",
    "hobbies": ["reading", "coding", "music"],
    "profile": {
        "isActive": true,
        "lastLogin": "2025-10-18",
        "preferences": {
            "theme": "dark",
            "language": "en"
        }
    },
    "projects": [
        {"name": "Project A", "status": "completed", "budget": 5000},
        {"name": "Project B", "status": "in-progress", "budget": 7500}
    ]
}
```

## Advanced Techniques

### 1. Safe Nested Access
```python
def safe_get(data, path, default=None):
    """Safely access nested dictionary values"""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

# Usage
theme = safe_get(data, 'profile.preferences.theme', 'default')
```

### 2. Search and Filter
```python
def find_keys_with_value(data, search_value):
    """Find all keys that contain a specific value"""
    found = []
    def search_recursive(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                current_path = f"{path}.{key}" if path else key
                if value == search_value:
                    found.append(current_path)
                elif isinstance(value, (dict, list)):
                    search_recursive(value, current_path)
    search_recursive(data)
    return found
```

### 3. Data Validation
```python
def validate_extracted_data(data, required_fields):
    """Validate that all required fields are present"""
    missing = [field for field in required_fields if field not in data]
    return len(missing) == 0, missing
```

## Error Handling

Always include proper error handling:

```python
try:
    with open('sample.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("JSON file not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!")
except Exception as e:
    print(f"Error: {e}")
```

## Tips for JSON Extraction

1. **Use `.get()` method** for safe access to prevent KeyError
2. **Validate data types** before processing
3. **Handle missing or null values** gracefully
4. **Use list comprehensions** for filtering arrays
5. **Create reusable functions** for complex extractions
6. **Always backup original data** before transforming
7. **Test with various JSON structures** to ensure robustness

## Troubleshooting

### Common Issues

1. **KeyError**: Use `.get()` instead of direct access
2. **TypeError**: Check data types before operations
3. **FileNotFoundError**: Verify file path and existence
4. **JSONDecodeError**: Validate JSON syntax

### Solutions

```python
# Instead of: name = data['name']  # May cause KeyError
# Use: name = data.get('name', 'Unknown')

# Instead of: age = int(data['age'])  # May cause ValueError
# Use: 
try:
    age = int(data.get('age', 0))
except ValueError:
    age = 0
```

This guide covers the most common scenarios for extracting specific information from JSON files. Use the provided scripts as starting points for your own JSON extraction needs.