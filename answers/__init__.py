from pydantic import BaseModel


class AddAnswerValidator(BaseModel):
    ask_id: int
    user_id: int
    answer: str


class AccessToUserIdValidator(BaseModel):
    user_id: int


class EditAnswerDataValidator(BaseModel):
    answer_id: int
    new_answer: str


class AccessToAnswerIdValidator(BaseModel):
    answer_id: int
