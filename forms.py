from flask_wtf import FlaskForm
import wtforms as wf
from wtforms import validators
from app.models import User

class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ok')

    def validate_username(self, name):
        expected_name = User.query.filter_by(username=name.data).first()
        if expected_name:
            raise validators.ValidationError('Такой пользователь уже существует')

    def validate_password(self, field):
        f_list = []
        for i in field.data:
            f_list.append(i)
        if len(f_list) < 8:
            raise validators.ValidationError('Пароль не должен быть короче 8 символов')
        if field.data.isdigit():
            raise validators.ValidationError('Пароль не может содержать одни цифры')
        if field.data.isalpha():
            raise validators.ValidationError('Пароль не может содержать одни буквы')
        field.data = field.data.replace('1', '')
        field.data = field.data.replace('2', '')
        field.data = field.data.replace('3', '')
        field.data = field.data.replace('4', '')
        field.data = field.data.replace('5', '')
        field.data = field.data.replace('6', '')
        field.data = field.data.replace('7', '')
        field.data = field.data.replace('8', '')
        field.data = field.data.replace('9', '')
        field.data = field.data.replace('0', '')
        if field.data.isalpha():
            raise validators.ValidationError('Пароль должен содержать символы')


class PostForm(FlaskForm):
    title = wf.StringField('Заголовок', validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField('Текст Новости', validators=[wf.validators.DataRequired()])
    is_boom_news = wf.BooleanField('Горячие новости')
    submit = wf.SubmitField('Ok')