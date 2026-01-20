import chardet
import csv

def read_sales_data(filename,file_encoder):
    """
    Reads sales data from file handling encoding issues

    Returns: list of raw lines (strings)

    Expected Output Format:
    ['T001|2024-12-01|P101|Laptop|2|45000|C001|North', ...]

    Requirements:
    - Use 'with' statement
    - Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    - Handle FileNotFoundError with appropriate error message
    - Skip the header row
    - Remove empty lines
    """
    try:
        data = []
        with open(file=filename, mode='r', encoding=file_encoder, newline='\n') as file:
            file_contents = csv.reader(file, delimiter='|' )
            header = next(file_contents, None)

            for row in file_contents:
                if row and any(field.strip for field in row):
                    data.append('|'.join(row))
        return data
    
    # handle non utf-8 encoded data 
    except UnicodeEncodeError:
        print (f'{filename} file is not in UTF-8 encoding')
        return data
    except FileNotFoundError:
        print (f'{filename} file is not found')
        return data

def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries

    Returns: list of dictionaries with keys:
    ['TransactionID', 'Date', 'ProductID', 'ProductName',
     'Quantity', 'UnitPrice', 'CustomerID', 'Region']

    Expected Output Format:
    [
        {
            'TransactionID': 'T001',
            'Date': '2024-12-01',
            'ProductID': 'P101',
            'ProductName': 'Laptop',
            'Quantity': 2,           # int type
            'UnitPrice': 45000.0,    # float type
            'CustomerID': 'C001',
            'Region': 'North'
        },
        ...
    ]

    Requirements:
    - Split by pipe delimiter '|'
    - Handle commas within ProductName (remove or replace)
    - Remove commas from numeric fields and convert to proper types
    - Convert Quantity to int
    - Convert UnitPrice to float
    - Skip rows with incorrect number of fields
    """
    data = []
    for line in raw_lines:
        t_id, dt, p_id, p_name, qty_raw, price_raw, c_id, region=[f.strip() for f in line.split('|')]
        
        p_name_clean = p_name.replace(",", " ").strip()
        qty_raw_clean = qty_raw.replace(",", " ").strip()
        price_raw_clean = price_raw.replace(",", " ").strip()

        try:
            qty = int(qty_raw_clean)
            unit_price = float(price_raw_clean)
        except ValueError:
            continue

        data.append(
           {
               # TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region
               # t_id, dt, p_id, p_name, qty_raw, price_raw, c_id, region=[f.strip() for f in line.split('|')]
               "TransactionID":t_id,
               "Date": dt,
               "ProductID": p_id,
               "ProductName": p_name,
               "Quantity": qty_raw,
               "UnitPrice": price_raw,
               "CustomerID": c_id,
               "Region": region
           }
        )
    return data


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters

    Parameters:
    - transactions: list of transaction dictionaries
    - region: filter by specific region (optional)
    - min_amount: minimum transaction amount (Quantity * UnitPrice) (optional)
    - max_amount: maximum transaction amount (optional)

    Returns: tuple (valid_transactions, invalid_count, filter_summary)

    Expected Output Format:
    (
        [list of valid filtered transactions],
        5,  # count of invalid transactions
        {
            'total_input': 100,
            'invalid': 5,
            'filtered_by_region': 20,
            'filtered_by_amount': 10,
            'final_count': 65
        }
    )

    Validation Rules:
    - Quantity must be > 0 --checked for each transaction, and appended to valid list if valid
    - UnitPrice must be > 0 --checked for each transaction, and appended to valid list if valid
    - All required fields must be present -- checked for each transaction, and appended to valid list if valid
    - TransactionID must start with 'T' --checked for each transaction, and appended to valid list if valid
    - ProductID must start with 'P' --checked for each transaction, and appended to valid list if valid
    - CustomerID must start with 'C' --checked for each transaction, and appended to valid list if valid

    Filter Display:
    - Print available regions to user before filtering
    - Print transaction amount range (min/max) to user
    - Show count of records after each filter applied
    """
    required_fields = ["TransactionID", "Date", "ProductID", "ProductName", "Quantity", "UnitPrice", "CustomerID", "Region"]
    input_size = len(transactions)
    valid_transactions = []
    invalid_count = 0


    
    # Filter Display: Print transaction amount range (min/max) to user

    # validate transactions

    # check if all required fields present, and if all ok, then proceed with other checks. 
    for t in transactions:
        if not isinstance(t,dict):
            invalid_count +=1 
            continue
    
        missing = [k for k in required_fields if k not in t or t[k] in (None,"")]

        if missing:
            invalid_count +=1
            continue

        # - TransactionID must start with 'T'      
        if not str(t["TransactionID"]).startswith("T"):
            invalid_count +=1
            continue

        # - ProductID must start with 'P'
        if not str(t["ProductID"]).startswith("P"):
            invalid_count +=1
            continue
     
        # - CustomerID must start with 'C'
        if not str(t["CustomerID"]).startswith("C"):
            invalid_count +=1
            continue

        try:
            qty = int(t["Quantity"])
            unit_price = float(t["UnitPrice"])
        except (ValueError,TypeError):
            invalid_count =+1
            continue

        # - Quantity must be > 0
        if qty<=0:
            invalid_count += 1
            continue 

        if unit_price <=0:
            invalid_count += 1
            continue 

        t["Quantity"] = qty
        t["UnitPrice"] = unit_price

        valid_transactions.append(t)

    # print("ALL VALID TRANSACTIONS -----> ", valid_transactions)

    # Filter Display:
    # Print available regions to user before filtering
    # Print transaction amount range (min/max) to user
    # Show count of records after each filter applied
    # Filter Display: Print available regions to user before filtering
    
    regions = sorted({
        t.get("Region","").strip() 
        for t in transactions 
        if isinstance(t,dict) and t.get("Region")
    })
    print("Available regions: ", regions if regions else "None Found")
    
    if valid_transactions: 
        amounts = [valid_transaction["Quantity"]*valid_transaction["UnitPrice"] for valid_transaction in valid_transactions]
        print(f"Transaction amount range (valid only): min = {min(amounts):,.2f}, max = {max(amounts):,.2f}")
    else:
        print("No transaction to provide min and max amount")    

    # order of filters from method signature: region, min amount, max amount
    #region_filter = 0
    #amount_filter = 0
    
    filtered_out_region_count = 0
    filtered_out_min_amt_count = 0 
    filtered_out_max_amt_count = 0
    latest_list = valid_transactions

    def calc_amt(t):
        return t["Quantity"]*t["UnitPrice"]
    
    if region is not None:
        # t_by_region = all valid transactions for the selected region
        pre_filter = len(latest_list) 
        latest_list = [filtered_t for filtered_t in latest_list if str(filtered_t.get("Region")).strip().lower() == str(region).strip().lower()]
                
        filtered_out_region_count = pre_filter-len(latest_list)
        #print(f"After region filter, ({region}): {len(latest_list)} records")

    if min_amount is not None:
        # t_gt_min = subset of t_by_region and greater than Quantity*UnitPrice > min_amount
        pre_filter = len(latest_list) 
        #print("In min filter", pre_filter)
        
        latest_list = [filtered_t for filtered_t in latest_list if ((filtered_t["Quantity"]))* (filtered_t["UnitPrice"]) >= float(min_amount)]
        #print("shortlisted txn list length ... # of recs that have amt >300", len(latest_list))
        
        filtered_out_min_amt_count = pre_filter-len(latest_list)
        #print(f"After min_amount filter, ({min_amount}): {len(latest_list)} records")

        #print("hi")


    if max_amount is not None:
        # t_lt_max = subset of t_by_region and greater than Quantity*UnitPrice < max_amount
        pre_filter = len(latest_list) 
        latest_list = [filtered_t for filtered_t in latest_list if ((filtered_t["Quantity"]))* (filtered_t["UnitPrice"]) <= float(max_amount)]
        filtered_out_max_amt_count = pre_filter-len(latest_list)
        #print(f"After min_amount filter, ({max_amount}): {len(latest_list)} records")

    filter_summary = {
        "total_input": len(transactions),
        "invalid": invalid_count,
        "filtered_out_region_count": filtered_out_region_count,
        "filtered_out_min_amt_count": filtered_out_min_amt_count,
        "filtered_out_max_amt_count": filtered_out_max_amt_count,
        "final_count": len(latest_list)
    }

    #print ("Filter Summary", filter_summary)    
    #Returns: tuple (valid_transactions, invalid_count, filter_summary)
    return latest_list, invalid_count, filter_summary








