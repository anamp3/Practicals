import files
import csv

def Add_Sales_Data(sales):

    amount = float(input('Amount:\t\t'))
    year = int(input('Year:\t\t'))
    month = int(input('Month (1-12):\t'))
    day = int(input('Day (1-31):\t'))

    # this was for the try ecxcepts but they ended up no wanting my code to add to the csv file
    # print("Please enter a decimal for Amount, and integer for Year, Month, and Day")

    Quarter(month)

    sale = [year, month, day, amount]
    sales.append(sale)

    files.Write_Sales(sales)

    print(f"Sales for {year}-{month}-{day} added.")


def Quarter(month):
    quarter = (month - 1) // 3 + 1
    return quarter

def View_Sales(sales):
    print("\t\tDate\tQuater\tAmount")
    print("__________________________________________")
    

#this is for importing I am meant to put the view function in it for simpler approach
def Import_Sales(sales):
    file_import = input("Enter file name to import: ")
    
   
    with open(file_import, "r", newline="") as imported:
        line = csv.reader(imported)
        for i, sale in enumerate (line, start=1):
            print(f"{i}.\t")


    
    

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
    command = input("Please enter a command: ")
    while True:
        if command.lower() == "import":
            Import_Sales(sales)
        elif command.lower() == "add":
            Add_Sales_Data(sales)

if __name__ == "__main__":
    main()