In the .env file, adjust DB_PASSWORD and DB_PORT (if necessary), then
run code 
python .\src\cinema_machine\main.py

database:
go to time_slots on mySQL and turn off Auto Incresae on id

create random showtime 
python .\src\cinema_machine\data\generate_showtime.py

then run sql in 
src/cinema_machine/resource/sql/showtimes.sql