import csv

FILE = "sales.csv"

def Append_TextFile():
    with open('imported_files.txt', 'w') as file:
        file.write(FILE+ '\n')

def Read_TextFile():
    with open('imported_files.txt', 'r') as f:
        imported_files = f.readlines()

    if FILE+ '\n' in imported_files:
        print('This file has already been imported.')
    else:
        print('This file has not been imported yet.')



'''This is the input that will be from the user'''
def Write_Sales(sales):
    with open(FILE, 'w',) as file:
        write = csv.writer(file)
        write.writerows(sales)

def Read_Sales():
    sales = []
    with open(FILE, 'r', newline="")as file:
        read = csv.reader(file)
        for line in read: 
            sales.append(line)
    return sales