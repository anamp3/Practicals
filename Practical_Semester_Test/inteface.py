import classes
from classes import Regions, Region, DailySales, SalesList,File, FileImportError
import files

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

def Clear_File():
    with open('imported_files.txt', 'r+') as f:
        f.truncate()

def main():
    Clear_File()
    Command_Menu()

    while True:
        command = input("Please enter a command: ")
        if command.lower() == "import":
            
            file_import = input("Enter file name to import: ")
            split_file = file_import.split('_')#spliting the file bythe underscore

            #declaring the variables on the splitted file
            # lastsection = split_file[3]

            # #spliting the last section r.csv into extention and region so that I can be able to access the both individually
            # lastsection_split = lastsection.split(".")
            # fileName = split_file[0] +'.'+ lastsection_split[1]

            #Region objects
            west = Region('w', 'West')
            east = Region('e', 'East')
            mountain = Region('m', 'Mountain')
            central = Region('c', 'Central')

            #Regions object with Region objects in it
            regions = Regions()
            regions.regional_list
            regions.createRegion(west)
            regions.createRegion(east)
            regions.createRegion(mountain)
            regions.createRegion(central)
            
            


            file = File(file_import, regions, 'sales_qn_yyyy_r.csv')
            file.filenameValidity()

            
        # elif command.lower() == "add":


            
        # elif command.lower() == "view":


            
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
