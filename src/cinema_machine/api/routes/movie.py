from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schemas.movie import MovieCreate, MovieUpdate
from api.response import success_response, error_response
from api.deps import get_db

from services.movieService import (
    get_movie_by_id_service,
)

router = APIRouter(prefix="/api/v1/movies", tags=["Movies"])

# @router.post("/")
# def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
#     try:
#         data = create_movie_service(db, movie)
#         return success_response(data=data, message="CREATE MOVIE SUCCESS", status_code=201)
#     except Exception as e:
#         return error_response(error_detail=str(e))


# @router.get("/")
# def get_movies(db: Session = Depends(get_db)):
#     data = get_movies_service(db)
#     return success_response(data=data, message="GET MOVIES SUCCESS")


@router.get("/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    data = get_movie_by_id_service(db, movie_id)
    if not data:
        return error_response("Movie not found", status_code=404)
    return success_response(data=data)


# @router.put("/{movie_id}")
# def update_movie(movie_id: int, movie_update: MovieUpdate, db: Session = Depends(get_db)):
#     data = update_movie_service(db, movie_id, movie_update)
#     if not data:
#         return error_response("Movie not found", status_code=404)
#     return success_response(data=data, message="UPDATE MOVIE SUCCESS")