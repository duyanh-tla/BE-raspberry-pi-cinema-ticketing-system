def import_models():
    from models.movies.movie import Movie
    from models.movies.category import Category
    from models.movies.trailer import Trailer
    from models.movies.poster import Poster
    from models.theaters.showtime import Showtime
    from models.theaters.seat import Seat
    from models.theaters.theaterroom import TheaterRoom
    from models.theaters.timeslot import TimeSlot
    from models.others.voucher import Voucher
    from models.tickets.booking import Booking
    from models.tickets.type import TicketType
    from models.tickets.ticket import Ticket