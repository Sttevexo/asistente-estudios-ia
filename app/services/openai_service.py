import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Carga de variables de entorno
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    logging.warning("OPENAI_API_KEY no definida. Configura tu .env")

client = OpenAI(api_key=OPENAI_API_KEY)

# This is the ONLY version you need to manage history
def gerar_resposta_ia(historico: list, nova_pergunta: str) -> str:
    try:
        # We define the role of the system
        system_prompt = {"role": "system", "content": "Você é um assistente de estudos útil."}
        
        # We combine everything: System Prompt + Past History + New Question
        mensagens = [system_prompt] + historico + [{"role": "user", "content": nova_pergunta}]
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.exception("Erro ao chamar OpenAI")
        return f"Erro na IA: {str(e)}"