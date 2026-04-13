from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from api.schemas.booking import BookingRequest
from services.bookingService import create_booking_service
from api.response import success_response, error_response

router = APIRouter(prefix="/api/v1/bookings", tags=["Bookings"])

@router.post("/")
def post_booking(data: BookingRequest, db: Session = Depends(get_db)):
    try:
        booking = create_booking_service(db, data)
        if isinstance(booking, dict) and "error" in booking:
            return error_response(booking["error"], status_code=400)
            
        return success_response(
            data={"booking_id": booking.id, "total_price": float(booking.total_price)},
            message="BOOKING SUCCESS"
        )
    except Exception as e:
        db.rollback()
        return error_response(str(e), status_code=500)