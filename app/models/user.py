from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Esto permite hacer: usuario.conversas
    conversas = relationship("Conversa", back_populates="owner")

class Conversa(Base):
    __tablename__ = "conversas"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pergunta = Column(String, nullable=False)
    resposta = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # This allows you to do: conversa.owner
    owner = relationship("User", back_populates="conversas")