from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. SQLite URL Definition
DATABASE_URL = "sqlite:///./estudos_ia.db"

# 2. Engine creation (engine)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3. Session configuration and base class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 4. Session generator function for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()