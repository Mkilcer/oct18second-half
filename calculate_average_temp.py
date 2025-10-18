#!/usr/bin/env python3
"""
Script to calculate average temperature for each day of the week from a CSV file.
"""

import csv
from collections import defaultdict


def calculate_daily_average(csv_file):
    """
    Read temperature data from CSV file and calculate average temperature for each day.
    
    Args:
        csv_file: Path to the CSV file containing day and temperature data
        
    Returns:
        Dictionary with day names as keys and average temperatures as values
    """
    # Dictionary to store temperatures for each day
    day_temperatures = defaultdict(list)
    
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Skip empty rows
            if not row.get('Day') or not row.get('Temperature'):
                continue
            day = row['Day']
            temperature = float(row['Temperature'])
            day_temperatures[day].append(temperature)
    
    # Calculate averages
    daily_averages = {}
    for day, temps in day_temperatures.items():
        daily_averages[day] = sum(temps) / len(temps)
    
    return daily_averages


def main():
    """Main function to run the script."""
    csv_file = 'temperature_data.csv'
    
    try:
        averages = calculate_daily_average(csv_file)
        
        print("Average Temperature for Each Day of the Week:")
        print("-" * 50)
        
        # Define day order for better display
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for day in day_order:
            if day in averages:
                print(f"{day:12} : {averages[day]:.2f}°F")
        
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_file}'. Please ensure the file exists.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
