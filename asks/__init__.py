from pydantic import BaseModel


class AddAskValidator(BaseModel):
    title: str
    description: str
    user_id: int


class AccessToUserIdValidator(BaseModel):
    user_id: int


class AccesToAskIdValidator(BaseModel):
    ask_id: int
