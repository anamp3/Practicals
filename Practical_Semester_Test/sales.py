import files#importing the files module
import csv
from io import StringIO
from os.path import exists # in this context this function is for checking if the file being imported is available on the textfile
from datetime import datetime#this is for the date formating
from decimal import Decimal#this is for the total formating
import locale#this is for the sales formating

#need to make sure that my container is a list of dictionaries dictionary not a list of list

regions = {"w": "West",  "m": "Mountain", "c": "Central", "e": "East"}

'''The edd sales data function checks if valid input types are entered by the user, and if yes add the data to the csv file'''
'''It also validates wherether if the correct quantities of the variables are entered'''
def Add_Sales_Data(sales):

    amount = float(input('Amount:\t\t'))
    if amount <= 0:
        print("Amount must be greater than zero.")
        print()

    while True:

        try:

            format = "%Y-%m-%d"
            date = input("Date (yyyy-mm-dd): ")

            parsed_date = datetime.strptime(date, format)
            year = parsed_date.year
            month = parsed_date.month
            day = parsed_date.day

        except ValueError:
            print("Date must be a valid 'yyyy-mm-dd' format.\n")
            continue
        else:
            region = input("Region:\t")
            if region in regions:
                sale = [date, region, amount]
                sales.append(sale)

                files.Write_Sales(sales)

                print(f"Sales for {year}-{month}-{day} added.")
                print()
            else:
                print("The region you entered is invalid, please try again.\n")
                continue
        break


'''This function is for calculating the quarter value but first checking to see the month value being passed to it.'''
def Quarter(month):
    if month == '?':
        quarter = 0
    else:
        quarter = (int(month) - 1) // 3 + 1
        
    return quarter

def Region(region):

    if region == "w":
        region = regions["w"]
    elif region == "m":
        region = regions["m"]
    elif region == "c":
        region = regions["c"]
    elif region == "e":
        region = regions["e"]
    
    return region

#this function has the code I will need to display for my import function, it was here for declutering purposes and less admin
def View_Sales(sales):
    totalAmount = 0
    grandTotal = 0
    print("\tDate\t\tQuarter\t\tRegion\t\tAmount")
    print("--------------------------------------------------------------------")
    for i, sale in enumerate (sales, start=1):

        converted = float(sale[2])
        locale.setlocale(locale.LC_ALL, 'en_us') #for my numbers to be localed I used this US localing
        localed = locale.format_string('%0.2f', converted, grouping=True) 

        #this is for getting the whole date and changing it into a date supported by python so I culd access individual variables of it
        date_str = sale[0]
        date_object = datetime.strptime(date_str, '%Y-%m-%d')
        month = date_object.month


        quarter = Quarter(int(month))
        region = Region(sale[1])
        print(f"{i}.\t{sale[0]}\t{quarter}\t\t{region}\t\t${localed}")
        totalAmount += float(sale[2])
        locale.setlocale(locale.LC_ALL, 'en_us') #for my numners to be localed I used this US localing
        grandTotal = locale.format_string('%0.2f', totalAmount, grouping=True)
    
    print("____________________________________________________________________")
    # number = Decimal(totalAmount)
    # rounded = number.quantize(Decimal('0.00'))
    print(f"TOTAL:\t\t\t\t\t\t\t${grandTotal}")
    print()

#my import couldn't import the corrupted part if the file, need to fix that
'''It saves to the textfile but doesn't when there's bad data, and when the user selects exit it clears the text file'''
def Import_Sales(sales):
    file_import = input("Enter file name to import: ")
    totalAmount = 0
    bad_data = 0
    grandTotal = 0


    '''this is for opening the textfile and checking to see if the csv file has been imported or not'''
    with open('imported_files.txt', 'r') as f:
        imported_files = f.readlines()

    '''This is the while loop that checks the textfile'''
    while True:
        if files.FILE+ '\n' in imported_files:
            print('This file has already been imported. Please clear the imported files and import once more.')
            print()
            break
        else:
            
            '''If the file that the user wants exists, it will execute the code below. If not an appropriate message will be displayed.'''
            if exists(file_import):
                files.Append_TextFile()
                print()
                print("\tDate\t\tQuarter\t\tRegion\t\tAmount")
                print("--------------------------------------------------------------------")
                for i, sale in enumerate (sales, start=1):
                    
                    date_str = sale[0]
                    date_object = datetime.strptime(date_str, '%Y-%m-%d')
                    month = date_object.month

                    if date_str == "":
                        date_str = '?'
                    if sale[1] == "":
                        sale[1] = '?'
                    if sale[2] == "":
                        sale[2] = '?'
                    
                    
                    
                    if date_str == '?' or sale[1] == '?' or sale[2] == '?':
                        print(f"{i}.*\t{date_str}\t\t{Quarter(month)}\t\t{sale[1]}${sale[2]}")
                        Clear_File()
                        bad_data += 1
                    else: #viewsales must only have this else statement in it with the enumerate above
                        converted = float(sale[2])
                        locale.setlocale(locale.LC_ALL, 'en_us') #for my numbers to be localed I used this US localing
                        localed = locale.format_string('%0.2f', converted, grouping=True) 

                        #this is for getting the whole date and changing it into a date supported by python so I culd access individual variables of it
                        date_str = sale[0]
                        date_object = datetime.strptime(date_str, '%Y-%m-%d')
                        month = date_object.month


                        quarter = Quarter(int(month))
                        region = Region(sale[1])
                        print(f"{i}.\t{sale[0]}\t{quarter}\t\t{region}\t\t${localed}")
                        totalAmount += float(sale[2])
                        locale.setlocale(locale.LC_ALL, 'en_us') #for my numners to be localed I used this US localing
                        grandTotal = locale.format_string('%0.2f', totalAmount, grouping=True)
                
                print("____________________________________________________________________")
                print(f"TOTAL:\t\t\t\t\t\t\t${grandTotal}")
                print()

                if bad_data > 0:
                    print(f"File '{file_import}' contains bad data.\nPlease correct the data in the file and try again.\n")
                break
            else:
                print("The file you are trying to import does not exist.")
                print()
                break


'''Function for clearing the textfile'''
def Clear_File():
    with open('imported_files.txt', 'r+') as f:
        f.truncate()       


#maybe in the future store this in a separate module
def Command_Menu():
    print("SALES DATA IMPORTER")
    print()
    print("COMMAND MENU")
    print("view\t- View all sales.")
    print("add\t- Add sales.")
    print("import\t- Import sales from file.")
    print("menu\t- Show menu.")
    print("clear\t- Clear imported files.")
    print("exit\t- Exit program.")
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
        elif command.lower() == "menu":
            Command_Menu()
            continue
        elif command.lower() == "exit":
            Clear_File()#This clears the text file when the user exits the application 
            break
        elif command.lower() == "clear":
            Clear_File()#This clears the text file
            print("Imported files cleared succefully!\n")
            continue
        else:
            print("The command you entered is invalid.")
            print()
            continue
    print("Bye!")
if __name__ == "__main__":
    main()
