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



        
