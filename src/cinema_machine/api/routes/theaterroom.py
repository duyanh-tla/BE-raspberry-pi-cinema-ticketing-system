from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.response import success_response, error_response
from api.deps import get_db
from api.schemas.theaterroom import SeatResponse
from services.theaterroomService import get_threater_room_seats

router = APIRouter(prefix="/api/v1/theaterrooms", tags=["TheaterRooms"])

@router.get("/{theater_room_id}")
def get_seats(theater_room_id: int, db: Session = Depends(get_db)):
    seats = get_threater_room_seats(db, theater_room_id)
    if not seats:
        return success_response(
            data=[], 
            message="NO SEAT IN THIS ROOM"
        )
    data = [
        SeatResponse.model_validate(s).model_dump(mode="json")
        for s in seats
    ]
    return success_response(
        data=data,
        message="GET SEATS SUCCESS"
    )