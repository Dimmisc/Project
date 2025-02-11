import sqlalchemy as sa

from .db_session import DataBase


class Visitings(DataBase):
    __tablename__ = 'visitings'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    date = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronomic = sa.Column(sa.String)
    firstEnter = sa.Column(sa.String)
    lastExit = sa.Column(sa.String)
    attended = sa.Column(sa.Boolean)
    status = sa.Column(sa.String)