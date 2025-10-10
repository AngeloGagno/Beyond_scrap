from crawler.beyond import BeyondCrawler
from get.parser.description_parser import DescriptionData
from environment.cookies import load_cookies
from environment.header import load_headers
from database.connection import Config
from database.models import Base
from database.commit_data import send_data

def filtered_data():
    json_accommodation = BeyondCrawler(cookies=load_cookies(), headers=load_headers()).get_endpoint_webpage()
    data = []
    for accommodation in json_accommodation:
        accommodation_desc = DescriptionData(accommodation).parser()
        data.append(accommodation_desc)
    return data

def main(data):
    Base.metadata.create_all(Config().engine)
    send_data(db=Config().get_db(),content=data)
    
if __name__ == '__main__':
    main(filtered_data())