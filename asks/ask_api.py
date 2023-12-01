from fastapi import APIRouter
from asks import AddAskValidator
from database.ask_service import add_ask_db, show_all_users_ask, show_all_asks, delete_exact_ask, get_ask_answers


ask_router = APIRouter(prefix='/ask', tags=['Опросы и Настройки'])


@ask_router.post('/add')
async def add_ask(data: AddAskValidator):
    ask = data.model_dump()
    result = add_ask_db(**ask)
    return {'message': result}


@ask_router.get('/all-users')
async def all_users_asks(user_id: int):
    result = show_all_users_ask(user_id)
    return {'message': result}


@ask_router.get('/all')
async def all_asks():
    result = show_all_asks()
    return {'message': result}


# @ask_router.delete('/delete-all-asks')
# async def delete_all_asks():
#     result = delete_all_asks()
#     return {'message': result}


# @ask_router.delete('/delete-user-asks')
# async def delete_user_asks(user_id: int):
#     result = delete_user_ask(user_id)
#     return {'message': result}


@ask_router.delete('/delete')
async def delete_ask(ask_id: int):
    result = delete_exact_ask(ask_id)
    return {'message': result}


@ask_router.get('/get-ask-answers')
async def ask_answers(ask_id: int):
    result = get_ask_answers(ask_id)
    return {'message': result}