from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from data.database import Base
from models.association import movie_category_association

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    # Quan hệ Many-to-Many
    movies = relationship(
        "Movie", 
        secondary=movie_category_association, 
        back_populates="categories"
    )