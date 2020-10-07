# Run the the script with this command `python3 2_customer_summary_cleanup.py`
import re
import csv
import time

def openfile(filename):
    #New file that will be created with cleaned up data
    with open(filename, encoding='utf-8') as r, open('Datasets-cleaned/customer_product_summary_clean.csv', 'w', newline='', encoding='utf-8') as w:
        reader = csv.DictReader(r)
        # Add all the attributes required in the new file in the array below.
        header = [
            'ACTIVITY_FEES',
            'COMMUNICATIONS_AND_IT_EXPENSE',
            'CUSTOMER_ID',
            'END_DATE',
            'INTEREST_EXPENSE',
            'INTEREST_INCOME',
            'LAST_CUSTOMER_REPLIED_TO_OFFER_INDICATOR',
            'LAST_CUSTOMER_REPLY_TIME',
            'LAST_INBOUND_COMMUNICATION_DATE',
            'LAST_INBOUND_COMMUNICATION_ID',
            'LAST_OUTBOUND_COMMUNICATION_DATE',
            'LAST_OUTBOUND_COMMUNICATION_ID',
            'LAST_PRODUCT_OFFER_CAMPAIGN',
            'LAST_PRODUCT_OFFER_DATE',
            'MANAGEMENT_FEES',
            'OTHER_NON_INTEREST_EXPENSE',
            'OTHER_NON_INTEREST_INCOME',
            'PRODUCT_ID',
            'PRODUCT_OFFERED_INDICATOR',
            'PRODUCT_OWNED_INDICATOR',
            'SENTIMENT_SCORE',
            'START_DATE',
            'STATUS',
            'STATUS_DATE',
            'STATUS_REASON',
            'WAIVED_INTEREST_EXPENSE',
            'WAIVED_INTEREST_INCOME',
            'WAIVED_NON_INTEREST_EXPENSE'
            ]
        writer = csv.DictWriter(w, fieldnames=header)
        writer.writeheader()
        # Add all the attributes that need to be eliminated in the array below. 
        excluded_columns = [
            'AMOUNT_OF_MANAGEMENT_FEES',
            'ARREARS',
            'AVERAGE_SENTIMENT_SCORE',
            'LATEST_SENTIMENT_SCORE',
            'LIFETIME_VALUE',
            'LIQUID_NET_WORTH',
            'NUMBER_OF_ACCOUNTS',
            'NUMBER_OF_ACTIVE_ACCOUNTS',
            'NUMBER_OF_CALLS',
            'NUMBER_OF_COMMUNICATIONS',
            'NUMBER_OF_COMPLAINTS',
            'NUMBER_OF_EMAILS',
            'NUMBER_OF_NEW_ACCOUNTS_OPENED',
            'NUMBER_OF_OPEN_COMPLAINTS',
            'NUMBER_OF_RECOMMENDATIONS',
            'NUMBER_OF_TRADING_PERIODS',
            'NUMBER_OF_TRANSACTIONS',
            'TOTAL_AMOUNT_OF_ALL_FEES',
            'TOTAL_AMOUNT_OF_BUY_TRADES',
            'TOTAL_AMOUNT_OF_COMMISSION',
            'TOTAL_AMOUNT_OF_DEPOSITS',
            'TOTAL_AMOUNT_OF_INTEREST_EARNED',
            'TOTAL_AMOUNT_OF_INTEREST_FEES',
            'TOTAL_AMOUNT_OF_MARKET_CHANGE',
            'TOTAL_AMOUNT_OF_SELL_TRADES',
            'TOTAL_AMOUNT_OF_TRANSACTION_FEES',
            'TOTAL_AMOUNT_OF_WAIVED_FEES',
            'TOTAL_AMOUNT_OF_WITHDRAWALS',
            'TOTAL_CALL_TIME',
            'TOTAL_CLOSING_BALANCE',
            'TOTAL_CLOSING_CASH_BALANCE',
            'TOTAL_INWARD_CALLS',
            'TOTAL_INWARD_COMMUNICATIONS',
            'TOTAL_INWARD_EMAILS',
            'TOTAL_NUMBER_OF_ACCOUNTS_AS_NON_PRIMARY',
            'TOTAL_NUMBER_OF_ACCOUNTS_AS_PRIMARY',
            'TOTAL_NUMBER_OF_ACTIVE_COMMUNICATION_THREADS',
            'TOTAL_NUMBER_OF_ALL_FEES',
            'TOTAL_NUMBER_OF_BUY_TRADES',
            'TOTAL_NUMBER_OF_DEPOSITS',
            'TOTAL_NUMBER_OF_SELL_TRADES',
            'TOTAL_NUMBER_OF_UNITS_BOUGHT',
            'TOTAL_NUMBER_OF_UNITS_SOLD',
            'TOTAL_NUMBER_OF_WITHDRAWALS',
            'TOTAL_OUTWARD_CALLS',
            'TOTAL_OUTWARD_COMMUNICATIONS',
            'TOTAL_OUTWARD_EMAILS',
            'TRADING_VOLUME',
            'TYPE',
            'USER_DEFINED_BOOLEAN_1',
            'USER_DEFINED_BOOLEAN_2',
            'USER_DEFINED_BOOLEAN_3',
            'USER_DEFINED_BOOLEAN_4',
            'USER_DEFINED_BOOLEAN_5',
            'USER_DEFINED_DATE_1',
            'USER_DEFINED_DATE_2',
            'USER_DEFINED_DATE_3',
            'USER_DEFINED_DATE_4',
            'USER_DEFINED_DATE_5',
            'USER_DEFINED_INTEGER_1',
            'USER_DEFINED_INTEGER_2',
            'USER_DEFINED_INTEGER_3',
            'USER_DEFINED_INTEGER_4',
            'USER_DEFINED_INTEGER_5',
            'USER_DEFINED_NUMERIC_1',
            'USER_DEFINED_NUMERIC_2',
            'USER_DEFINED_NUMERIC_3',
            'USER_DEFINED_NUMERIC_4',
            'USER_DEFINED_NUMERIC_5',
            'USER_DEFINED_STRING_1',
            'USER_DEFINED_STRING_2',
            'USER_DEFINED_STRING_3',
            'USER_DEFINED_STRING_4',
            'USER_DEFINED_STRING_5',
            'WAIVED_FEES']
        for row in reader:
            for col in excluded_columns:
                row.pop(col)
            row = cleanup(row)
            writer.writerow(row)

def cleanup(row):
    return row

#File that needs to be cleaned
openfile('sample-inputs/customer_product_summary.csv')