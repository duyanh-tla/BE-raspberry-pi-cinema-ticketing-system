from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from api.schemas.category import CategorySchema
from api.schemas.type import TicketTypeSchema
from api.schemas.trailer import TrailerSchema
from api.schemas.poster import PosterSchema
from api.schemas.showtime import ShowtimeSchema


class MovieDetailResponse(BaseModel):

    id: int
    title: str
    description: Optional[str]
    age_rating: Optional[str]
    duration_min: int
    status: str

    categories: List[CategorySchema] = []

    ticket_types: List[TicketTypeSchema] = []

    trailers: List[TrailerSchema] = []

    posters: List[PosterSchema] = []

    showtimes: List[ShowtimeSchema] = []
    
    class Config:
        from_attributes = True
        
        
        






# Schema dùng chung
class MovieBase(BaseModel):
    title: str
    age_rating: Optional[str]
    duration_min: int
    description: Optional[str] = None
    release_date: date
    end_date: date

# Schema cho POST (Create)
class MovieCreate(MovieBase):
    pass

# Schema cho PUT (Update) có thể cho phép update một phần
class MovieUpdate(BaseModel):
    title: Optional[str] = None
    age_rating: Optional[str] = None
    duration_min: Optional[int] = None
    description: Optional[str] = None
    release_date: Optional[date] = None
    end_date: Optional[date] = None

# # Schema cho Response (chứa id và status từ property)
# class MovieResponse(MovieBase):
#     id: int
#     status: str

#     class Config:
#         from_attributes = True
