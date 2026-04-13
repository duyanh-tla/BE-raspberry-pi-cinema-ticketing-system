from pydantic import BaseModel
from typing import List, Optional

class BookingRequest(BaseModel):
    showtime_id: int
    voucher_id: Optional[int] = None
    guest_name: str
    info: str  # SĐT hoặc Email
    seat_ids: List[int] # Danh sách ID ghế cần đặt