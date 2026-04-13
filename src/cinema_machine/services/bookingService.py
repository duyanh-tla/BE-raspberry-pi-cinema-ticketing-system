from sqlalchemy.orm import Session
from datetime import date

# Import models
from models.tickets.booking import Booking
from models.tickets.ticket import Ticket
from models.theaters.showtime import Showtime

# Import Schema để sử dụng làm Type Hint (Dòng này sẽ giải quyết lỗi của bạn)
from api.schemas.booking import BookingRequest

def create_booking_service(db: Session, data: BookingRequest):
    # 1. Kiểm tra suất chiếu tồn tại
    showtime = db.query(Showtime).filter(Showtime.id == data.showtime_id).first()
    if not showtime:
        return {"error": "Showtime not found"}

    # 2. Kiểm tra xem có ghế nào đã bị đặt trước đó cho suất chiếu này chưa
    # (Để tránh trường hợp 2 máy Kiosk đặt trùng 1 ghế cùng lúc)
    existing_tickets = (
        db.query(Ticket)
        .join(Booking)
        .filter(
            Booking.showtime_id == data.showtime_id,
            Ticket.seat_id.in_(data.seat_ids)
        )
        .all()
    )
    
    if existing_tickets:
        return {"error": "One or more seats are already booked"}

    # 3. Tính toán giá tổng
    base_price = float(showtime.ticket_type.base_price) if showtime.ticket_type else 0
    total_price = base_price * len(data.seat_ids)

    # 4. Tạo Booking mới
    new_booking = Booking(
        day_create=date.today(),
        showtime_id=data.showtime_id,
        voucher_id=data.voucher_id,
        guest_name=data.guest_name,
        info=data.info,
        total_price=total_price
    )
    
    db.add(new_booking)
    db.flush()  # Lấy ID của booking vừa tạo

    # 5. Tạo các Ticket cho từng ghế
    for seat_id in data.seat_ids:
        new_ticket = Ticket(
            seat_id=seat_id,
            booking_id=new_booking.id
        )
        db.add(new_ticket)

    db.commit()
    db.refresh(new_booking)
    
    return new_booking