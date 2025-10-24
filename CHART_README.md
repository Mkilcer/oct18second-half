# CSV Data Visualization with Matplotlib

This project contains scripts to install matplotlib and generate bar charts from CSV data.

## Files

- `run_chart_program.ps1` - PowerShell script to install matplotlib and run the chart generator
- `csv_chart_generator.py` - Main Python program that reads CSV data and creates bar charts
- `test_matplotlib.py` - Test script to verify matplotlib installation
- `sales_revenue.csv` - Sample CSV data file with product sales information
- `import csv.py` - Original CSV handling code

## How to Use

### Option 1: Run the PowerShell Script (Recommended)

1. Open PowerShell as Administrator (for package installation)
2. Navigate to the project directory:
   ```powershell
   cd "c:\Users\Miche\OneDrive\Documents\GitHub\Kilcer-108-5\oct18second-half"
   ```
3. Allow script execution (if needed):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Run the main script:
   ```powershell
   .\run_chart_program.ps1
   ```

### Option 2: Manual Installation and Execution

1. Install matplotlib:
   ```powershell
   pip install matplotlib
   ```
2. Test the installation:
   ```powershell
   python test_matplotlib.py
   ```
3. Generate the chart:
   ```powershell
   python csv_chart_generator.py
   ```

## What the Scripts Do

### PowerShell Script (`run_chart_program.ps1`)
- Checks for Python and pip installation
- Installs matplotlib package
- Verifies matplotlib installation
- Lists matplotlib-related packages
- Runs the test script
- Executes the main chart generation program

### Chart Generator (`csv_chart_generator.py`)
- Reads data from `sales_revenue.csv`
- Creates a bar chart with product names and revenue values
- Displays data summary (total, average, highest, lowest revenue)
- Saves the chart as `sales_revenue_chart.png`
- Shows the chart in a window

### Test Script (`test_matplotlib.py`)
- Tests import functionality for required modules
- Verifies CSV file exists and is readable
- Creates a simple test chart to ensure matplotlib works

## Output

After running the scripts, you will get:
- `sales_revenue_chart.png` - Bar chart of the sales data
- `test_chart.png` - Simple test chart (if test script runs)
- Console output showing data summary and status messages

## Sample CSV Data

The `sales_revenue.csv` file contains:
- Product names (Laptop, Mouse, Keyboard, etc.)
- Revenue values for each product
- Header row: Product, Revenue

## Requirements

- Python 3.x
- pip (Python package installer)
- PowerShell (for the automation script)
- matplotlib (installed automatically by the script)

## Troubleshooting

If you encounter issues:
1. Ensure Python is installed and in your PATH
2. Check that pip is working: `pip --version`
3. Try installing matplotlib manually: `pip install matplotlib`
4. Make sure you have write permissions in the directory
5. Check PowerShell execution policy if scripts won't run

## Chart Features

The generated bar chart includes:
- Product names on x-axis (rotated for readability)
- Revenue values on y-axis
- Value labels on top of each bar
- Grid lines for better readability
- Professional styling with colors and borders
- High-resolution output (300 DPI)