import re
import csv
import time
import pandas as pd

def Merge_Customer_summary():
    df1 = pd.read_csv("Dataset-Final/customer_clean.csv")
    df2 = pd.read_csv("Dataset-Final/customer_summary_clean.csv")

    df = df1.merge(df2, how='left', on='CUSTOMER_ID') 
    # df = pd.concat([df1.reset_index(), df2], axis=1).set_index("CUSTOMER_ID")
    df.to_csv("Dataset-Final/merge_customer_summary1.csv", index=False)

Merge_Customer_summary()