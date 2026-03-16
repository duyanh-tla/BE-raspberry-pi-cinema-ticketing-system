from data.createdata import create_database
from config.serverConfig import HOST, PORT

def run_startup():
    print("Initializing database...")
    create_database()
    print(f"Uvicorn running on http://{HOST}:{PORT} (Press CTRL+C to quit)")