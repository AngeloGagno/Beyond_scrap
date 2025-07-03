from requests import HTTPError 
import requests

class Extracter:
    def __init__(self,cookie,header):
        self.cookie = cookie
        self.header = header
    
    def status_page(self):
        status_code = requests.get('https://api.beyondpricing.com/api/pricing/listings',cookies=self.cookie,headers=self.header).status_code
        return status_code
    
    def webpage(self):
        if self.status_page() == 200:
            return requests.get('https://api.beyondpricing.com/api/pricing/listings',cookies=self.cookie,headers=self.header).json()
        else: 
            raise HTTPError(f'Status: {self.status_page()}')