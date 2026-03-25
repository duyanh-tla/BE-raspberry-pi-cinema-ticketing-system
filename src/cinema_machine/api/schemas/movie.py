from pydantic import BaseModel, Field
from typing import Optional, List
from api.schemas.category import CategorySchema
from api.schemas.type import TicketTypeSchema
from api.schemas.trailer import TrailerSchema
from api.schemas.poster import PosterSchema
from api.schemas.showtime import ShowtimeSchema


# Schema dùng chung
class MovieBase(BaseModel):
    id: int
    title: str
    age_rating: Optional[str]
    posters: List[PosterSchema] = Field(default_factory=list)
    
    class Config:
        from_attributes = True


class MovieDetailResponse(BaseModel):

    id: int
    title: str
    description: Optional[str]
    age_rating: Optional[str]
    duration_min: int
    status: str

    categories: List[str] = Field(default_factory=list)

    ticket_types: List[TicketTypeSchema] = Field(default_factory=list)

    posters: List[PosterSchema] = Field(default_factory=list)
    
    trailers: List[TrailerSchema] = Field(default_factory=list)

    showtimes: List[ShowtimeSchema] = Field(default_factory=list)
    
    class Config:
        from_attributes = True
    