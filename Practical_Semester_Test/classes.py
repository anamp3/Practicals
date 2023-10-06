from dataclasses import dataclass
from datetime import datetime
import re#this is for the date formating

DATE_FORMAT = '%Y-%m-%d'

@dataclass
class Region:
    code:str
    name:str


class Regions:
    def __init__(self):
        self.regional_list = []

    def findRegionCode(self, code):
        for i, region in enumerate(self.regional_list):
            if code in region:
                name = self.regional_list[i][1]
                return name
        return '?'
    
    #become re-usable along the code
    def validRegionCodes(self):
        regionCodes = []
        for region in self.regional_list:
            regionCodes.append(region)
        return regionCodes
    
    # this will add to the regonal list a region object
    def createRegion(self, code, region):
        self.regional_list.append([code, region])

    def __str__(self):
        output = "| ".join(self.validRegionCodes())
        return output




'''This is the file class'''
class File:
    def __init__(self, fileName, region, name_conv) -> None:
        self.fileName = fileName
        self.region = region
        self.name_conv = name_conv

    #this means that creating objects will be done on the main functions, create a new module for avoiding confusion and 
    #be sure to make use of the code on my sales.py module
    def codeFromFileName(self):
        split_file = self.fileName.split('_')
        if split_file == 4:
            lastsection = split_file[3]
            lastsection_split = lastsection.split(".")
            region = lastsection_split[0] #this is accessing my region
            return region
        else:
            return None
        

    def filenameValidity(self):
        rcode = self.codeFromFileName()
        if rcode and rcode in self.region.validRegionCodes:#the regioncodes from the regions class
            return True
        else:
            return False


    @property
    def namingConvention(self):
        pattern = re.compile(r"^sales_q\d_\d{4}_[a-zA-Z]+\.csv$")
        if pattern.match(self.fileName):
            print(f"{self.fileName} is valid.")
        else:
            print(f"{self.fileName} is not valid.")

        return self.name_conv #this will return an expected naming convention which will be 'sales_qn_yyy_r.csv' in this case.


'''This is the daily sales class'''
class DailySales:
    def __init__(self, date, region, amount, quarter=0) -> None:
        self.date = date
        self.region = region
        self.quarter = quarter

        if self.quarter == 0:
            self.quarter = self.Quarter(date)

        self.amount = amount
        

    def Quarter(self, date):
        if date == '?':
            quarter = 0
        else:
            quarter = (int(date.month) - 1) // 3 + 1
            
        return quarter
    
    def checkValidity(self):
        if (isinstance(self.amount, float) and isinstance(self.date, str) and 
            isinstance(self.region, str) and self.quarter >= 1 and self.quarter <= 4):

            return True
        else:
            return False

    @staticmethod
    def convRowofFile(row):
        portion = row.split(",")

        date = datetime.strptime(portion[0], DATE_FORMAT)
        region = portion[1]
        amount = portion[2]

        return DailySales(date, region, amount)
    
    def toAList(self):
        list_to_CSV = [self.date, self.region, self.amount, self.quarter]
        return list_to_CSV
    

'''This is the sales list class'''
class SalesList:
    def __init__(self) -> None:
        self.daily_sales = []
        self.bad_data = False

    def createSales(self, sale):
        if sale[0] == "":
            sale[0] = '?'
        if sale[1] == "":
            sale[1] = '?'
        if sale[2] == "":
            sale[2] = '?'
        
        if sale[0] == '?' and sale[1] == '?' and sale[2] == '?':
            self.bad_data = True

        self.daily_sales.append(sale)

    def retrieveSalesbyIndex(self, index):

        if 0 <= index < len(self.daily_sales):
            return self.daily_sales[index]
        else:
            return None
        
    def createSalesList(self, another_sales_list):
        for sale in another_sales_list.daily_sales:
            self.createSales(sale)

    def __len__(self):
        count = len(self.daily_sales)
        return count
    
    def __iter__(self):
        iteration = iter(self.daily_sales)
        return iteration
    

class FileImportError(OSError):
    def __init__(self, issue) -> None:
        super().__init__(issue)
