from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from data.database import Base

class Poster(Base):
    __tablename__ = 'posters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    path = Column(Text, nullable=False) # duong_dan_anh
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)

    # Quan hệ với Movie
    movie = relationship("Movie", back_populates="posters")