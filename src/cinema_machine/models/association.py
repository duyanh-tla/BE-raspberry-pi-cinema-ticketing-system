from sqlalchemy import Table, Column, Integer, ForeignKey
from data.database import Base

movie_category_association = Table(
    "movie_category",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id"), nullable=False)
)

theater_room_ticket_type_association = Table(
    "theater_room_ticket_type",
    Base.metadata,
    Column("theater_room_id", Integer, ForeignKey("theater_rooms.id"), nullable=False),
    Column("ticket_type_id", Integer, ForeignKey("ticket_types.id"), nullable=False)
)