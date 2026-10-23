import csv

# A sales analyzer that reads sales data, calculates revenue and quantity metrics, and generates reports.


sales_data = []

with open("sales_data.csv", "r") as file:
    """reads sales_data.csv using csv.DictReader. Converts price to float and quantity to int, then appends each row to sales_data."""
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['date']}, {row['product']}, {row['price']}, {row['quantity']}")
        row["price"] = float(row["price"])
        row["quantity"] = int(row["quantity"])
        sales_data.append(row)

    """Initializes total revenue, revenue per product, quantity per product, and revenue per day."""
total_revenue = 0
revenue_per_product = {}
quantity_per_product = {}
revenue_per_day = {}

for row in sales_data:
    """Processes each row in sales_data to calculate total revenue, revenue per product, quantity per product, and revenue per day."""
    date = row["date"]
    product = row["product"]
    price = row["price"]
    quantity = row["quantity"]
    revenue = price * quantity

    total_revenue += revenue

    if product not in revenue_per_product:
        revenue_per_product[product] = 0
    revenue_per_product[product] += revenue

    if product not in quantity_per_product:
        quantity_per_product[product] = 0
    quantity_per_product[product] += quantity

    if date not in revenue_per_day:
        revenue_per_day[date] = 0
    revenue_per_day[date] += revenue

highest_revenue_day = max(revenue_per_day, key=revenue_per_day.get)

with open("sales_report.txt", "w") as report_file:
    """Writes a formatted summary to sales_report.txt including total revenue, revenue per product, quantity per product, and the highest revenue day."""
    report_file.write(f"Total Revenue: {total_revenue:.2f}\n")
    report_file.write("Revenue per Product:\n")
    for product, revenue in revenue_per_product.items():
        report_file.write(f"  {product}: {revenue:.2f}\n")
    report_file.write("Quantity per Product:\n")
    for product, quantity in quantity_per_product.items():
        report_file.write(f"  {product}: {quantity}\n")
    report_file.write(f"Highest Revenue Day: {highest_revenue_day}\n")

with open("product_summary.csv", "w", newline="") as summary_file:
    """Writes a summary CSV called product_summary.csv with columns: product, total_quantity, total_revenue."""
    writer = csv.DictWriter(summary_file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader()
    for product in revenue_per_product:
        writer.writerow({
            "product": product,
            "total_quantity": quantity_per_product[product],
            "total_revenue": f"{revenue_per_product[product]:.2f}"
        })
        
        
        
        

 


