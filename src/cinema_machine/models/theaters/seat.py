from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from data.database import Base

class Seat(Base):
    __tablename__ = 'seats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    theater_room_id = Column(Integer, ForeignKey('theater_rooms.id'), nullable=False)
    row = Column(String(100), nullable=False)
    number = Column(int, nullable = False)
    
    theater_room = relationship("TheaterRoom", back_populates="seats")