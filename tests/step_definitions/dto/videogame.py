from dataclasses import dataclass
from datetime import datetime

@dataclass
class Videogame:
    id: int
    name: str
    release_date: datetime
    review_score: int
    category: str
    rating: str

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            release_date=datetime.strptime(data['releaseDate'], "%Y-%m-%d %H:%M:%S"),
            review_score=data['reviewScore'],
            category=data['category'],
            rating=data['rating']
        )