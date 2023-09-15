import files
import csv
from io import StringIO
from os.path import exists

def Add_Sales_Data(sales):
    while True:
        try:
            amount = float(input('Amount:\t\t'))
            if amount <= 0:
                print("Amount must be greater than zero.")
                print()
                continue
            year = int(input('Year:\t\t'))
            if year < 2000 or year > 9999:
                print("The year should be between 2000 and 9999, inclusive.")
                print()
                continue
            month = int(input('Month (1-12):\t'))
            if month < 1 or month > 12:
                print("The month value should be between 1 and 12.")
                print()
                continue
            day = int(input('Day (1-31):\t'))
            print()
            if day >= 1 and day <= 31:
                if (month == 4 or month == 6 or month == 9 or month == 11) and day >= 31:
                    print("The maximum day for month 4, 6, 9 and 11 is 30.")
                    print()
                    continue
                elif month == 2 and day >= 29:
                    print("The maximum day for month 2 is 28.")
                    print()
                    continue
            else:
                print("The days should be between 1 and 31, inclusive.")
                print()
                continue
        except ValueError:
            print("Please enter a decimal for amount, and integers for values year, month, and day.")
        else:
            # this was for the try ecxcepts but they ended up no wanting my code to add to the csv file
            # print("Please enter a decimal for Amount, and integer for Year, Month, and Day")

            sale = [year, month, day, amount]
            sales.append(sale)

            files.Write_Sales(sales)

            print(f"Sales for {year}-{month}-{day} added.")
            print()
        break


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
    print("\tDate\t\tQuarter\t\tAmount")
    print("------------------------------------------------")
    for i, sale in enumerate (sales, start=1):
        
        quarter = Quarter(int(sale[1]))
        print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{quarter}\t\t${sale[3]}")
        totalAmount += float(sale[3])

    print("________________________________________________")
    print(f"TOTAL:\t\t\t\t\t${totalAmount}")
    print()

    
        
    
    

#There is a textfile function that I need to do before importing
#It saves to the textfile but doesn't when there's bad data, and when the user selects exit it clears the text file
def Import_Sales(sales):
    file_import = input("Enter file name to import: ")
    totalAmount = 0
    bad_data = 0

    files.Read_TextFile()
    files.Append_TextFile()
    

    #imported the IO class or module then converted the input from the user to a csv file  so I can be able to loop trough it
    converted = StringIO(file_import)

    if exists(file_import):

    # if not ".csv" in file_import:
    #     file_import += ".csv"
    
        print()
        print("\tDate\t\tQuarter\t\tAmount")
        print("------------------------------------------------")
        for i, sale in enumerate (sales, start=1):
            
            if sale[0] == "":
                sale[0] = '?'
            if sale[1] == "":
                sale[1] = '?'
            if sale[2] == "":
                sale[2] = '?'
            if sale[3] == "":
                sale[3] = '?'
            
            if sale[0] == '?' or sale[1] == '?' or sale[2] == '?' or sale[3] == '?':
                print(f"{i}.*\t{sale[0]}-{sale[1]}-{sale[2]}\t{Quarter(sale[1])}\t\t${sale[3]}")
                files.Clear_File()
                bad_data += 1
            else: #viewsales must onlu have this else statement in it with the enumerate above
                quarter = Quarter(int(sale[1]))
                print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{quarter}\t\t${sale[3]}")
                totalAmount += float(sale[3])
        
        print("________________________________________________")
        print(f"TOTAL:\t\t\t\t\t${totalAmount}")
        print()
        if bad_data > 0:
            print(f"File '{file_import}' contains bad data.\nPlease correct the data in the file and try again.\n")
    else:
        print("The file you are trying to import does not exist.")
        print()
    
        



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
            Import_Sales(sales)
        elif command.lower() == "add":
            Add_Sales_Data(sales)
        elif command.lower() == "view":
            View_Sales(sales)
        elif command.lower() == "exit":
            files.Clear_File()
            break
    print("Bye!")
if __name__ == "__main__":
    main()
