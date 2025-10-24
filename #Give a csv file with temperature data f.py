#Give a csv file with temperature data for each day of the week, find the average temperature for each day
import csv
import os
import pandas as pd 


# Read example CSV file with daily temperature data
file_path = 'temperature_data.csv'
df = pd.read_csv(file_path) 


#Find the average temperature for each day
average_temps = df.groupby('Day')['Temperature'].mean()
print("Average Temperatures for Each Day:")
for day, temp in average_temps.items():
    print(f"{day}: {temp:.2f}°F")   


# Filter data