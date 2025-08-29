from database.models import DescriptionData,BookingUpdate
from sqlalchemy.orm import Session

def send_data(db:Session,content):
    update_list = []
    for item in content:
        accommodations_data = DescriptionData(
            beyond_id = item['beyond_id'],
            beyond_status = item['beyond_status'],
            accommodation_id = item['accommodation_id'],
            price_cluster = item['cluster'],
            base_price = item['base_price'],
            minimum_price= item['min_price'],
            last_booking_date   = item['last_booking_date'],
            furthest_checkin_date = item['furthest_checkin_date'])
        
        booking_update = BookingUpdate(
            beyond_id = item['beyond_id'],
            scrap_date = item['scrap_date'],
            booked_7_days = item['booked_7_days'],
            booked_14_days = item['booked_14_days'],
            booked_30_days = item['booked_30_days'],
            booked_60_days = item['booked_60_days'],
            booked_90_days = item['booked_90_days'],
            last_base_price_update = item['last_base_price_update'],
            last_minimum_price_update = item['last_min_price_update']
        )
        update_list.append(booking_update)
        db.merge(accommodations_data)
    db.add_all(update_list)
    db.commit()
    