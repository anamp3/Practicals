import csv

FILE = "sales.csv"

def Append_TextFile():
    with open('imported_files.txt', 'w') as file:
        file.write(FILE+ '\n')

def Read_TextFile():
    ithas = 0
    with open('imported_files.txt', 'r') as f:
        imported_files = f.readlines()

    while True:
        if FILE+ '\n' in imported_files:
            print('This file has already been imported.')
            ithas += 1
            break
        else:
            break
    return ithas


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