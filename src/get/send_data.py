from Beyond_scrap.src.crawler.beyond import BeyondCrawler
from Beyond_scrap.src.get.parser.description_parser import DescriptionData

def filtered_data(cookies,headers):
    json_accommodation = BeyondCrawler(cookies=cookies, headers=headers).get_endpoint_webpage()
    data = []
    for accommodation in json_accommodation:
        accommodation_desc = DescriptionData(accommodation).parser()
        data.append(accommodation_desc)
    return data