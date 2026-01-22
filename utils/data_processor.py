"""
    2.1 Calculates total revenue from all transactions

    Returns: float (total revenue)

    Expected Output: Single number representing sum of (Quantity * UnitPrice)
    Example: 1545000.50

"""
def calculate_total_revenue(transactions):
    total_revenue = 0
    for t in transactions:
        qty = int(t.get("Quantity"))
        price = float(t.get("UnitPrice"))
        total_revenue += qty * price
        #print("total revenue IS :::::::", qty, price, total_revenue)

    return round(total_revenue,2)
    
def region_wise_sales(transactions):
    """
    Analyzes sales by region
    Returns: dictionary with region statistics
    Expected Output Format:
    {
        'North': {
            'total_sales': 450000.0,
            'transaction_count': 15,
            'percentage': 29.13
        },
        'South': {...},
        ...
    }

    Requirements:
    - Calculate total sales per region
    - Count transactions per region
    - Calculate percentage of total sales
    - Sort by total_sales in descending order
    """

    region_statistics = {"North":{"total_sales":0.0,"transaction_count":0, "percentage":0.0},"South":{"total_sales":0.0,"transaction_count":0, "percentage":0.0},"East":{"total_sales":0.0,"transaction_count":0, "percentage":0.0},"West":{"total_sales":0.0,"transaction_count":0, "percentage":0.0}}
       
    grand_total = 0.0

    for t in transactions:
        region = str(t.get("Region")).strip()
        qty = int(t.get("Quantity"))
        price = float(t.get("UnitPrice"))
        amount = qty * price

        if not region:
            continue

        grand_total += amount

        region_statistics[region]["total_sales"] += amount
        region_statistics[region]["transaction_count"] += 1
    
    for region in region_statistics:
        region_statistics[region]["percentage"] = f"{((region_statistics[region]["total_sales"]/grand_total)*100):.2f}"
    
    print("region stats", region_statistics)


def top_selling_products(transactions, n=5):
    """
    Finds top n products by total quantity sold

    Returns: list of tuples

    Expected Output Format:
    [
        ('Laptop', 45, 2250000.0),  # (ProductName, TotalQuantity, TotalRevenue)
        ('Mouse', 38, 19000.0),
        ...
    ]

    Requirements:
    - Aggregate by ProductName
    - Calculate total quantity sold
    - Calculate total revenue for each product
    - Sort by TotalQuantity descending
    - Return top n products
    """

    product_statistics = {}
    grand_total = 0.0

    for t in transactions:
        ProductName = str(t.get("ProductName")).strip()
        qty = int(t.get("Quantity"))
        price = float(t.get("UnitPrice"))
        amount = qty * price

        if not ProductName:
            continue

        if ProductName not in product_statistics:
            product_statistics[ProductName] = {                
                "total_qty": 0,
                "total_revenue": 0.0
            }

        product_statistics[ProductName]["total_qty"] += qty
        product_statistics[ProductName]["total_revenue"] += amount

    top_n = sorted(product_statistics.items(), key=lambda x: x[1]["total_qty"],reverse=True)[:n]
        
    for ProductName, metrics in top_n:
        print(ProductName, metrics["total_qty"], metrics["total_revenue"])



        
