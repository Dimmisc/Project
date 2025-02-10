import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import DataBase


class Users(DataBase): # База данных пользователей сайта
    __tablename__ = 'users'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)
    password = sa.Column(sa.String)

    
