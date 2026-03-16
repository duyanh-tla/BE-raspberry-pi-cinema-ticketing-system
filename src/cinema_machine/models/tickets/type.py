from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from data.database import Base
from models.association import theater_room_ticket_type_association

class TicketType(Base):
    __tablename__ = 'ticket_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    base_price = Column(Integer, nullable=False)
    description = Column(Text)
    

    theater_rooms = relationship(
        "TheaterRoom",
        secondary=theater_room_ticket_type_association,
        back_populates="ticket_type"
    )
    
    showtimes = relationship("Showtime", back_populates="ticket_type")
    