import files
import csv
from io import StringIO

def Add_Sales_Data(sales):

    amount = float(input('Amount:\t\t'))
    year = int(input('Year:\t\t'))
    month = int(input('Month (1-12):\t'))
    day = int(input('Day (1-31):\t'))

    # this was for the try ecxcepts but they ended up no wanting my code to add to the csv file
    # print("Please enter a decimal for Amount, and integer for Year, Month, and Day")

    sale = [year, month, day, amount]
    sales.append(sale)

    files.Write_Sales(sales)

    print(f"Sales for {year}-{month}-{day} added.")


def Quarter(month):
    if month == '?':
        quarter = 0
    else:
        quarter = (month - 1) // 3 + 1
        
    return quarter

#need to set the alignment of these tabs and amounts displayed and also tell the user that this file contains bad data
#impot must take the code of view sales
def View_Sales(sales):
    totalAmount = 0
    bad_data = 0
    print("\t\tDate\tQuarter\tAmount")
    print("__________________________________________")
    for i, sale in enumerate (sales, start=1):
        
        quarter = Quarter(int(sale[1]))
        print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{quarter}\t ${sale[3]}")
        totalAmount += float(sale[3])

    print("__________________________________________")
    print(f"TOTAL:\t\t\t\t${totalAmount}")

    
        
    
    

#this is for importing I am meant to put the view function in it for simpler approach
def Import_Sales():
    file_import = input("Enter file name to import: ")
    totalAmount = 0
    bad_data = 0

    #imported the IO class or module then converted the input from the user to a csv file  so I can be able to loop trough it
    converted = StringIO(file_import)

    reader = csv.reader(converted)

    # if not ".csv" in file_import:
    #     file_import += ".csv"
        

    print("\t\tDate\tQuarter\tAmount")
    print("__________________________________________")
    for i, sale in enumerate (reader, start=1):
        
        if sale[0] == "":
            sale[0] = '?'
        if sale[1] == "":
            sale[1] = '?'
        if sale[2] == "":
            sale[2] = '?'
        if sale[3] == "":
            sale[3] = '?'
        
        if sale[0] == '?' or sale[1] == '?' or sale[2] == '?' or sale[3] == '?':
            print(f"{i}.*\t{sale[0]}-{sale[1]}-{sale[2]}\t{Quarter(sale[1])}\t ${sale[3]}")
            bad_data += 1
        else: #viewsales must onlu have this else statement in it with the enumerate above
            quarter = Quarter(int(sale[1]))
            print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{quarter}\t ${sale[3]}")
            totalAmount += float(sale[3])
    
    print("__________________________________________")
    print(f"TOTAL:\t\t\t\t${totalAmount}")
    
        



#maybe in the future store this in a separate module
def Command_Menu():
    print("SALES DATA IMPORTER")
    print()
    print("COMMAND MENU")
    print("view\t- View all sales")
    print("add\t- Add sales")
    print("import\t- Import sales from file")
    print("menu\t- Show menu")
    print("exit\t- Exit program")
    print()

def main():
    Command_Menu()
    sales = files.Read_Sales()
    while True:
        command = input("Please enter a command: ")
        if command.lower() == "import":
            Import_Sales()
        elif command.lower() == "add":
            Add_Sales_Data(sales)
        elif command.lower() == "view":
            View_Sales(sales)

if __name__ == "__main__":
    main()
