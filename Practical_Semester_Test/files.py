import csv
import re
from classes import FileImportError,Regions

FILE = "sales.csv"

def Append_TextFile():
    with open('imported_files.txt', 'w') as file:
        file.write(FILE+ '\n')



'''This is the input that will be from the user'''
def Write_Sales(sales):
    with open(FILE, 'w',newline="") as file:
        write = csv.writer(file)
        write.writerows(sales)

def Read_Sales():
    sales = []
    with open(FILE, 'r',)as file:
        read = csv.reader(file)
        for line in read: 
            sales.append(line)
    return sales

def import_file(fileName, imported_file):
    
    if fileName in imported_file:
        raise FileImportError(f"The file '{fileName}' has already been imported.")
    
    if not re.match(r"^sales_q\d_\d{4}_[a-zA-Z]+\.csv$", fileName):
        raise FileImportError(f"The file '{fileName}' has invalid format.")
    
    try:
        Read_Sales()
    
    except FileImportError:
        raise FileImportError(f"File {fileName} was not found.")
