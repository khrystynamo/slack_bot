import os # lib work system
import random # lib random 
from datetime import date, datetime # lib with date, datetime

import gspread # lib work with google sheet 
from google.oauth2 import service_account # lib oauth(creds)
# from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials # lib creds 

SERVICE_ACCOUNT_FILE = 'creds.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)


spreadsheet_id = '1381W8jtx__oojEqkY-ae2hX6H9nyYmIlj4jRzpTicWo'
spreadsheet = client.open_by_key(spreadsheet_id)

sheet_readonly = spreadsheet.worksheet('Gifts')
sheet_users = spreadsheet.worksheet('Scores')
sheet_score = spreadsheet.worksheet('Send_scores')

# task 1: all gifts name 
records = sheet_readonly.get_all_records()

# create function with doc-s
def active_gifts(records):
    for record in records: 
        if record['is_active'] == 'TRUE' and record['Amount'] >= 1:
            print(record['Gift_name'], record['Value'], record['Describe'])

# task 2: check score by user 

def get_now() -> str:
    return datetime.now().strftime('%Y-%m-%d')


def is_valid_user(user_id: str, sheet_name: str = sheet_users) -> bool:
    """_summary_

    Args:
        user_id (str): _description_

    Returns:
        bool: _description_
    """
    records = sheet_name.get_all_records()
    
    for record in records:
        if record['user_id'] == user_id:
            return True 
    return False


def get_score(user_id: str, sheet_name: str = sheet_users) -> int | None:
    
    records = sheet_name.get_all_records()
    for record in records: 
        if user_id == record['user_id']:
            return record['score'] # if more than one score, need sum 
        
    return None    


user_id = 10001
user_id_second = 10002 

if is_valid_user(user_id) and is_valid_user(user_id_second):
    
    score_user_id = (user_id, get_score(user_id))
    score_user_id2 = (user_id_second, get_score(user_id_second))
    
    score = 500
    
    if score_user_id[1] >= score:
        sheet_score.append_row([score_user_id[0], score_user_id2[0], score, get_now(), 'for gifts'])
        
        # MARK: /// Update Scores sheet
             
    else:
        print(f'No score {score_user_id[0]}')
        
def get_records(sheet_users):
    tmp = 0
    for record in sheet_users.get_all_records():
        if record['date'] == get_now():
            tmp += record['score']
        print(f'User_id: {user_id}\n. Score: {tmp}.\n Date: {get_now()}')
        
#do we need to check is_valid_user every time?

#send thanks at the end of the month

#support

sheet_readonly = spreadsheet.worksheet('Support')
sheet_support = spreadsheet.worksheet('Support')
headers = sheet_support.row_values(1)
column_name = "description"
try:
    col_index = headers.index(column_name) + 1 
except ValueError:
    raise Exception(f"Колонку з назвою '{column_name}' не знайдено")

support_phrases = sheet_support.col_values(col_index)[1:]

def generate_support_message():
    return random.choice(support_phrases)

support_message = generate_support_message()
print(support_message)

#do we need to do that every time?

