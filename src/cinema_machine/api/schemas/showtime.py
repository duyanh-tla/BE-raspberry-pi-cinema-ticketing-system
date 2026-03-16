from pydantic import BaseModel
from datetime import date

class ShowtimeSchema(BaseModel):
    dayshow: date
    start_time: str

    class Config:
        from_attributes = True