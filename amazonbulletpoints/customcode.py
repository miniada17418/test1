import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.styles import NamedStyle, PatternFill, Font
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.cell.cell import WriteOnlyCell
import datetime
from datetime import date, timedelta
import pandas as pd
from pandas import read_csv
import csv, codecs
import os

from .models import ItemCodeToPull, ItemDetail

def file_upload(f):
    handle_uploaded_file(f)

    joined_data = join_data()

    list_data = create_df_list(joined_data)

    return list_data



def handle_uploaded_file(f):
    #converts the file name to include today's date
    time = datetime.datetime.today().strftime('%d-%m-%y')
    fileLocation = 'media/amazon/uploads/amazonupload{}.csv'.format(time)
    with open(fileLocation, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #function that formats the file for uploading into the QBImportFile table
    with open(fileLocation, 'r') as upload:
        reader = csv.reader(upload)
        reader.__next__()
        for row in reader:
            _, created = ItemCodeToPull.objects.get_or_create(
            itemCode = row[0],
            )

def join_data():
    joined_table_file_name = 'media/amazon/uploads/amz_joined_tables.csv'
    df = pd.DataFrame(list(ItemDetail.objects.all().values('itemCode','yahooID','itemName','description')))
    df = df[['itemCode','yahooID','itemName','description']]

    df2 = pd.DataFrame(list(ItemCodeToPull.objects.all().values('itemCode')))
    df2 =df2[['itemCode']]

    df3 = pd.merge(df, df2, on='itemCode')

    df3.to_csv(joined_table_file_name, sep=',', encoding='utf-8')

    return joined_table_file_name


def create_df_list(x):
    time = datetime.datetime.today().strftime('%d-%m-%y')
    fileLocation = 'media/amazon/uploads/amazon{}.csv'.format(time)

    headers = ['itemCode','yahooID', 'itemName', 'description', 'amzbulletpoint1',
                'amzbulletpoint2','amzbulletpoint3','amzbulletpoint4','amzbulletpoint5']
    with open(x, 'rt', encoding='utf8') as readCSV, open(fileLocation, 'w', newline="", encoding='utf8') as writeCSV:
        readCSV = csv.DictReader(readCSV, delimiter=',' )
        writer = csv.DictWriter(writeCSV, fieldnames=headers, extrasaction='ignore', lineterminator='\n')
        writer.writeheader()
        issue = []
        for row in readCSV:
            try:
                writer.writerow(row)
            except:
                issue.append(row['itemCode'])
                print(issue)

    return fileLocation
