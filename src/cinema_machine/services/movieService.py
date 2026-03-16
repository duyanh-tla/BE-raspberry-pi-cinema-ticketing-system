from sqlalchemy.orm import Session
from models.movies.movie import Movie
from api.schemas.movie import MovieDetailResponse


def get_movies_service(db: Session):
    movies = db.query(Movie).all()
    return [MovieDetailResponse.model_validate(m).model_dump() for m in movies]


def get_movie_by_id_service(db: Session, movie_id: int):

    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        return None

    # categories
    categories = [
        {
            "id": c.id,
            "name": c.name
        }
        for c in movie.categories
    ]

    # trailers
    trailers = [
        {
            "path": t.path
        }
        for t in movie.trailers
    ]

    # posters
    posters = [
        {
            "path": p.path
        }
        for p in movie.posters
    ]

    # showtimes
    showtimes = []

    # ticket types (unique)
    ticket_types_dict = {}

    for s in movie.showtimes:

        showtimes.append({
            "dayshow": s.dayshow.isoformat(),
            "start_time": s.time_slot.start_time
        })

        if s.ticket_type:
            ticket_types_dict[s.ticket_type.id] = {
                "id": s.ticket_type.id,
                "name": s.ticket_type.name,
                "base_price": s.ticket_type.base_price
            }

    ticket_types = list(ticket_types_dict.values())

    data = {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "age_rating": movie.age_rating,
        "duration_min": movie.duration_min,
        "status": movie.status,

        "categories": categories,
        "ticket_types": ticket_types,
        "trailers": trailers,
        "posters": posters,
        "showtimes": showtimes
    }

    return data