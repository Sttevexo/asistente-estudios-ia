from fastapi import FastAPI
from app.database.database import engine, Base
# Importamos todos los routers
from app.routers import users, ask, auth, history

# This creates the tables in the database automatically at startup.
Base.metadata.create_all(bind=engine)

app = FastAPI()

# We registered all the routers so that FastAPI would recognize them.
app.include_router(users.router)
app.include_router(ask.router)
app.include_router(auth.router)
app.include_router(history.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your AI Assistant.."}