import pandas as pd
from database.connection import Config

def table_reader(query):
    con = Config().engine_creator() 
    return pd.read_sql(query,con)

if __name__ == '__main__':
    print(table_reader('SELECT name,beyond_id, discount_30_days FROM marts.beyond_sales').head())