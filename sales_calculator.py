"""
Module to read CSV file and calculate total sales revenue for specific products.
"""
import csv


def calculate_product_revenue(csv_file, product_name):
    """
    Read a CSV file and calculate the total sales revenue for a specific product.
    
    Args:
        csv_file (str): Path to the CSV file containing sales data.
        product_name (str): Name of the product to calculate revenue for.
    
    Returns:
        float: Total sales revenue for the specified product.
    
    Raises:
        FileNotFoundError: If the CSV file doesn't exist.
        ValueError: If the CSV file has invalid format or missing required columns.
    """
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            
            # Verify required columns exist
            if not reader.fieldnames:
                raise ValueError("CSV file is empty or has no header")
            
            required_columns = {'product', 'quantity', 'price'}
            if not required_columns.issubset(set(reader.fieldnames)):
                raise ValueError(
                    f"CSV file must contain columns: {', '.join(required_columns)}"
                )
            
            total_revenue = 0.0
            
            for row in reader:
                if row['product'] == product_name:
                    try:
                        quantity = float(row['quantity'])
                        price = float(row['price'])
                        total_revenue += quantity * price
                    except (ValueError, KeyError) as e:
                        raise ValueError(f"Invalid data in CSV row: {e}")
            
            return total_revenue
    
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {csv_file}")


def get_all_products(csv_file):
    """
    Get a list of unique products from the CSV file.
    
    Args:
        csv_file (str): Path to the CSV file containing sales data.
    
    Returns:
        list: List of unique product names.
    """
    products = set()
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if 'product' in row:
                products.add(row['product'])
    
    return sorted(list(products))


if __name__ == "__main__":
    # Example usage
    csv_file = "sales_data.csv"
    
    try:
        # Get all products
        products = get_all_products(csv_file)
        print(f"Available products: {', '.join(products)}\n")
        
        # Calculate revenue for each product
        for product in products:
            revenue = calculate_product_revenue(csv_file, product)
            print(f"Total revenue for {product}: ${revenue:,.2f}")
    
    except Exception as e:
        print(f"Error: {e}")
