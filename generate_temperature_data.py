#!/usr/bin/env python3
"""
Temperature Data Generator
Creates a CSV file with 2 weeks of daily temperature readings
Date: October 18, 2025
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_temperature_data():
    """Generate 2 weeks of realistic daily temperature readings"""
    
    # Starting date (2 weeks ago from today)
    start_date = datetime(2025, 10, 5)  # October 5, 2025
    
    # Generate dates for 14 days
    dates = []
    temperatures_high = []
    temperatures_low = []
    conditions = []
    humidity = []
    
    # Weather conditions options
    weather_conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Overcast"]
    
    for i in range(14):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date.strftime("%Y-%m-%d"))
        
        # Generate realistic temperature ranges (Fahrenheit)
        # Simulate fall weather with some variation
        base_high = random.randint(65, 78)  # High temperature
        base_low = base_high - random.randint(15, 25)  # Low temperature
        
        # Add some weather pattern variation
        if i in [3, 7, 10]:  # Some cooler/rainy days
            base_high -= random.randint(8, 15)
            base_low -= random.randint(8, 15)
            condition = random.choice(["Rainy", "Cloudy", "Overcast"])
            humidity_val = random.randint(75, 95)
        else:
            condition = random.choice(["Sunny", "Partly Cloudy", "Cloudy"])
            humidity_val = random.randint(45, 70)
        
        temperatures_high.append(base_high)
        temperatures_low.append(base_low)
        conditions.append(condition)
        humidity.append(humidity_val)
    
    # Create DataFrame
    data = {
        'Date': dates,
        'High_Temp_F': temperatures_high,
        'Low_Temp_F': temperatures_low,
        'Condition': conditions,
        'Humidity_%': humidity
    }
    
    df = pd.DataFrame(data)
    
    # Add calculated columns
    df['Avg_Temp_F'] = (df['High_Temp_F'] + df['Low_Temp_F']) / 2
    df['Temp_Range_F'] = df['High_Temp_F'] - df['Low_Temp_F']
    
    # Convert some temperatures to Celsius for comparison
    df['High_Temp_C'] = ((df['High_Temp_F'] - 32) * 5/9).round(1)
    df['Low_Temp_C'] = ((df['Low_Temp_F'] - 32) * 5/9).round(1)
    df['Avg_Temp_C'] = ((df['Avg_Temp_F'] - 32) * 5/9).round(1)
    
    return df

def main():
    """Generate and save temperature data"""
    print("Temperature Data Generator")
    print("="*40)
    
    # Generate the data
    print("Generating 2 weeks of temperature data...")
    df = generate_temperature_data()
    
    # Display the data
    print("\nGenerated Temperature Data:")
    print("="*40)
    print(df.to_string(index=False))
    
    # Save to CSV
    csv_filename = "temperature_data.csv"
    df.to_csv(csv_filename, index=False)
    print(f"\n✓ Data saved to: {csv_filename}")
    
    # Display summary statistics
    print("\nTemperature Summary Statistics:")
    print("="*40)
    print(f"Date Range: {df['Date'].iloc[0]} to {df['Date'].iloc[-1]}")
    print(f"Highest Temperature: {df['High_Temp_F'].max()}°F ({df['High_Temp_C'].max()}°C)")
    print(f"Lowest Temperature: {df['Low_Temp_F'].min()}°F ({df['Low_Temp_C'].min()}°C)")
    print(f"Average High: {df['High_Temp_F'].mean():.1f}°F")
    print(f"Average Low: {df['Low_Temp_F'].mean():.1f}°F")
    print(f"Average Humidity: {df['Humidity_%'].mean():.1f}%")
    
    # Weather condition summary
    print(f"\nWeather Conditions:")
    condition_counts = df['Condition'].value_counts()
    for condition, count in condition_counts.items():
        print(f"  {condition}: {count} days")
    
    # Create a simple analysis
    print(f"\nTemperature Analysis:")
    hot_days = len(df[df['High_Temp_F'] >= 75])
    cool_days = len(df[df['High_Temp_F'] < 65])
    print(f"  Hot days (≥75°F): {hot_days}")
    print(f"  Cool days (<65°F): {cool_days}")
    print(f"  Moderate days: {14 - hot_days - cool_days}")
    
    return df

if __name__ == "__main__":
    # Generate the data
    temperature_df = main()
    
    # Show first few rows in a nice format
    print(f"\nFirst 5 rows of data:")
    print("-" * 40)
    print(temperature_df.head().to_string(index=False))