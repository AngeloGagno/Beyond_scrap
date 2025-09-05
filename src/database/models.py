from sqlalchemy import String,Column,Date,Boolean,Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class DescriptionData(Base):
    __tablename__ = 'beyond_detailed_data'
    beyond_id = Column(String,primary_key=True,index=True)
    beyond_status = Column(Boolean)
    accommodation_id = Column(String,index=True)
    price_cluster = Column(String)
    base_price = Column(String)
    minimum_price = Column(String)
    last_booking_date = Column(Date)
    furthest_checkin_date = Column(Date)

class BookingUpdate(Base):
    __tablename__ = 'beyond_booking_update'
    beyond_id = Column(String,primary_key=True,index=True)
    scrap_date = Column(Date,primary_key=True,index=True)
    booked_7_days = Column(Integer)
    booked_14_days = Column(Integer)
    booked_30_days = Column(Integer)
    booked_60_days = Column(Integer)
    booked_90_days = Column(Integer)
    last_base_price_update = Column(String)
    last_minimum_price_update = Column(String)

class BasePriceHistorical(Base):
    __tablename__ = 'beyond_base_historical_data'
    transaction_id = Column(String(100), primary_key=True)
    beyond_id = Column(String(50),primary_key=True,index=True)
    price_date_stamp = Column(Date)
    value = Column(String(20))
    scrap_date = Column(Date)

class BaseMinHistorical(Base):
    __tablename__ = 'beyond_minimum_historical_data'
    transaction_id = Column(String(100), primary_key=True)
    beyond_id = Column(String(50),primary_key=True,index=True)
    price_date_stamp = Column(Date)
    value = Column(String(20))
    scrap_date = Column(Date)