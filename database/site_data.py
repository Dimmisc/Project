import sqlalchemy as sa
from sqlalchemy import orm
from .db_session import DataBase


class Grades(DataBase):
    __tablename__ = "grades"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    grade = sa.Column(sa.String)


    students = orm.relationship("Students", back_populates="Grade")


class Students(DataBase):
    __tablename__ = "students"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String)
    name = sa.Column(sa.String)
    patronymic = sa.Column(sa.String)
    status = sa.Column(sa.String)
    grade_name = sa.Column(sa.String)


    grade_id = sa.Column(sa.Integer, sa.ForeignKey("grades.id"))

    Grade = orm.relationship("Grades", back_populates="students")
    Visits = orm.relationship("Visitings", back_populates="student")


class XLSXFILES(DataBase):
    __tablename__ = 'xlsxfiles'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    file_href = sa.Column(sa.String)
    data = sa.Column(sa.Date)