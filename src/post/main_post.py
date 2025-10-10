from crawler.beyond import BeyondPost
from environment.cookies import load_cookies
from environment.header import load_headers
from datetime import datetime, timedelta
from utils import table_reader

def pipeline():
    header = load_headers()
    cookies = load_cookies()
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    data = table_reader('SELECT name,beyond_id, discount_30_days FROM marts.beyond_sales')
    accommodation_discounts = []
    for row in data.itertuples(index=False):
        BeyondPost(cookies=cookies,
                   headers=header,
                   start_date=start_date,
                   end_date=end_date,
                   accommodation_id=row.beyond_id, 
                   percentual=(row.discount_30_days)*100).post_beyond_pipeline()
        accommodation_discounts.append({'beyond_id':row.beyond_id, 'discount_30_days':row.discount_30_days,'timestamp_changes': start_date})
    return accommodation_discounts

pipeline()