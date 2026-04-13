from datetime import date
from sqlalchemy.orm import Session, joinedload
from models.movies.movie import Movie


def get_movie_by_id_service(db: Session, movie_id: int):

    movie = (
        db.query(Movie)
        .options(
            joinedload(Movie.categories),
            joinedload(Movie.posters),
            joinedload(Movie.trailers),
        )
        .filter(Movie.id == movie_id)
        .first()
    )

    if not movie:
        return None
    
    data = {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "age_rating": movie.age_rating,
        "actors": movie.actors,
        "duration_min": movie.duration_min,
        "status": movie.status,

        "categories": [
            c.name
            for c in movie.categories
        ],

        "posters": [
            {"path": p.path}
            for p in movie.posters
        ],

        "trailers": [
            {"path": t.path}
            for t in movie.trailers
        ],
    }

    return data

def get_showing_movies_service(db: Session):

    today = date.today()

    movies = (
        db.query(Movie)
        .options(
            joinedload(Movie.categories),
            joinedload(Movie.posters),
            joinedload(Movie.trailers),
        )
        .filter(
            Movie.release_date <= today,
            Movie.end_date >= today
        )
        .all()
    )
# Chuyển đổi danh sách object sang danh sách dictionary
    result = []
    for m in movies:
        result.append({
            "id": m.id,
            "title": m.title,
            "categories": [c.name for c in m.categories],
            "description": m.description,
            "age_rating": m.age_rating,
            "actors": m.actors,
            "duration_min": m.duration_min,
            "status": m.status,
            "posters": [{"path": p.path} for p in m.posters],
            "trailers": [{"path": p.path} for p in m.trailers],
        })

    return result