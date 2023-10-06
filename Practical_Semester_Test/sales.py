import files#importing the files module
import csv
from io import StringIO
from os.path import exists # in this context this function is for checking if the file being imported is available on the textfile
from datetime import datetime#this is for the date formating
from decimal import Decimal#this is for the total formating
import locale#this is for the sales formating
import re#for the regular expression that I will be using
import os
import inteface
from classes import Regions, DailySales, SalesList,File, FileImportError, DATE_FORMAT




#need to make sure that my container is a list of dictionaries dictionary not a list of list

regions = {"w": "West",  "m": "Mountain", "c": "Central", "e": "East"}

regions_class = Regions()
regions_class.regional_list
regions_class.createRegion('w', 'West')
regions_class.createRegion('e', 'East')
regions_class.createRegion('m', 'Mountain')
regions_class.createRegion('c', 'Central')
'''The edd sales data function checks if valid input types are entered by the user, and if yes add the data to the csv file'''
'''It also validates wherether if the correct quantities of the variables are entered'''
def Add_Sales_Data(sales):

    amount = float(input('Amount:\t\t'))
    if amount <= 0:
        print("Amount must be greater than zero.")
        print()

    while True:

        try:

            date = input("Date (yyyy-mm-dd): ")

            parsed_date = datetime.strptime(date, DATE_FORMAT)
            year = parsed_date.year
            month = parsed_date.month
            day = parsed_date.day

        except ValueError:
            print("Date must be a valid 'yyyy-mm-dd' format.\n")
            continue
        else:
            region = input("Region:\t")
            particular_region = regions_class.validRegionCodes()
            if region in regions:
                sale = {"d":date, "r":region, "a":amount}
                
                sale_list = list(sale.values())

                sales.append(sale_list)
            
                #change sales back to a list to write to a file
                files.Write_Sales(sales)

                print(f"Sales for {year}-{month}-{day}  added.")
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


def View_Sales(sales):
    totalAmount = 0
    grandTotal = 0
    print(f"{'':<8}{'Date' :<15}{'Quarter' :<15}{'Region' :<15}{'Amount' :>15}")
    print("--------------------------------------------------------------------")
    for i, sale in enumerate (sales, start=1):

        converted = float(sale[2])
        locale.setlocale(locale.LC_ALL, '') #for my numbers to be localed 
        localed = locale.format_string('%0.2f', converted, grouping=True) 

        #this is for getting the whole date and changing it into a date supported by python so I culd access individual variables of it
        date_str = sale[0]
        # date_object = datetime.strptime(date_str, '%Y-%m-%d')
        # month = date_object.month
        month = int(date_str[5:7])


        quarter = Quarter(int(month))
        region = inteface.regions.findRegionCode(sale[1])
        newconv = Decimal(converted)
        decimaled = newconv.quantize(Decimal('0.00'))
        print(f"{i}.{'':<6}{sale[0] :<15}{quarter :<15}{region :<15}{locale.currency(decimaled, symbol=True, grouping=True) :>15}")
        totalAmount += float(sale[2])
        locale.setlocale(locale.LC_ALL, '') #for my numners to be localed
    
    print("____________________________________________________________________")
    number = Decimal(totalAmount)
    rounded = number.quantize(Decimal('0.00'))
    print(f"TOTAL:{'' :<52}{locale.currency(rounded, symbol=True, grouping=True)}")
    print()

def Format_Checker(file_import):
    pattern = re.compile(r"^sales_q\d_\d{4}_[a-zA-Z]+\.csv$")
    return pattern.match(file_import)


'''It saves to the textfile but doesn't when there's bad data, and when the user selects exit it clears the text file'''
def Import_Sales(sales):
    file_import = input("Enter file name to import: ")
    files.import_file(file_import,'sales.csv')

    # try:
    split_file = file_import.split('_')#spliting the file bythe underscore

    #declaring the variables on the splitted file
    nuquarter = split_file[1]
    nuyear = split_file[2]
    lastsection = split_file[3]

    #spliting the last section r.csv into extention and region so that I can be able to access the both individually
    lastsection_split = lastsection.split(".")
    nuregion = lastsection_split[0]


    totalAmount = 0
    bad_data = 0


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
            files.Append_TextFile()
            print()
            print(f"{'':<8}{'Date' :<15}{'Quarter' :<15}{'Region' :<15}{'Amount' :>15}")
            print("--------------------------------------------------------------------")
            for i, sale in enumerate (sales, start=1):
                
                date_str = sale[0]
                month = date_str[5:7]

            
                region = inteface.regions.findRegionCode(sale[1]) #region from the interface module
                
                if month == "":
                    month = '?'
                if sale[0] == "":
                    date_str = '?'
                if sale[1] == "":
                    sale[1] = '?'
                if sale[2] == "":
                    sale[2] = '?'

                try:
                    if (nuyear == date_str[:4] and nuquarter == "q"+ str(Quarter(month)) and nuregion == sale[1]):

                        if date_str == '?' or sale[1] == '?' or sale[2] == '?': 
                            if sale[2] != '?':
                                converted = float(sale[2])
                                totalAmount += float(sale[2])
                                locale.setlocale(locale.LC_ALL, '') #for my numbers to be localed
                                localed = locale.format_string('%0.2f', converted, grouping=True)
                                print(f"{i}.*{'':<5}{date_str :<15}{Quarter(month) :<15}{region :<15}{locale.currency(converted, symbol=True, grouping=True) :>15}")
                            else:                                            
                                print(f"{i}.*{'':<5}{date_str :<15}{Quarter(month) :<15}{region :<15}{sale[2] :>15}")

                            Clear_File()
                            bad_data += 1

                        else: #viewsales must only have this else statement in it with the enumerate above
                        
                            #this is for getting the whole date and changing it into a date supported by python so I culd access individual variables of it
                            date_str = sale[0]
                            date_object = datetime.strptime(date_str, '%Y-%m-%d')
                            month = date_object.month

                            converted = float(sale[2])
                            locale.setlocale(locale.LC_ALL, '') #for my numbers to be localed
                            localed = locale.format_string('%0.2f', converted, grouping=True)


                            quarter = Quarter(int(month))
                            
                            print(f"{i}.{'':<6}{sale[0] :<15}{quarter :<15}{region :<15}{locale.currency(converted, symbol=True, grouping=True) :>15}")
                            totalAmount += float(sale[2])
                            locale.setlocale(locale.LC_ALL, '') #for my numners to be localed
                except TypeError:
                    print(f"{i}.*{'':<5}{date_str :<15}{Quarter(month) :<15}{region :<15}{sale[2] :>15}")
                    
            
            print("____________________________________________________________________")
            print(f"TOTAL:{'' :<52}{locale.currency(totalAmount, symbol=True, grouping=True)}")
            print()

            if bad_data > 0:
                print(f"File '{file_import}' contains bad data.\nPlease correct the data in the file and try again.\n")
            break

    # except Exception as e:
    #     print(f"{e}")


'''Function for clearing the textfile'''
def Clear_File():
    with open('imported_files.txt', 'r+') as f:
        f.truncate()       



