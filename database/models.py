from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    password = Column(String, nullable=False)

    reg_date = Column(DateTime)


class UserAsk(Base):
    __tablename__ = 'user_asks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class UserAnswers(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    ask_id = Column(Integer, ForeignKey('user_asks.id'))

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    ask_fk = relationship(UserAsk, lazy='subquery')

