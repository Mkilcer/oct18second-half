"""
Unit tests for the sales_calculator module.
"""
import unittest
import os
import tempfile
import csv
from sales_calculator import calculate_product_revenue, get_all_products


class TestSalesCalculator(unittest.TestCase):
    """Test cases for sales calculator functions."""
    
    def setUp(self):
        """Set up test fixtures before each test."""
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        self.temp_filename = self.temp_file.name
        
        # Write test data
        writer = csv.writer(self.temp_file)
        writer.writerow(['product', 'quantity', 'price'])
        writer.writerow(['Laptop', '5', '1200.00'])
        writer.writerow(['Mouse', '10', '25.50'])
        writer.writerow(['Keyboard', '8', '75.00'])
        writer.writerow(['Laptop', '3', '1200.00'])
        writer.writerow(['Mouse', '15', '25.50'])
        self.temp_file.close()
    
    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.temp_filename):
            os.remove(self.temp_filename)
    
    def test_calculate_single_product_revenue(self):
        """Test calculating revenue for a product with a single entry."""
        revenue = calculate_product_revenue(self.temp_filename, 'Keyboard')
        expected = 8 * 75.00  # 600.00
        self.assertEqual(revenue, expected)
    
    def test_calculate_multiple_entries_revenue(self):
        """Test calculating revenue for a product with multiple entries."""
        revenue = calculate_product_revenue(self.temp_filename, 'Laptop')
        expected = (5 * 1200.00) + (3 * 1200.00)  # 9600.00
        self.assertEqual(revenue, expected)
    
    def test_calculate_multiple_entries_mouse(self):
        """Test calculating revenue for Mouse with multiple entries."""
        revenue = calculate_product_revenue(self.temp_filename, 'Mouse')
        expected = (10 * 25.50) + (15 * 25.50)  # 637.50
        self.assertEqual(revenue, expected)
    
    def test_nonexistent_product(self):
        """Test calculating revenue for a product that doesn't exist."""
        revenue = calculate_product_revenue(self.temp_filename, 'NonExistent')
        self.assertEqual(revenue, 0.0)
    
    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent file."""
        with self.assertRaises(FileNotFoundError):
            calculate_product_revenue('nonexistent.csv', 'Laptop')
    
    def test_invalid_csv_format(self):
        """Test that ValueError is raised for invalid CSV format."""
        # Create a CSV file with missing required columns
        invalid_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        writer = csv.writer(invalid_file)
        writer.writerow(['name', 'amount'])  # Wrong column names
        writer.writerow(['Product1', '100'])
        invalid_file.close()
        
        try:
            with self.assertRaises(ValueError):
                calculate_product_revenue(invalid_file.name, 'Product1')
        finally:
            os.remove(invalid_file.name)
    
    def test_empty_csv_file(self):
        """Test that ValueError is raised for empty CSV file."""
        empty_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        empty_file.close()
        
        try:
            with self.assertRaises(ValueError):
                calculate_product_revenue(empty_file.name, 'Laptop')
        finally:
            os.remove(empty_file.name)
    
    def test_get_all_products(self):
        """Test getting all unique products from CSV."""
        products = get_all_products(self.temp_filename)
        expected = ['Keyboard', 'Laptop', 'Mouse']
        self.assertEqual(products, expected)
    
    def test_decimal_values(self):
        """Test that decimal prices and quantities are handled correctly."""
        # Create a CSV with decimal quantities
        decimal_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv')
        writer = csv.writer(decimal_file)
        writer.writerow(['product', 'quantity', 'price'])
        writer.writerow(['Widget', '2.5', '10.99'])
        writer.writerow(['Widget', '1.5', '10.99'])
        decimal_file.close()
        
        try:
            revenue = calculate_product_revenue(decimal_file.name, 'Widget')
            expected = (2.5 * 10.99) + (1.5 * 10.99)  # 43.96
            self.assertAlmostEqual(revenue, expected, places=2)
        finally:
            os.remove(decimal_file.name)
    
    def test_case_sensitive_product_names(self):
        """Test that product names are case-sensitive."""
        revenue = calculate_product_revenue(self.temp_filename, 'laptop')
        self.assertEqual(revenue, 0.0)  # Should not match 'Laptop'


class TestWithRealCSV(unittest.TestCase):
    """Test cases using the actual sales_data.csv file if it exists."""
    
    def test_real_csv_laptop_revenue(self):
        """Test calculating Laptop revenue from sales_data.csv."""
        csv_file = 'sales_data.csv'
        if os.path.exists(csv_file):
            revenue = calculate_product_revenue(csv_file, 'Laptop')
            # Laptop appears 3 times: 5*1200 + 3*1200 + 2*1200 = 12000
            expected = 12000.00
            self.assertEqual(revenue, expected)
    
    def test_real_csv_mouse_revenue(self):
        """Test calculating Mouse revenue from sales_data.csv."""
        csv_file = 'sales_data.csv'
        if os.path.exists(csv_file):
            revenue = calculate_product_revenue(csv_file, 'Mouse')
            # Mouse appears 2 times: 10*25.50 + 15*25.50 = 637.50
            expected = 637.50
            self.assertEqual(revenue, expected)


if __name__ == '__main__':
    unittest.main()
