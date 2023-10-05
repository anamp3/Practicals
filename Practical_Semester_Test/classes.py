class Region:
    def __init__(self, code, name) -> None:
        self.code = code
        self.name = name


class Regions:
    def __init__(self):
        self.regional_list = []

    def findRegionCode(self, code):
        for region in self.regional_list:
            if region.code == code:
                return region
        return print("Region was not found.")
    
    @property #become re-usable along the code
    def validRegionCodes(self):
        regionCodes = [region.code for region in self.regional_list]
        return regionCodes
    
    # this will add to the regonal list a region object
    def createRegion(self, region):
        self.regional_list.append(region)

    def __str__(self):
        output = "| ".join(self.validRegionCodes)
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
            return ("The filename you entered is invalid.")
        

    def filenameValidity(self):
        rcode = self.codeFromFileName()
        if rcode and rcode in self.region.validRegionCodes:#the regioncodes from the regions class
            return print("The file name you entered is valid.")
        else:
            return print("The file name you entered is not valid.")


    @property
    def namingConvention(self):
        return self.name_conv #this will return an expected naming convention which will be 'sales_qn_yyy_r.csv' in this case.


'''This is the daily sales class'''
class DailySales:
    def __init__(self, amount, date, region, quarter) -> None:
        self.amount = amount
        self.date = date
        self.region = region
        self.quarter = quarter