# Run the the script with this command `python3 2_customer_summary_cleanup.py`
import re
import csv
import time

def openfile(filename):
    #New file that will be created with cleaned up data
    with open(filename, encoding='utf-8') as r, open('Datasets-cleaned/customer_summary_clean.csv', 'w', newline='', encoding='utf-8') as w:
        reader = csv.DictReader(r)
        # Add all the attributes required in the new file in the array below.
        header = [
            'AGGREGATE_RETAIL_SPEND',
            'AMOUNT_OF_MANAGEMENT_FEES',
            'ANNUAL_INCOME_OTHER',
            'ARREARS',
            'ASSETS',
            'AVERAGE_SENTIMENT_SCORE',
            'CUSTOMER_ID',
            'CUSTOMER_LIFETIME_VALUE',
            'END_DATE',
            'EXPERIENCE_NUMBER_OF_PERIODS',
            'EXPERIENCE_RATING',
            'FINANCIAL_ASSETS',
            'FUNDS_UNDER_MANAGEMENT',
            'LATEST_SENTIMENT_SCORE',
            'LIABILITIES',
            'LIQUID_NET_WORTH',
            'LOG_INS_MARKET_DOWNTURN',
            'LOG_INS_MARKET_UPTURN',
            'NON_FINANCIAL_ASSETS',
            'NUMBER_OF_30_DAY_DELINQUENCIES',
            'NUMBER_OF_ACCOUNTS',
            'NUMBER_OF_ACTIVE_ACCOUNTS',
            'NUMBER_OF_CALLS',
            'NUMBER_OF_COMMUNICATIONS',
            'NUMBER_OF_COMPLAINTS',
            'NUMBER_OF_CREDIT_BUREAU_INQUIRIES',
            'NUMBER_OF_DORMANT_CREDIT_CARD_ARRANGEMENTS',
            'NUMBER_OF_EMAILS',
            'NUMBER_OF_HARD_INQUIRIES',
            'NUMBER_OF_LOGINS',
            'NUMBER_OF_MOBILE_LOGINS',
            'NUMBER_OF_NEW_ACCOUNTS_OPENED',
            'NUMBER_OF_OPEN_COMPLAINTS',
            'NUMBER_OF_POSTS',
            'NUMBER_OF_RECOMMENDATIONS',
            'NUMBER_OF_REPORTED_CREDIT_CHECKS',
            'NUMBER_OF_REPORTED_MAIL_STOLEN_INCIDENTS',
            'NUMBER_OF_SOFT_INQUIRIES',
            'NUMBER_OF_TRADING_PERIODS',
            'NUMBER_OF_TRANSACTIONS',
            'PRIORITY',
            'REAL_PROPERTY_ASSETS',
            'RETURN_10Y',
            'RETURN_1Y',
            'RETURN_2Y',
            'RETURN_3Y',
            'RETURN_5Y',
            'RETURN_LAST_QUARTER',
            'RETURN_SINCE_INCEPTION',
            'RETURN_YTD',
            'SOURCE_SYSTEM_ID',
            'START_DATE',
            'TOP_SPENDING_CATEGORY',
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
            'TOTAL_CLOSING_BALANCE_CREDIT_CARDS',
            'TOTAL_CLOSING_BALANCE_LOANS',
            'TOTAL_CLOSING_CASH_BALANCE',
            'TOTAL_COMMUNICATIONS_AND_IT_EXPENSE',
            'TOTAL_INWARD_CALLS',
            'TOTAL_INWARD_COMMUNICATIONS',
            'TOTAL_INWARD_EMAILS',
            'TOTAL_LOGIN_OR_QUERIES',
            'TOTAL_NET_WORTH',
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
            'TYPE']
        writer = csv.DictWriter(w, fieldnames=header)
        writer.writeheader()
        # Add all the attributes that need to be eliminated in the array below. 
        excluded_columns = [
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
            'USER_DEFINED_STRING_5']
        for row in reader:
            for col in excluded_columns:
                row.pop(col)
            row = cleanup(row)
            writer.writerow(row)

def cleanup(row):
    return row

#File that needs to be cleaned
openfile('sample-inputs/customer_summary.csv')