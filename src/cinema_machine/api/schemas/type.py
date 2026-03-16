from pydantic import BaseModel


class TicketTypeSchema(BaseModel):
    id: int
    name: str
    base_price: int

    class Config:
        from_attributes = True