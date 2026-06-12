from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import Conversa
from app.schemas.schemas import AskRequest
from app.services.openai_service import gerar_resposta_ia

router = APIRouter(tags=["Assistente de IA"])

@router.post("/ask")
def ask_ai(payload_req: AskRequest, db: Session = Depends(get_db)):
    # 1. For now, we're passing an empty list as historical data.
    # (In the future, we will search for previous records in the database here.)
    historico = [] 
    
    # 2. We call the function with the two required arguments
    resposta_ia = gerar_resposta_ia(historico, payload_req.question)
    
    user_id = 1 
    nova_conversa = Conversa(
        user_id=user_id,
        pergunta=payload_req.question,
        resposta=resposta_ia
    )
    
    db.add(nova_conversa)
    db.commit()
    db.refresh(nova_conversa)

    return {
        "pergunta": nova_conversa.pergunta,
        "resposta": nova_conversa.resposta,
        "created_at": nova_conversa.created_at
    }