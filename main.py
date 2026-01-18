import utils.file_handler
import os

folderpath = "/Users/mmullagiri/OneDrive - DXC Production/Documents/GitHub/bitsom_ba_25071879-sales-analytics-system/data/sales_data.txt" 

result = utils.file_handler.read_sales_data(folderpath, 'utf-8')
result1 = utils.file_handler.parse_transactions(result)
#parse_transactions(raw_lines):
print(result1)
print("First element of the dictionary", result1[:1])