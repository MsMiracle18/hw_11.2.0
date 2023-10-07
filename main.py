from fastapi import FastAPI
from . import models, database

app = FastAPI()

# Ініціалізація бази даних
database.init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
