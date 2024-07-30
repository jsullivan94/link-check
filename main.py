from google_sheet import *

class GoogleSheetsClient: 
    def __init__(self):
        self.creds = check_creds()
        self.links = get_links(self.creds)
        self.checked_list = []

class Amazon:
    pass

if __name__ == "__main__":
    client = GoogleSheetsClient()
    print("Links:", client.links)
    print("Checked List:", client.checked_list)