from datetime import date, datetime
from sqlalchemy.orm import Session, joinedload, contains_eager
from models.movies.movie import Movie
from models.theaters.showtime import Showtime
from models.theaters.timeslot import TimeSlot


def get_movie_by_id_service(db: Session, movie_id: int):

    movie = (
        db.query(Movie)
        .options(
            joinedload(Movie.showtimes).joinedload(Showtime.time_slot),
            joinedload(Movie.showtimes).joinedload(Showtime.ticket_type),
            joinedload(Movie.categories),
            joinedload(Movie.posters),
            joinedload(Movie.trailers),
        )
        .filter(Movie.id == movie_id)
        .first()
    )

    if not movie:
        return None

    now = datetime.now()
    showtimes = []
    for s in movie.showtimes:

        try:
            show_time = datetime.strptime(s.time_slot.start_time, "%H:%M").time()
        except Exception:
            continue

        show_datetime = datetime.combine(s.dayshow, show_time)

        if show_datetime < now:
            continue

        showtimes.append({
            "dayshow": s.dayshow,
            "start_time": s.time_slot.start_time
        })

    data = {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "age_rating": movie.age_rating,
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

        "showtimes": showtimes,

        "ticket_types": list({
            s.ticket_type.id: {
                "id": s.ticket_type.id,
                "name": s.ticket_type.name,
                "base_price": s.ticket_type.base_price
            }
            for s in movie.showtimes
            if s.ticket_type
        }.values())
    }

    return data

def get_showing_movies_service(db: Session):

    today = date.today()

    movies = (
        db.query(Movie)
        .options(joinedload(Movie.posters))
        .filter(
            Movie.release_date <= today,
            Movie.end_date >= today
        )
        .all()
    )

    return movies