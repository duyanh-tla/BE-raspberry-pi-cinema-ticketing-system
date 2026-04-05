from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from data.database import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    showtime_id = Column(Integer, ForeignKey('showtimes.id'), nullable=False)
    seat_id = Column(Integer, ForeignKey('seats.id'), nullable=False)
    status = Column(String(100), nullable=True)
    