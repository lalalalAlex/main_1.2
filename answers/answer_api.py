from fastapi import APIRouter
from database.answer_service import add_answer_db, edit_answer_db, get_users_answers, delete_user_answer
from answers import AddAnswerValidator, EditAnswerDataValidator


answer_router = APIRouter(prefix='/answer', tags=['Ответы и Настройки'])


@answer_router.post('/add-answer')
async def add_answer(data: AddAnswerValidator):
    answer = data.model_dump()
    result = add_answer_db(**answer)
    return {'message': result}


@answer_router.put('/edit-answer')
async def edit_answer(data: EditAnswerDataValidator):
    answer = data.model_dump()
    result = edit_answer_db(**answer)
    return {'message': result}


@answer_router.post('/get-users-answers')
async def get_answers(user_id: int):
    result = get_users_answers(user_id)
    return {'message': result}


@answer_router.delete('/delete-user-answer')
async def delete_answer(answer_id: int):
    result = delete_user_answer(answer_id)
    return {'message': result}


# @answer_router.get('/get-ask-answers')
# async def get_answers(ask_id: int):
#     result = get_ask_answers(ask_id)
#     return {'message': result}
