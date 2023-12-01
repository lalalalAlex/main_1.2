from .models import UserAsk, User, UserAnswers
from database import get_db
from datetime import datetime


def checker_descriptions(description):
    db = next(get_db())
    checker = db.query(UserAsk).filter_by(description=description).first()
    if checker:
        return False
    else:
        return 'Данного Опроса еще нет'


def add_ask_db(title, description, user_id):
    db = next(get_db())
    user_checker = db.query(User).filter_by(id=user_id).first()
    if user_checker:
        ask_checker = checker_descriptions(description)
        if not ask_checker:
            return {'status': 0,
                    'message': 'Данный опрос уже существует'}
        else:
            ask = UserAsk(title=title, description=description, user_id=user_id, reg_date=datetime.now())
            db.add(ask)
            db.commit()
            return {'status': 1,
                    'message': {'Опрос успешно добавлен': ask.title}}
    else:
        return {'status': 0,
                'message': 'Данного пользователя не существует'}


def show_all_users_ask(user_id):
    db = next(get_db())
    checker_user = db.query(User).filter_by(id=user_id).first()
    ask = db.query(UserAsk).filter_by(user_id=user_id).first()
    if checker_user:
        if ask:
            return {'status': 1,
                    'message': ask}
        else:
            return {'status': 0,
                    'message': 'У данного пользователя еще нет Опросов'}
    else:
        return {'status': 0,
                'message': 'Данного пользователя нет'}


def show_all_asks():
    db = next(get_db())
    ask = db.query(UserAsk).all()
    if ask:
        return {'status': 1,
                'message': ask}
    else:
        return {'status': 0,
                'message': 'Опросов пока нет'}


# def delete_all_asks():
#     db = next(get_db())
#     ask = db.query(UserAsk).all()
#     db.delete(ask)
#     db.commit()
#     return 'круто'


# def delete_user_ask(user_id):
#     db = next(get_db())
#     asks = db.query(UserAsk).filter_by(user_id=user_id).all()
#     db.delete(asks)
#     db.commit()
#     return 'Все удалено'


def delete_exact_ask(ask_id):
    db = next(get_db())
    ask = db.query(UserAsk).filter_by(id=ask_id).first()
    if ask:
        db.delete(ask)
        db.commit()
        return {'status': 1,
                'message': 'Опрос успешно удален'}
    else:
        return {'status': 0,
                'message': 'Опрос с данным id не найден'}


def get_ask_answers(ask_id):
    db = next(get_db())
    answers = db.query(UserAnswers).filter_by(ask_id=ask_id).all()
    ask_checker = db.query(UserAsk).filter_by(id=ask_id).first()
    if ask_checker:
        if answers:
            return {'status': 1,
                    'message': answers}
        else:
            return {'status': 0,
                    'message': 'У данного опроса еще нет Ответов'}
    else:
        return {'status': 0,
                'message': 'Данного Опроса не существует'}

