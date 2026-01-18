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



