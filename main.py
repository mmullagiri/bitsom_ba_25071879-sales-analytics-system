"""
Docstring for main

    Main execution function

    Workflow:
    1. Print welcome message
    2. Read sales data file (handle encoding)
    3. Parse and clean transactions
    4. Display filter options to user
       - Show available regions
       - Show transaction amount range
       - Ask if user wants to filter (y/n)
    5. If yes, ask for filter criteria and apply
    6. Validate transactions
    7. Display validation summary
    8. Perform all data analyses (call all functions from Part 2)
    9. Fetch products from API
    10. Enrich sales data with API info
    11. Save enriched data to file
    12. Generate comprehensive report
    13. Print success message with file locations

    Error Handling:
    - Wrap entire process in try-except
    - Display user-friendly error messages
    - Don't let program crash on errors

    Expected Console Output:
    ========================================
    SALES ANALYTICS SYSTEM
    ========================================

    [1/10] Reading sales data...
    ✓ Successfully read 95 transactions

    [2/10] Parsing and cleaning data...
    ✓ Parsed 95 records

    [3/10] Filter Options Available:
    Regions: North, South, East, West
    Amount Range: ₹500 - ₹90,000

    Do you want to filter data? (y/n): n

    [4/10] Validating transactions...
    ✓ Valid: 92 | Invalid: 3

    [5/10] Analyzing sales data...
    ✓ Analysis complete

    [6/10] Fetching product data from API...
    ✓ Fetched 30 products

    [7/10] Enriching sales data...
    ✓ Enriched 85/92 transactions (92.4%)

    [8/10] Saving enriched data...
    ✓ Saved to: data/enriched_sales_data.txt

    [9/10] Generating report...
    ✓ Report saved to: output/sales_report.txt

    [10/10] Process Complete!
    ========================================
    

if __name__ == "__main__":
    main()

"""

import utils.file_handler
import utils.data_processor

def main():
    #[0/10] Print welcome message
    print ("========================================")
    print("SALES ANALYTICS SYSTEM")
    print ("========================================\n")

    folderpath = "data/sales_data.txt" 
    result = utils.file_handler.read_sales_data(folderpath, 'utf-8')
    print("[1/10] Reading sales data...")
    print("✓ Successfully read ",len(result), " transactions \n")

    result1 = utils.file_handler.parse_transactions(result)
    print("[2/10] Parsing and cleaning data...")
    print("✓ Parsed", len(result1), " records\n")
    

    print("[3/10] Filter Options Available:")
    latest_list1, invalid_count1, filter_summary1 = utils.file_handler.validate_and_filter(result1)
    print("\n")

    q = input( "Do you want to filter data? y/n \n")
    if q=="y":
        print("Great!, Please provide Filter Criteria from Filter Options available above within the range,\n else the application will not function as expected")
        region = str(input("region: "))
        min_amt = float(input("min_amt: "))
        max_amt = float(input("max_amt: "))

        latest_list, invalid_count, filter_summary = utils.file_handler.validate_and_filter(result1,region,min_amt, max_amt)
        print("[4/10] Validating transactions...")
        print("✓ Valid: ", len(latest_list1), "| Invalid: ", invalid_count, "\n")
        print("Total Input Records: ", filter_summary["total_input"])
        print("Invalid records: ", filter_summary["invalid"])
        print("Count records after filtering by region: ", filter_summary["total_input"]-filter_summary["invalid"]-filter_summary["filtered_out_region_count"])
        print("Count records after filtering by min_amt: ", filter_summary["total_input"]-filter_summary["invalid"]-filter_summary["filtered_out_region_count"]-filter_summary["filtered_out_min_amt_count"])
        print("Count records after filtering by min_amt: ", filter_summary["total_input"]-filter_summary["invalid"]-filter_summary["filtered_out_region_count"]-filter_summary["filtered_out_min_amt_count"]-filter_summary["filtered_out_max_amt_count"])
        print("\n")


    else:
        print("you dont want to filter")
        
   
    print("[5/10] Analyzing sales data...")
    print("✓ Analysis complete")
    
    total_revenue = utils.data_processor.calculate_total_revenue(latest_list1)
    print(total_revenue)




    


    #result3 = utils.file_handler.validate_and_filter(result1)
    #total_revenue = utils.data_processor.calculate_total_revenue(result1)
    #print("TOTAL REVENUE = ", total_revenue)

main()