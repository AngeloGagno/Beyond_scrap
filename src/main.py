from crawler.beyond import Extracter
from parser.price_parser import MinimumPriceData,BasePriceData
from parser.description_parser import DescriptionData
from environment.cookies import load_cookies
from environment.header import load_headers

def main():
    json_accommodation = Extracter(cookie=load_cookies(), header=load_headers()).webpage()
    data_min_price = []
    data_base_price = []
    data = []
    for accommodation in json_accommodation:
        accommodation_desc = DescriptionData(accommodation).parser()
        parsed_minimum = MinimumPriceData(accommodation).minimum_price_historical_data()
        parsed_base = BasePriceData(accommodation).base_price_historical_data()
        accommodation_desc = DescriptionData(accommodation).parser()
        data.append(accommodation_desc)
        if parsed_minimum:
            data_min_price.append(parsed_minimum)
        if parsed_base:
            data_base_price.append(parsed_base)

    return data,data_min_price,data_base_price
if __name__ == '__main__':
    data,data_min_price,data_base_price = main()
    print(data_base_price)