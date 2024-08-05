from google_sheet import *
from amazon import *



class Robots:
    pass



if __name__ == "__main__":
    links_from_google_sheet = GoogleSheetsClient().get_amazon_links()
    AmazonSeleniumRobot().check_product_availablility_for(links_from_google_sheet)



     