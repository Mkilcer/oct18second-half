import csv
from gettext import install

import pip

# Sample sales data
sales_data = [
    ['Product', 'Revenue'],
    ['Laptop', 1200.50],
    ['Mouse', 25.99],
    ['Keyboard', 75.00],
    ['Monitor', 299.99],
    ['Headphones', 89.95],
    ['Webcam', 45.50],
    ['Printer', 150.00],
    ['Tablet', 399.99],
    ['Phone', 699.99],
    ['Speakers', 125.75]
]

# Create CSV file
with open('sales_revenue.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

print("CSV file 'sales_revenue.csv' created successfully!")

# Read the CSV file and find revenue for a specific product
def find_product_revenue(product_name):
    try:
        with open('sales_revenue.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0].lower() == product_name.lower():
                    return float(row[1])
        return None
    except FileNotFoundError:
        print("CSV file not found!")
        return None

# Get user input and find revenue
product_to_find = input("Enter product name to find revenue: ")
revenue = find_product_revenue(product_to_find)

if revenue is not None:
    print(f"Revenue for {product_to_find}: ${revenue:.2f}")
else:
    print(f"Product '{product_to_find}' not found in the data.")


# Create a text file with a list of numbers
# Sample numbers
numbers = [10, 23, 45, 67, 89, 12, 34, 56, 78, 90]

#write a function that finds the sum of all the numbers in the text file
with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")
print("Text file 'numbers.txt' created successfully!")
def sum_of_numbers_in_file(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            for line in file:
                total += int(line.strip())
        return total
    except FileNotFoundError:
        print("Text file not found!")
        return None 
    
# Calculate and print the sum of numbers in the text file
sum_numbers = sum_of_numbers_in_file('numbers.txt')
if sum_numbers is not None:
    print(f"Sum of numbers in 'numbers.txt': {sum_numbers}")  


#Function that reads a JSON file and prints the contents
import json
import random
from datetime import datetime, timedelta
def update_json_with_user_input(filename):
    try:
        user_name = input("Enter your name: ")
        user_age = int(input("Enter your age: "))
        user_city = input("Enter your city: ")

        with open(filename, 'r+') as file:
            data = json.load(file)
            data.update({'name': user_name, 'age': user_age, 'city': user_city})
            file.seek(0)
            json.dump(data, file)
            file.truncate()
    except ValueError:
        print("Invalid age input. Please enter a number.")
    except FileNotFoundError:
        print("JSON file not found!")

        # Create CSV file with temperature data for April

        # Generate temperature data for April (30 days)
        april_temp_data = [['Date', 'Temperature (°F)']]

        # Start date: April 1st
        start_date = datetime(2024, 4, 1)

        for day in range(30):
            current_date = start_date + timedelta(days=day)
            date_str = current_date.strftime('%Y-%m-%d')
            # Generate random temperature between 50-80°F for spring weather
            temperature = round(random.uniform(50, 80), 1)
            april_temp_data.append([date_str, temperature])

        # Write to CSV file
        with open('april_temperatures.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(april_temp_data)

        print("CSV file 'april_temperatures.csv' created successfully!")

        #Find the average of april_temperatures.csv
def calculate_average_temperature(filename):
    try:
        with open   (filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            total_temp = 0
            count = 0
            for row in reader:
                total_temp += float(row[1])
                count += 1
            average_temp = total_temp / count if count > 0 else 0
            return average_temp
    except FileNotFoundError:
        print("CSV file not found!")
        return None

# Calculate and print the average temperature
average_temperature = calculate_average_temperature('april_temperatures.csv')
if average_temperature is not None:
    print(f"Average temperature in 'april_temperatures.csv': {average_temperature:.2f}°F")