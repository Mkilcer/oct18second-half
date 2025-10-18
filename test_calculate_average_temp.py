#!/usr/bin/env python3
"""
Unit tests for calculate_average_temp.py
"""

import unittest
import os
import csv
from calculate_average_temp import calculate_daily_average


class TestCalculateAverageTemp(unittest.TestCase):
    """Test cases for temperature calculation functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_csv = 'test_temp_data.csv'
        
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)
    
    def test_calculate_daily_average_basic(self):
        """Test basic average calculation with simple data."""
        # Create test CSV
        with open(self.test_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Day', 'Temperature'])
            writer.writerow(['Monday', '70'])
            writer.writerow(['Monday', '80'])
            writer.writerow(['Tuesday', '60'])
        
        averages = calculate_daily_average(self.test_csv)
        
        self.assertEqual(averages['Monday'], 75.0)
        self.assertEqual(averages['Tuesday'], 60.0)
    
    def test_calculate_daily_average_multiple_days(self):
        """Test average calculation with multiple readings per day."""
        with open(self.test_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Day', 'Temperature'])
            writer.writerow(['Monday', '72'])
            writer.writerow(['Monday', '75'])
            writer.writerow(['Monday', '68'])
            writer.writerow(['Monday', '70'])
        
        averages = calculate_daily_average(self.test_csv)
        
        self.assertEqual(averages['Monday'], 71.25)
    
    def test_calculate_with_empty_rows(self):
        """Test that empty rows are properly skipped."""
        with open(self.test_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Day', 'Temperature'])
            writer.writerow(['Monday', '70'])
            writer.writerow(['Monday', '80'])
            writer.writerow(['', ''])  # Empty row
            writer.writerow(['Tuesday', '60'])
        
        averages = calculate_daily_average(self.test_csv)
        
        self.assertEqual(averages['Monday'], 75.0)
        self.assertEqual(averages['Tuesday'], 60.0)
        self.assertEqual(len(averages), 2)
    
    def test_calculate_with_whitespace_and_invalid_data(self):
        """Test that whitespace-only and invalid data are properly skipped."""
        with open(self.test_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Day', 'Temperature'])
            writer.writerow(['Monday', '70'])
            writer.writerow(['  ', '80'])  # Whitespace-only day
            writer.writerow(['Tuesday', '  '])  # Whitespace-only temperature
            writer.writerow(['Wednesday', 'abc'])  # Invalid temperature
            writer.writerow(['Thursday', '65'])
        
        averages = calculate_daily_average(self.test_csv)
        
        self.assertEqual(averages['Monday'], 70.0)
        self.assertEqual(averages['Thursday'], 65.0)
        self.assertEqual(len(averages), 2)
    
    def test_actual_data_file(self):
        """Test with the actual temperature_data.csv file."""
        if os.path.exists('temperature_data.csv'):
            averages = calculate_daily_average('temperature_data.csv')
            
            # Check that all days of the week are present
            expected_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                           'Friday', 'Saturday', 'Sunday']
            
            for day in expected_days:
                self.assertIn(day, averages)
                self.assertGreater(averages[day], 0)
            
            # Verify Monday's average from our test data
            self.assertEqual(averages['Monday'], 71.25)


if __name__ == '__main__':
    unittest.main()
