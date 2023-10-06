import datetime
import classes
from classes import Regions, Region, DailySales, SalesList,File, FileImportError, DATE_FORMAT
import files, sales

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


#Regions object with Region objects in it
regions = Regions()
regions.regional_list
regions.createRegion('w', 'West')
regions.createRegion('e', 'East')
regions.createRegion('m', 'Mountain')
regions.createRegion('c', 'Central')

def Clear_File():
    with open('imported_files.txt', 'r+') as f:
        f.truncate()

def main():
    Clear_File()
    Command_Menu()

    while True:
        # print(regions.regional_list)
        sale = files.Read_Sales()
        command = input("Please enter a command: ")
        if command.lower() == "import":
            sales.Import_Sales(sale)

            
        elif command.lower() == "add":
            sales.Add_Sales_Data(sale)


            
        elif command.lower() == "view":
            sales.View_Sales(sale)


            
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
