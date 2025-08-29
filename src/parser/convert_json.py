from crawler.beyond import Extracter
from parser.price_parser import MinimumPriceData,BasePriceData
from parser.description_parser import DescriptionData
from environment.cookies import load_cookies
from environment.header import load_headers

def consolidated_json():
    json_accommodation = Extracter(cookie=load_cookies(), header=load_headers()).webpage()

    data = []
    for accommodation in json_accommodation:
        accommodation_desc = DescriptionData(accommodation).parser()
        data.append(accommodation_desc)    
    return data