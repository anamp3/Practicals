import csv

FILE = "sales.csv"
 
# with open('imported_files.txt', 'r') as f:
#     imported_files = f.readlines()

# if FILE + '\n' in imported_files:
#     print('This file has already been imported.')


'''This is the input that will be from the user'''
def Write_Sales(sales):
    with open(FILE, 'w', newline="") as file:
        write = csv.writer(file)
        write.writerows(file)

def Read_Sales():
    sales = [[]]
    with open(FILE, 'r', newline="")as file:
        read = csv.reader(file)
        for line in read:
            sales.append(line)
    return sales