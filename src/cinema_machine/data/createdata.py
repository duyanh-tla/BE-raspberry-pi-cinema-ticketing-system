from data.database import engine, Base, create_database_if_not_exists
from models.model import import_models
from data.trigger import create_movie_triggers

def create_database():
    create_database_if_not_exists()
    import_models()
    print("Connecting to engine and creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    create_movie_triggers()