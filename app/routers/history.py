from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import Conversa
from app.routers.auth import get_current_user  # Usamos el usuario autenticado

router = APIRouter(tags=["Historial"])

@router.get("/history")
def get_user_history(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Filter only conversations belonging to the logged-in user
    history = db.query(Conversa).filter(Conversa.user_id == current_user.id).all()
    return history