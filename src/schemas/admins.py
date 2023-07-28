from pydantic import BaseModel
from typing import Optional


class AdminSchema(BaseModel):
    id: int
    login: str
    password: str
    permission: int
    school_id: Optional[int]
    
    class Config:
        from_attributes = True


class AdminAuthSchema(BaseModel):
    login: str
    password: str
    
    class Config:
        from_attributes = True


class AdminOutSchema(BaseModel):
    id: int
    login: str
    hashed_password: str
    permission: int
    school_id: Optional[int] = None
    
    class Config:
        from_attributes = True


class AdminRegisterSchema(BaseModel):
    login: str
    password: str
    permission: int
    school_id: Optional[int]
    
    class Config:
        from_attributes = True

    
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        from_attributes = True


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None

    class Config:
        from_attributes = True