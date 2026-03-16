from pydantic import BaseModel


class PosterSchema(BaseModel):
    path: str

    class Config:
        from_attributes = True