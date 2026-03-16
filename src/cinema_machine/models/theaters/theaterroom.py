from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base
from models.association import theater_room_ticket_type_association
    
class TheaterRoom(Base):
    __tablename__ = 'theater_rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False) # ten_phong_chieu
    seat_capacity = Column(Integer, nullable=False) # so_luong_ghe

    # Quan hệ với Showtimes (One-to-Many)
    showtimes = relationship(
        "Showtime", 
        back_populates="theater_room"
    )
    
    # Quan hệ với TicketType (Many-to-Many)
    ticket_type = relationship(
        "TicketType",
        secondary=theater_room_ticket_type_association,
        back_populates="theater_rooms"
    )