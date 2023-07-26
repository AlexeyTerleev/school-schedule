from pydantic import BaseModel


class AdminSchema(BaseModel):
    id: int
    login: str
    password: str
    
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