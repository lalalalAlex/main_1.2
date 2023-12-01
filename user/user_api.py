from fastapi import APIRouter
from user import UserRegistrationValidator, UserLoginValidator, EditUserDataValidator, AccesToUserIdValidator
from database.user_service import register_user_db, checker_email_db, login_user_db, edit_user_db, get_exact_user_data_db, delete_user_db, get_all_users


user_router = APIRouter(prefix='/user', tags=['Пользователи и Настройки'])


@user_router.post('/register')
async def register_user(data: UserRegistrationValidator):
    user = data.model_dump()
    result = register_user_db(**user)
    return {'message': result}


@user_router.post('/get-exact-data')
async def exact_user_data(data: AccesToUserIdValidator):
    user = data.model_dump()
    result = get_exact_user_data_db(**user)
    return {'message': result}


# @user_router.get('/check-email')
# async def check_email_user(email: str):
#     result = checker_email_db(email)
#     return {'message': result}


@user_router.post('/login')
async def login_user(data: UserLoginValidator):
    user = data.model_dump()
    result = login_user_db(**user)
    return {'message': result}


@user_router.put('/edit-profile')
async def edit_user(data: EditUserDataValidator):
    user = data.model_dump()
    result = edit_user_db(**user)
    return {'message': result}


@user_router.delete('/delete-data')
async def delete_user(data: AccesToUserIdValidator):
    user = data.model_dump()
    result = delete_user_db(**user)
    return {'message': result}


@user_router.get('/get-all-users')
async def all_users():
    result = get_all_users()
    return {'message': result}