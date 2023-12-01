from .models import User
from database import get_db
from datetime import datetime


def checker_email_db(email):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        return {'status': '-',
                'message': 'Пользователь существует'}
    else:
        return False


def phone_number_checker(phone_number):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return {'status': '-',
                'message': 'Пользователь существует'}
    else:
        return checker


def register_user_db(name, surname, email, password, phone_number):
    db = next(get_db())
    checker = checker_email_db(email)
    if checker:
        return {'status': 0,
                'message': 'Пользователь уже существует'}
    else:
        user = User(name=name, surname=surname, email=email, password=password, phone_number=phone_number, reg_date=datetime.now())
        db.add(user)
        db.commit()
        return {'status': 1,
                'message': 'Пользователь успешно добавлен'}


def login_user_db(email, password):
    db = next(get_db())
    user = db.query(User).filter_by(email=email).first()
    if user:
        if user.password == password:
            return {'status': 1,
                    'message': user}
        elif user.password != password:
            return {'status': 0,
                    'message': 'Пароль введен неверно'}
        else:
            return False
    else:
        return {'status': 0,
                'message': 'Пользователя с данным e-mail не существует'}


def edit_user_db(user_id, component, new_data):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        if component == 'password':
            exact_user.password = new_data
        elif component == 'email':
            checker = checker_email_db(component)
            if checker:
                return 'Данный e-mail уже занят'
            else:
                exact_user.email = new_data
        elif component == 'name':
            exact_user.name = new_data
        elif component == 'surname':
            exact_user.surname = new_data
        elif component == 'phone_number':
            checker = phone_number_checker(component)
            if checker:
                return {'status': 0,
                        'message': 'Пользователь с данным номером телефона существует'}
        else:
            return {'status': 0,
                    'message': 'Данного типа изменения не нашлось. Попробуйте позже'}

        db.commit()
        return {'status': 1,
                'message': 'Данные успешно изменены'}
    return {'status': 0,
            'message': 'Данный пользователь не найден'}


def get_exact_user_data_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        return {'status': 1,
                'message': {'Имя': user.name,
                            'Фамилия': user.surname,
                            'E-mail': user.email,
                            'Пароль': user.password,
                            'id': user.id}
                }
    else:
        return {'status': 0,
                'message': 'Нет пользователя с данным id'}


def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'


def get_all_users():
    db = next(get_db())
    users = db.query(User).all()
    if users:
        return users
    else:
        return 'Пока нет пользователей'





