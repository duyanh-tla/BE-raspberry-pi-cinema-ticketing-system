from sqlalchemy.orm import Session, joinedload
from models.theaters.seat import Seat

def get_threater_room_seats(db: Session, theater_room_id: int):

    seats = (
        db.query(Seat)
        .filter(
            Seat.theater_room_id == theater_room_id,
        )
        .all()
    )

    result = []

    for s in seats:
    
            result.append({
                "id": s.id,
                "seat_row": s.seat_row,
                "seat_number": s.seat_number,
            })

    return result