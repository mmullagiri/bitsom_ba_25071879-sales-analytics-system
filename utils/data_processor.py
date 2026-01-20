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
    

