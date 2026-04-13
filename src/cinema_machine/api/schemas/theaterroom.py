from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class SeatResponse(BaseModel):
    id: int
    seat_row: str
    seat_number: int

    class Config:
        from_attributes = True