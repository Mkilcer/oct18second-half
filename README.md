# oct18second-half
Questions 6-10

## Sales Revenue Calculator

This project provides code to read a CSV file and calculate total sales revenue for specific products.

### Features

- Read sales data from CSV files
- Calculate total revenue for a specific product
- Get a list of all available products
- Comprehensive error handling
- Full test suite

### Files

- `sales_calculator.py` - Main module with revenue calculation functions
- `sales_data.csv` - Sample CSV file with sales data
- `test_sales_calculator.py` - Comprehensive test suite

### CSV Format

The CSV file should have the following columns:
- `product` - Name of the product
- `quantity` - Number of units sold
- `price` - Price per unit

Example:
```csv
product,quantity,price
Laptop,5,1200.00
Mouse,10,25.50
Keyboard,8,75.00
```

### Usage

#### Calculate Revenue for a Specific Product

```python
from sales_calculator import calculate_product_revenue

# Calculate total revenue for "Laptop"
revenue = calculate_product_revenue('sales_data.csv', 'Laptop')
print(f"Total revenue for Laptop: ${revenue:,.2f}")
```

#### Get All Products

```python
from sales_calculator import get_all_products

products = get_all_products('sales_data.csv')
print(f"Available products: {', '.join(products)}")
```

#### Run the Example

```bash
python sales_calculator.py
```

This will display the total revenue for each product in the sales_data.csv file.

### Running Tests

Run the test suite to verify functionality:

```bash
python -m unittest test_sales_calculator -v
```

All tests should pass, validating:
- Single product revenue calculation
- Multiple entries for the same product
- Non-existent products (returns 0)
- Error handling for missing files
- Invalid CSV format detection
- Decimal value support
- Case-sensitive product matching

### Example Output

```
Available products: Headphones, Keyboard, Laptop, Monitor, Mouse

Total revenue for Headphones: $1,000.00
Total revenue for Keyboard: $975.00
Total revenue for Laptop: $12,000.00
Total revenue for Monitor: $3,500.00
Total revenue for Mouse: $637.50
```
