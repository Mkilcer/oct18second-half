#!/usr/bin/env python3
"""
Temperature Data Analysis
Demonstrates working with the generated temperature CSV data
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_and_analyze_temperature_data():
    """Load and analyze the temperature data CSV"""
    
    print("Temperature Data Analysis")
    print("="*40)
    
    # Load the CSV file
    try:
        df = pd.read_csv('temperature_data.csv')
        print("✓ Successfully loaded temperature_data.csv")
    except FileNotFoundError:
        print("✗ temperature_data.csv not found. Please run generate_temperature_data.py first.")
        return
    
    # Display basic information
    print(f"\nDataset Info:")
    print(f"- Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"- Date range: {df['Date'].iloc[0]} to {df['Date'].iloc[-1]}")
    print(f"- Columns: {', '.join(df.columns)}")
    
    # Display first few rows
    print(f"\nFirst 5 rows:")
    print(df.head())
    
    # Basic statistics
    print(f"\nTemperature Statistics (Fahrenheit):")
    print(f"High Temperature - Mean: {df['High_Temp_F'].mean():.1f}°F, "
          f"Min: {df['High_Temp_F'].min()}°F, Max: {df['High_Temp_F'].max()}°F")
    print(f"Low Temperature - Mean: {df['Low_Temp_F'].mean():.1f}°F, "
          f"Min: {df['Low_Temp_F'].min()}°F, Max: {df['Low_Temp_F'].max()}°F")
    print(f"Average Temperature: {df['Avg_Temp_F'].mean():.1f}°F")
    print(f"Average Humidity: {df['Humidity_%'].mean():.1f}%")
    
    # Weather condition analysis
    print(f"\nWeather Conditions Analysis:")
    condition_summary = df['Condition'].value_counts()
    for condition, count in condition_summary.items():
        percentage = (count / len(df)) * 100
        print(f"- {condition}: {count} days ({percentage:.1f}%)")
    
    # Temperature trends
    print(f"\nTemperature Trends:")
    hottest_day = df.loc[df['High_Temp_F'].idxmax()]
    coldest_day = df.loc[df['Low_Temp_F'].idxmin()]
    print(f"Hottest day: {hottest_day['Date']} - {hottest_day['High_Temp_F']}°F ({hottest_day['Condition']})")
    print(f"Coldest day: {coldest_day['Date']} - {coldest_day['Low_Temp_F']}°F ({coldest_day['Condition']})")
    
    # Find patterns
    rainy_days = df[df['Condition'] == 'Rainy']
    high_humidity_days = df[df['Humidity_%'] > 80]
    
    print(f"\nPattern Analysis:")
    print(f"- Days with high humidity (>80%): {len(high_humidity_days)}")
    if len(high_humidity_days) > 0:
        print(f"  Average temperature on high humidity days: {high_humidity_days['Avg_Temp_F'].mean():.1f}°F")
    
    # Temperature ranges
    large_range_days = df[df['Temp_Range_F'] > 20]
    print(f"- Days with large temperature range (>20°F): {len(large_range_days)}")
    
    return df

def create_temperature_visualizations(df):
    """Create visualizations of the temperature data"""
    
    print(f"\nCreating temperature visualizations...")
    
    # Convert Date column to datetime for better plotting
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Create a figure with multiple subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Temperature Data Analysis - 2 Weeks', fontsize=16)
    
    # Plot 1: High and Low temperatures over time
    ax1.plot(df['Date'], df['High_Temp_F'], 'r-o', label='High Temp', linewidth=2)
    ax1.plot(df['Date'], df['Low_Temp_F'], 'b-o', label='Low Temp', linewidth=2)
    ax1.fill_between(df['Date'], df['Low_Temp_F'], df['High_Temp_F'], alpha=0.3, color='gray')
    ax1.set_title('Daily High and Low Temperatures')
    ax1.set_ylabel('Temperature (°F)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    # Plot 2: Humidity over time
    ax2.bar(df['Date'], df['Humidity_%'], color='lightblue', edgecolor='navy')
    ax2.set_title('Daily Humidity Levels')
    ax2.set_ylabel('Humidity (%)')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(axis='x', rotation=45)
    
    # Plot 3: Weather condition distribution
    condition_counts = df['Condition'].value_counts()
    ax3.pie(condition_counts.values, labels=condition_counts.index, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Weather Condition Distribution')
    
    # Plot 4: Temperature range analysis
    ax4.bar(df['Date'], df['Temp_Range_F'], color='orange', alpha=0.7)
    ax4.set_title('Daily Temperature Range')
    ax4.set_ylabel('Temperature Range (°F)')
    ax4.grid(True, alpha=0.3)
    ax4.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('temperature_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Temperature visualization saved as 'temperature_analysis.png'")
    plt.show()

def export_analysis_results(df):
    """Export analysis results to files"""
    
    print(f"\nExporting analysis results...")
    
    # Create summary statistics
    summary_stats = {
        'Metric': [
            'Average High Temperature (°F)',
            'Average Low Temperature (°F)', 
            'Highest Temperature (°F)',
            'Lowest Temperature (°F)',
            'Average Humidity (%)',
            'Days with High Humidity (>80%)',
            'Most Common Weather Condition',
            'Temperature Range Average (°F)'
        ],
        'Value': [
            f"{df['High_Temp_F'].mean():.1f}",
            f"{df['Low_Temp_F'].mean():.1f}",
            f"{df['High_Temp_F'].max()}",
            f"{df['Low_Temp_F'].min()}",
            f"{df['Humidity_%'].mean():.1f}",
            f"{len(df[df['Humidity_%'] > 80])}",
            f"{df['Condition'].mode().iloc[0]}",
            f"{df['Temp_Range_F'].mean():.1f}"
        ]
    }
    
    summary_df = pd.DataFrame(summary_stats)
    summary_df.to_csv('temperature_summary.csv', index=False)
    print("✓ Summary statistics saved to 'temperature_summary.csv'")
    
    # Export filtered data (hot days)
    hot_days = df[df['High_Temp_F'] >= 75].copy()
    if len(hot_days) > 0:
        hot_days.to_csv('hot_days.csv', index=False)
        print(f"✓ Hot days data ({len(hot_days)} days) saved to 'hot_days.csv'")
    
    # Export filtered data (high humidity days)
    humid_days = df[df['Humidity_%'] > 80].copy()
    if len(humid_days) > 0:
        humid_days.to_csv('high_humidity_days.csv', index=False)
        print(f"✓ High humidity days ({len(humid_days)} days) saved to 'high_humidity_days.csv'")

def main():
    """Main analysis function"""
    
    # Load and analyze data
    df = load_and_analyze_temperature_data()
    if df is None:
        return
    
    # Create visualizations
    try:
        create_temperature_visualizations(df)
    except Exception as e:
        print(f"Note: Visualization creation failed: {e}")
        print("This is normal if matplotlib display is not available.")
    
    # Export results
    export_analysis_results(df)
    
    print(f"\n" + "="*50)
    print("Temperature Data Analysis Complete!")
    print("="*50)
    print("Generated files:")
    print("- temperature_data.csv (original data)")
    print("- temperature_summary.csv (summary statistics)")
    print("- temperature_analysis.png (visualizations)")
    print("- hot_days.csv (filtered hot days)")
    print("- high_humidity_days.csv (filtered humid days)")

if __name__ == "__main__":
    main()