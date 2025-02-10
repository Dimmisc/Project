from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class ExselFile(FlaskForm):
    file = FileField('Прикрепите xlsx файл')
    submit = SubmitField('Добавить')