from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User
from app.schemas.schemas import UserCreate, UserResponse
from passlib.context import CryptContext

router = APIRouter(tags=["Usuarios"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Verify if the email already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="The email is already registered")
    
    # 2. Hash the password before saving it
    hashed_password = pwd_context.hash(user.password)
    
    # 3. Create the new user
    new_user = User(name=user.name, email=user.email, password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user