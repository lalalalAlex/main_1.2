from pydantic import BaseModel


class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str


class UserLoginValidator(BaseModel):
    email: str
    password: str


class EditUserDataValidator(BaseModel):
    user_id: int
    component: str
    new_data: str


class AccesToUserIdValidator(BaseModel):
    user_id: int

