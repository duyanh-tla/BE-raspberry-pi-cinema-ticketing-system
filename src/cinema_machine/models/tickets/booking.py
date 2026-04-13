from sqlalchemy import Column, Integer, ForeignKey, String, Date, Numeric
from sqlalchemy.orm import relationship
from data.database import Base
from models.tickets.ticket import Ticket

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    day_create = Column(Date)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    voucher_id = Column(Integer, ForeignKey('vouchers.id'))
    guest_name = Column(String(255))
    info = Column(String(255))
    total_price = Column(Numeric(10, 2))
    
    showtime = relationship("Showtime", back_populates="bookings")
    tickets = relationship("Ticket", back_populates="booking")
    voucher = relationship("Voucher", back_populates="bookings")