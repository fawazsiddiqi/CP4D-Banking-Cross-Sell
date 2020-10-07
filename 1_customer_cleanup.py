import re
import csv
import time

def openfile(filename):
    with open(filename, encoding='utf-8') as r, open('Datasets-cleaned/customer_clean.csv', 'w', newline='', encoding='utf-8') as w:
        reader = csv.DictReader(r)
        # Add all the attributes required in the new file in the array below.
        header = [
            'ACQUISITION_COST',
            'ADDRESS_HOME_CITY',
            'ADDRESS_HOME_COUNTRY',
            'ADDRESS_HOME_POSTAL_CODE',
            'ADDRESS_HOME_STATE',
            'ADDRESS_LAST_CHANGED_DATE',
            'ADDRESS_MAILING_CITY',
            'ADDRESS_MAILING_COUNTRY',
            'ADDRESS_MAILING_POSTAL_CODE',
            'ADDRESS_MAILING_STATE',
            'ADDRESS_WORK_CITY',
            'ADDRESS_WORK_COUNTRY',
            'ADDRESS_WORK_POSTAL_CODE',
            'ADDRESS_WORK_STATE',
            'ADVERTISING_INDICATOR',
            'AGE_RANGE',
            'AGGREGATION_OPT_IN_INDICATOR',
            'ANNUAL_INCOME',
            'ATTACHMENT_ALLOWED_INDICATOR',
            'BIRTH_YEAR',
            'CONTACT_PREFERENCE',
            'CREDIT_AUTHORITY_LEVEL',
            'CREDIT_SCORE',
            'CREDIT_UTILIZATION',
            'CURRENT_EMPLOYMENT_START_DATE',
            'CUSTOMER_BEHAVIOR',
            'CUSTOMER_ID',
            'DATE_FIRST_ACCOUNT_OPENED',
            'DATE_LAST_ACCOUNT_OPENED',
            'EDUCATION_LEVEL',
            'EFFECTIVE_DATE',
            'EMPLOYMENT_STATUS',
            'FAMILY_SIZE',
            'GENDER',
            'GEOGRAPHIC_AREA_HOME',
            'GEOGRAPHIC_AREA_MAILING',
            'GEOGRAPHIC_AREA_WORK',
            'HEAD_OF_HOUSEHOLD_INDICATOR',
            'HOME_OWNER_INDICATOR',
            'HOUSEHOLD_ID',
            'IMPORTANCE_LEVEL_CODE',
            'INFLUENCE_SCORE',
            'INTERNET_BANKING_INDICATOR',
            'LOYALTY_RATING_CODE',
            'MARITAL_STATUS',
            'MARKET_GROUP',
            'MONTHLY_HOUSING_COST',
            'MONTHLY_NET_INCOME',
            'NUMBER_OF_DEPENDENT_ADULTS',
            'NUMBER_OF_DEPENDENT_CHILDREN',
            'PREFERRED_COMMUNICATION_FORM',
            'PRIMARY_ADVISOR_ID',
            'PRIMARY_ADVISOR_ORGANIZATION_ID',
            'PRIMARY_BRANCH_PROXIMITY',
            'PRIMARY_SPOKEN_LANGUAGE',
            'PRIMARY_WRITTEN_LANGUAGE',
            'PROFESSION',
            'PURSUIT',
            'RECORDED_VOICE_SAMPLE_ID',
            'REFERRALS_VALUE_CODE',
            'RELATIONSHIP_START_DATE',
            'RETIREMENT_AGE',
            'SATISFACTION_RATING_FROM_SURVEY',
            'SECONDARY_ADVISOR_ID',
            'SECONDARY_ADVISOR_ORGANIZATION_ID',
            'SPECIAL_TERMS_INDICATOR',
            'STATUS',
            'STATUS_DATE',
            'STATUS_REASON',
            'URBAN_CODE',
            'WALLET_SHARE_PERCENTAGE']
        writer = csv.DictWriter(w, fieldnames=header)
        writer.writeheader()
        # Add all the attributes that need to be eliminated in the array below. 
        excluded_columns = [
            'DEATH_YEAR', 
            'DEBT_SERVICE_COVERAGE_RATIO', 
            'LIFE_CYCLE_STATUS_CHANGE_REASON',
            'LIFE_CYCLE_STATUS_CODE',
            'METRIC_BEHAVIOR_PROFILE',
            'METRIC_BEHAVIOR_PROFILE_2',
            'METRIC_BEHAVIOR_PROFILE_3',
            'METRIC_BEHAVIOR_PROFILE_4',
            'METRIC_BEHAVIOR_PROFILE_5',
            'METRIC_COMMUNICATION_STYLE',
            'METRIC_FINANCIAL_KNOWLEDGE_RATING',
            'METRIC_LATEST_TONE',
            'METRIC_NET_PROMOTER_SCORE',
            'METRIC_PERSONALITY_TYPE',
            'METRIC_SATISFACTION_LEVEL',
            'METRIC_STRENGTH_OF_RELATIONSHIP',
            'METRIC_TECH_SAVY',
            'OLDEST_DEPENDENT_ADULT_BIRTH_YEAR',
            'OLDEST_DEPENDENT_CHILD_BIRTH_YEAR',
            'PERSONAL_INTEREST_TOPIC_1',
            'PERSONAL_INTEREST_TOPIC_2',
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
            'YOUNGEST_DEPENDENT_ADULT_BIRTH_YEAR', 
            'YOUNGEST_DEPENDENT_CHILD_BIRTH_YEAR']
        for row in reader:
            for col in excluded_columns:
                row.pop(col)
            row = cleanup(row)
            writer.writerow(row)

def cleanup(row):
    return row

openfile('sample-inputs/customer.csv')