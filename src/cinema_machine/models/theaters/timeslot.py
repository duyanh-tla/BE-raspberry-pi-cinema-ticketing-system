from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data.database import Base
    
class TimeSlot(Base):
    __tablename__ = 'time_slots'
    id = Column(Integer, primary_key=True, autoincrement=False)
    start_time = Column(String(5), nullable=False) # gio_bat_dau
    
    showtimes = relationship("Showtime", back_populates="time_slot")