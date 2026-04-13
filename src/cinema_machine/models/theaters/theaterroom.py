from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base
from models.association import theater_room_ticket_type_association
    
class TheaterRoom(Base):
    __tablename__ = 'theater_rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False) # ten_phong_chieu
    seat_capacity = Column(Integer, nullable=False) # so_luong_ghe

    showtimes = relationship("Showtime", back_populates="theater_room")
    seats = relationship("Seat", back_populates="theater_room")
    ticket_types = relationship("TicketType",
        secondary=theater_room_ticket_type_association,
        back_populates="theater_rooms"
    )