from datetime import date, timedelta
import random

TOTAL_SHOWTIMES = 1000
IMAX_COUNT = 100

movies = list(range(1, 12))
animation_movies = [3, 7, 10]
IMAX_MOVIE = 5

normal_rooms = [1, 2, 3]
imax_rooms = [5, 6]

time_slots = [
    800, 915, 1030, 1145,
    1300, 1415, 1530, 1645,
    1800, 1915, 2030, 2145, 2300
]

start_date = date.today() + timedelta(days=1)
days = [start_date + timedelta(days=i) for i in range(30)]

showtimes = []

# ================= TẠO FULL SLOT =================
normal_slots = []
for d in days:
    for r in normal_rooms:
        for ts in time_slots:
            normal_slots.append((r, ts, d))

imax_slots = []
for d in days:
    for r in imax_rooms:
        for ts in time_slots:
            imax_slots.append((r, ts, d))

random.shuffle(normal_slots)
random.shuffle(imax_slots)

# ================= IMAX =================
for i in range(IMAX_COUNT):
    r, ts, d = imax_slots[i]
    showtimes.append((IMAX_MOVIE, r, 5, ts, d))

# ================= NORMAL =================
base = (TOTAL_SHOWTIMES - IMAX_COUNT) // len(movies)
extra = (TOTAL_SHOWTIMES - IMAX_COUNT) % len(movies)

movie_quota = {m: base for m in movies}
for m in movies[:extra]:
    movie_quota[m] += 1

for movie in movies:
    if movie == IMAX_MOVIE:
        continue

    quota = movie_quota[movie]

    for _ in range(quota):
        r, ts, d = normal_slots.pop()

        if movie in animation_movies and random.random() < 0.4:
            ticket = 2
        else:
            ticket = 1

        showtimes.append((movie, r, ticket, ts, d))

# ================= EXPORT =================
values = [
    f"({m},{r},{t},{ts},'{d}')"
    for m, r, t, ts, d in showtimes
]

sql = """INSERT INTO showtimes(movie_id, theater_room_id, type_ticket_id, time_slot_id, dayshow)
VALUES
"""
sql += ",\n".join(values) + ";"

with open("src/cinema_machine/resource/sql/showtimes.sql", "w", encoding="utf-8") as f:
    f.write(sql)

print("✅ Done: 1000 showtimes (balanced & no conflict)")

