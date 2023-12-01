from database.models import UserAnswers, User, UserAsk
from database import get_db
from datetime import datetime


def add_answer_db(user_id, ask_id, answer):
    db = next(get_db())
    user_checker = db.query(User).filter_by(id=user_id).first()
    ask_checker = db.query(UserAsk).filter_by(id=ask_id).first()
    if user_checker:
        if ask_checker:
            answer = UserAnswers(user_id=user_id, ask_id=ask_id, answer=answer, reg_date=datetime.now())
            db.add(answer)
            db.commit()
            return {'status': 1,
                    'message': 'Ответ успешно добавлен'}
        else:
            return {'status': 0,
                    'message': 'Опрос не найден'}
    else:
        return {'status': 0,
                'message': 'Пользователь не найден'}


def edit_answer_db(answer_id, new_answer):
    db = next(get_db())
    text = db.query(UserAnswers).filter_by(id=answer_id).first()
    if text:
        text.answer = new_answer
        db.commit()
        return {'status': 1,
                'message': {'Ответ успешно изменен': new_answer}}
    else:
        return {'status': 0,
                'message': 'Нет такого ответа'}


def get_users_answers(user_id):
    db = next(get_db())
    answer = db.query(UserAnswers).filter_by(user_id=user_id).all()
    if answer:
        return {'status': 1,
                'message': {'Ответы данного пользователя': answer}}
    else:
        return {'status': 0,
                'message': 'Ответов от данного пользователя не надйено'}


def delete_user_answer(answer_id):
    db = next(get_db())
    answer = db.query(UserAnswers).filter_by(id=answer_id).first()
    all_answers = db.query(UserAnswers).all()
    if answer:
        db.delete(answer)
        db.commit()
        return {'status': 1,
                'message': {'Ответ успешно удален': {'Все ответы': all_answers}}}
    else:
        return {'status': 0,
                'message': 'Такого пользователя нет'}

