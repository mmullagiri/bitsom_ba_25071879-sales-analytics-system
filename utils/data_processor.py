"""
    2.1 Calculates total revenue from all transactions

    Returns: float (total revenue)

    Expected Output: Single number representing sum of (Quantity * UnitPrice)
    Example: 1545000.50

"""
def calculate_total_revenue(transactions):
    total_revenue = 0

    length = len(transactions)
    print("length of .... ", length)

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

    region_statistics = {}
    grand_total = 0.0

    for t in transactions:
        region = "North"
