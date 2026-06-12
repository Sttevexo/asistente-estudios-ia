from pydantic import BaseModel, EmailStr

# Scheme for registering a new user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Scheme to show the user# Scheme to show the user
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

# --- ADD THIS ---
# Scheme for requesting a question to the AI
class AskRequest(BaseModel):
    question: str