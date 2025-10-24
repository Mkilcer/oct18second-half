#!/usr/bin/env python3
"""
CSV Data Visualization Program
Reads sales_revenue.csv and generates a bar chart
Date: October 18, 2025
"""

import csv
import matplotlib.pyplot as plt
import os

def read_csv_data(filename):
    """Read CSV file and return products and revenues as separate lists"""
    products = []
    revenues = []
    
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 2:  # Ensure row has at least 2 columns
                    products.append(row[0])
                    revenues.append(float(row[1]))
                    
        return products, revenues
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return None, None
    except ValueError as e:
        print(f"Error: Invalid data format in CSV file. {e}")
        return None, None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None

def create_bar_chart(products, revenues, save_file=True):
    """Create and display a bar chart from the data"""
    
    # Create the figure and axis
    plt.figure(figsize=(12, 8))
    
    # Create bar chart
    bars = plt.bar(products, revenues, color='skyblue', edgecolor='navy', linewidth=1.2)
    
    # Customize the chart
    plt.title('Sales Revenue by Product', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Products', fontsize=12, fontweight='bold')
    plt.ylabel('Revenue ($)', fontsize=12, fontweight='bold')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on top of each bar
    for bar, revenue in zip(bars, revenues):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'${revenue:.2f}', ha='center', va='bottom', fontsize=10)
    
    # Add grid for better readability
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the chart
    if save_file:
        output_file = 'sales_revenue_chart.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Chart saved as '{output_file}'")
    
    # Display the chart
    plt.show()

def display_data_summary(products, revenues):
    """Display a summary of the data"""
    print("\n" + "="*50)
    print("DATA SUMMARY")
    print("="*50)
    print(f"Total products: {len(products)}")
    print(f"Total revenue: ${sum(revenues):.2f}")
    print(f"Average revenue: ${sum(revenues)/len(revenues):.2f}")
    print(f"Highest revenue: ${max(revenues):.2f} ({products[revenues.index(max(revenues))]})")
    print(f"Lowest revenue: ${min(revenues):.2f} ({products[revenues.index(min(revenues))]})")
    print("="*50)

def main():
    """Main function to run the program"""
    print("CSV Data Visualization Program")
    print("Reading sales_revenue.csv and generating bar chart...")
    print("-" * 50)
    
    # Read the CSV data
    csv_file = 'sales_revenue.csv'
    products, revenues = read_csv_data(csv_file)
    
    if products is None or revenues is None:
        print("Failed to read CSV data. Exiting...")
        return
    
    # Display data summary
    display_data_summary(products, revenues)
    
    # Print the data
    print("\nDATA FROM CSV:")
    print("-" * 30)
    for product, revenue in zip(products, revenues):
        print(f"{product:12} | ${revenue:8.2f}")
    print("-" * 30)
    
    # Create and display the bar chart
    print("\nGenerating bar chart...")
    create_bar_chart(products, revenues)
    
    print("\nProgram completed successfully!")

if __name__ == "__main__":
    main()