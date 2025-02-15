from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    select = SelectField("Найти ученика")
    Submit = SubmitField("Перейти")