from pydantic import BaseModel

class TrailerSchema(BaseModel):
    path: str

    class Config:
        from_attributes = True