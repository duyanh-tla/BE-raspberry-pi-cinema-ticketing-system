import uvicorn
from core.app import app
from config.serverConfig import HOST, PORT

if __name__ == "__main__":
    uvicorn.run("core.app:app", host=HOST, port=PORT, reload=True)