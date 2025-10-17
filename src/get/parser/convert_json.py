from Beyond_scrap.src.crawler.beyond import Extracter
from Beyond_scrap.src.get.parser.description_parser import DescriptionData
from Beyond_scrap.src.environment.cookies import load_cookies
from Beyond_scrap.src.environment.header import load_headers

def consolidated_json():
    json_accommodation = Extracter(cookie=load_cookies(), header=load_headers()).webpage()

    data = []
    for accommodation in json_accommodation:
        accommodation_desc = DescriptionData(accommodation).parser()
        data.append(accommodation_desc)    
    return data