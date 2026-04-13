from datetime import datetime, date
from sqlalchemy.orm import Session, joinedload
from models.theaters.showtime import Showtime
from models.theaters.theaterroom import TheaterRoom
from models.tickets.booking import Booking

from models.tickets.ticket import Ticket
from models.theaters.seat import Seat

def get_today_showtimes_with_booked_seats(db: Session, movie_id: int):
    now = datetime.now()
    today = date.today()

    showtimes = (
        db.query(Showtime)
        .options(
            joinedload(Showtime.time_slot),
            joinedload(Showtime.theater_room),
            joinedload(Showtime.ticket_type)
        )
        .filter(
            Showtime.movie_id == movie_id,
            Showtime.dayshow == today
        )
        .all()
    )

    result = []

    for s in showtimes:
        try:
            start_time_obj = datetime.strptime(s.time_slot.start_time, "%H:%M").time()
            show_datetime = datetime.combine(s.dayshow, start_time_obj)
        except Exception:
            continue

        if show_datetime > now:
            # Lấy danh sách ghế đã đặt (giữ nguyên logic join Seat-Ticket-Booking)
            booked_seats = (
                db.query(Seat)
                .join(Ticket, Ticket.seat_id == Seat.id)
                .join(Booking, Ticket.booking_id == Booking.id)
                .filter(Booking.showtime_id == s.id)
                .all()
            )

            # Gán trực tiếp ticket_type
            ticket_data = None
            if s.ticket_type:
                ticket_data = {
                    "id": s.ticket_type.id,
                    "name": s.ticket_type.name,
                    "base_price": s.ticket_type.base_price
                }

            result.append({
                "id": s.id,
                "start_time": s.time_slot.start_time,
                "theater_room_id": s.theater_room.id,
                "theater_room_name": s.theater_room.name,
                "ticket_type": ticket_data, # Dữ liệu đơn lẻ
                "booked_seats": [
                    {
                        "id": seat.id,
                        "seat_row": seat.seat_row,
                        "seat_number": seat.seat_number
                    } for seat in booked_seats
                ]
            })

    return result