from fastapi import FastAPI
from api.routes import movie, showtime, theaterroom, otp, booking
from core.startup import run_startup

app = FastAPI(
    title="Cinema Machine AIoT API",
    description="Hệ thống API cho máy bán vé tự động",
    version="0.0.1"
)

@app.on_event("startup")
def startup_event():
    run_startup()

app.include_router(movie.router)
app.include_router(showtime.router)
app.include_router(theaterroom.router)
app.include_router(otp.router)
app.include_router(booking.router)


@app.get("/")
def root():
    return {"message": "Welcome to Cinema Machine API System"}