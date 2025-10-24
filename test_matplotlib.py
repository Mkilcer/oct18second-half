#!/usr/bin/env python3
"""
Test script to verify matplotlib installation and functionality
"""

def test_imports():
    """Test if required modules can be imported"""
    print("Testing imports...")
    
    try:
        import csv
        print("✓ csv module imported successfully")
    except ImportError:
        print("✗ Failed to import csv module")
        return False
    
    try:
        import matplotlib
        print(f"✓ matplotlib imported successfully (version: {matplotlib.__version__})")
    except ImportError:
        print("✗ Failed to import matplotlib")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✓ matplotlib.pyplot imported successfully")
    except ImportError:
        print("✗ Failed to import matplotlib.pyplot")
        return False
    
    return True

def test_csv_file():
    """Test if CSV file exists and is readable"""
    print("\nTesting CSV file...")
    
    import csv
    import os
    
    csv_file = 'sales_revenue.csv'
    
    if not os.path.exists(csv_file):
        print(f"✗ CSV file '{csv_file}' not found")
        return False
    
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            print(f"✓ CSV file readable, contains {len(rows)} rows")
            print(f"  Header: {rows[0] if rows else 'No data'}")
            return True
    except Exception as e:
        print(f"✗ Error reading CSV file: {e}")
        return False

def create_simple_chart():
    """Create a simple test chart"""
    print("\nCreating test chart...")
    
    try:
        import matplotlib.pyplot as plt
        
        # Simple test data
        x = ['A', 'B', 'C']
        y = [1, 2, 3]
        
        plt.figure(figsize=(6, 4))
        plt.bar(x, y)
        plt.title('Test Chart')
        plt.savefig('test_chart.png')
        plt.close()  # Close without showing
        
        print("✓ Test chart created successfully as 'test_chart.png'")
        return True
    except Exception as e:
        print(f"✗ Error creating test chart: {e}")
        return False

def main():
    """Run all tests"""
    print("Matplotlib Installation and Functionality Test")
    print("=" * 50)
    
    success = True
    
    success &= test_imports()
    success &= test_csv_file()
    success &= create_simple_chart()
    
    print("\n" + "=" * 50)
    if success:
        print("✓ All tests passed! Ready to run the chart generator.")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    
    return success

if __name__ == "__main__":
    main()