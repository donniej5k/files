# Task 1: Travel Blog Sentiment Analysis
import re

def analyze_blog_sentiments(blog_file):
    positive_words = ['amazing', 'enjoy', 'beautiful', 'wonderful', 'memorable', 'fantastic', 'excellent']
    negative_words = ['disappointing', 'poor', 'crowded', 'lackluster']

    positive_count = 0
    negative_count = 0

    try:
        # Open the travel blog file for reading
        with open(blog_file, 'r') as file:
            # Read each line (blog entry) from the file
            for line in file:
                # Convert the line to lower case for case-insensitive matching
                lower_line = line.lower()

                # Count positive words
                for word in positive_words:
                    if re.search(r'\b' + re.escape(word) + r'\b', lower_line):
                        positive_count += 1

                # Count negative words
                for word in negative_words:
                    if re.search(r'\b' + re.escape(word) + r'\b', lower_line):
                        negative_count += 1

        # Print the results
        print(f"Sentiment Analysis Report for '{blog_file}':")
        print(f"Positive words count: {positive_count}")
        print(f"Negative words count: {negative_count}")

    except FileNotFoundError:
        print(f"Error: The file '{blog_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File containing travel blog entries
blog_file = "travel_blogs.txt"

# Perform sentiment analysis on the travel blog file
analyze_blog_sentiments(blog_file)
print("Task 1 Complete")
# Task 2: Historical Weather Data Compiler

import os
from collections import defaultdict

def analyze_weather_data(files):
    yearly_temperatures = defaultdict(list)

    try:
        # Process each file
        for file in files:
            print(f"Processing file: {file}")
            with open(file, 'r') as f:
                # Read each line in the file
                for line in f:
                    print(f"Raw line: {line.strip()}")  # Debug: Print raw line
                    # Split the line by comma to separate date and temperature
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        date = parts[0].strip()
                        temp_str = parts[1].strip().rstrip('°C')  # Strip '°C' from temperature string
                        print(f"Parsed: Date={date}, Temperature={temp_str}")  # Debug: Print parsed components
                        # Extract year from date (assuming date format is YYYY-MM-DD)
                        year = date.split('-')[0]
                        try:
                            # Convert temperature to integer
                            temperature = int(temp_str)
                            # Add temperature to the list for the corresponding year
                            yearly_temperatures[year].append(temperature)
                        except ValueError:
                            print(f"Warning: Ignoring invalid temperature '{temp_str}' in {file}")

        # Calculate average temperature for each year
        average_temperatures = {}
        for year, temps in yearly_temperatures.items():
            average_temperatures[year] = sum(temps) / len(temps)

        # Identify the year with the highest average temperature
        if average_temperatures:
            highest_avg_year = max(average_temperatures, key=average_temperatures.get)
            highest_avg_temp = average_temperatures[highest_avg_year]

            # Print the results
            print("\nYearly Average Temperatures:")
            for year, avg_temp in average_temperatures.items():
                print(f"{year}: {avg_temp:.2f}°C")
            print(f"\nYear with the highest average temperature: {highest_avg_year} ({highest_avg_temp:.2f}°C)")
        else:
            print("No valid temperature data found.")

    except FileNotFoundError as e:
        print(f"Error: {e}")

# Get current working directory
current_directory = os.getcwd()

# List of weather data files in the current directory
weather_files = [
    os.path.join(current_directory, "weather_2020.txt"),
    os.path.join(current_directory, "weather_2021.txt"),
    os.path.join(current_directory, "weather_2022.txt")
]

# Perform analysis on weather data
analyze_weather_data(weather_files)
print("Task 2 Complete")
