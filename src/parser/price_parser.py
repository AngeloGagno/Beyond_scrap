from datetime import datetime
import uuid

class PriceData:
    def __init__(self,accommodation):
        self.data = accommodation

    def uuid_generator(self):
        return str(uuid.uuid4())
    
    def beyond_id(self):
        return self.data['id']

    def scrap_date(self):
        return datetime.now().strftime(r'%Y-%m-%d')

class BasePriceData(PriceData):
    def __init__(self, accommodation):
        super().__init__(accommodation)

    def price_updated_at(self):
        return self.data['base_price_updated_at']

    def base_price_historical_data(self):
        historical_data = self.data['base_price_history']
        for data in historical_data:
           return {'beyond_id':self.beyond_id(),
                   'operation_id':self.uuid_generator(),
                 'price_date_stamp': data['stamp'],
                 'value':data['value'],
                 'scrap_date':self.scrap_date()
                 }
    
class MinimumPriceData(PriceData):
    def __init__(self, accommodation):
        super().__init__(accommodation)

    def minimum_price_historical_data(self):
        historical_data = self.data['min_price_history']
        
        for data in historical_data:     
            return  {'beyond_id':self.beyond_id(),
                     'operation_id':self.uuid_generator(),
                 'price_date_stamp': data['stamp'],
                 'value':data['value'],
                 'scrap_date':self.scrap_date()
                 }
        