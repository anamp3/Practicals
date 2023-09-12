import files

def Add_Sales_Data(sales):
    amount = float(input('Amount:\t\t'))
    year = int(input('Year:\t\t'))
    month = int(input('Month (1-12):\t'))
    day = int(input('Day (1-31):\t'))

    quarter = (month - 1) // 3 + 1
    sale = [year, month, day, quarter, amount]
    sales.append(sale)

    files.Write_Sales(sales)

    print(f"Sales for {year}-{month}-{day} added.")


def Import_Sales(sales):
    print("\tDate\tQuater\tAmount")
    print("__________________________________________")
    for i, sale in enumerate(sales, start=1):
        if sale[0] or sale[1] or sale[2] or sale[3] or sale[4] == 0:
            print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{sale[3]}\t{sale[4]}")
            totalValue += sale[4]
        else:
            print(f"{i}.\t{sale[0]}-{sale[1]}-{sale[2]}\t{sale[3]}\t{sale[4]}")
            totalValue += sale[4]
    
    


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
