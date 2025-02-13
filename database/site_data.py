import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import DataBase


class Students(DataBase):
    __tablename__ = "students"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronomic = sa.Column(sa.String)
    school_class = sa.Column(sa.String)


class XLSXFILES(DataBase):
    __tablename__ = 'xlsxfiles'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    file_href = sa.Column(sa.String)