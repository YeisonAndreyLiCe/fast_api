from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    id: int = Field(..., gt=0)
    year: int = Field(..., gt=1900, lt=2023)
    category: Optional[str] = None
    director: str
    cast: list

    class Config:
        schema_extra = {
            "example": {
                "title": "The Shawshank Redemption",
                "id": 1,
                "year": 1994,
                "category": "Drama",
                "director": "Frank Darabont",
                "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]
            }
        }

    def to_dict(self):
        return {
            "title": self.title,
            "id": self.id,
            "year": self.year,
            "category": self.category,
            "director": self.director,
            "cast": self.cast
        }