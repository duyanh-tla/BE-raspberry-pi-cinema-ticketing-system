from pydantic import BaseModel


class TicketTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True