import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import DataBase


# class Users(DataBase):
#     __tablename__ = 'users'
    
#     id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
#     status = sa.Column(sa.String)
#     login = sa.Column(sa.String)
#     hashed_password = sa.column(sa.String)

#     # Files = orm.Relationship("xlsxfiles", back_populates='User')

#     VWS = sa.Column(sa.Boolean)