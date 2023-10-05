class Region:
    def __init__(self, code, name) -> None:
        self.code = code
        self.name = name


class Regions:
    def __init__(self):
        self.regional_list = []

    def regionCode(self, code):
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

class File:
    def __init__(self, fileName, region, name_conv) -> None:
        self.fileName = fileName
        self.region = region
        self.name_conv = name_conv

    

        