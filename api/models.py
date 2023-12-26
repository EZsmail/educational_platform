import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")

class TunelModel(BaseModel):
    class Config:
        
        orm_mode = True
        
    
class ShowUser(TunelModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool 
    
    
class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    
    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value
    
    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, details="Surname should contains only letters"
            )
        return value
    
    