from datetime import datetime

class DescriptionData:
    def __init__(self,accommodation):
        self.data = accommodation

    def beyond_id(self):
        return self.data['id']
    
    def title(self):
        return self.data['title']
    
    def beyond_status(self):
        return self.data['enabled']

    def princing_cluster(self):
        return self.data['cluster']
    
    def avantio_id(self):
        return self.data['managed_accounts'][0]['channel_id']
    
    def last_base_price_update(self):
        return self.data['base_price_updated_at']
    
    def actual_base_price(self):
        return self.data['base_price']   
    
    def last_min_price_update(self):
        return self.data['min_price_updated_at']

    def actual_min_price(self):
        return self.data['min_price']
    
    def booked_in_seven_days(self):
        return self.data['booked_seven']

    def booked_in_fourteen_days(self):
        return self.data['booked_fourteen']
    
    def booked_in_thirty_days(self):
        return self.data['booked_thirty']

    def booked_in_sixty_days(self):
        return self.data['booked_sixty']
    
    def booked_in_ninety_days(self):
        return self.data['booked_ninety']
    

    def parser(self):
        json = {
            'beyond_id':str(self.beyond_id()),
            'beyond_status':self.beyond_status(),
            'cluster':self.princing_cluster(),
            'accommodation_id':self.avantio_id(),
            'last_base_price_update':self.last_base_price_update(),
            'last_min_price_update':self.last_min_price_update(),
            'base_price':self.actual_base_price(),
            'min_price':self.actual_min_price(),
            'booked_7_days':self.booked_in_seven_days(),
            'booked_14_days':self.booked_in_fourteen_days(),
            'booked_30_days':self.booked_in_thirty_days(),
            'booked_60_days':self.booked_in_sixty_days(),
            'booked_90_days':self.booked_in_ninety_days(),
            'scrap_date':datetime.now()
        }
        return json