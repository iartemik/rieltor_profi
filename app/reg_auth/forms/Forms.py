from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,IntegerField,
SubmitField,TextAreaField, EmailField)
from wtforms.validators import (ValidationError,
                                DataRequired,
                                        Email)
from app import *



class LoginForm(FlaskForm):
     phone = StringField(label='Телефон',name="login-phone", validators=[DataRequired()])
     is_rieltor=BooleanField(label='Вы риелтор?',name='is_rieltor')
     submit = SubmitField('Вход')

class RegisterForm(FlaskForm):
     username = StringField(label='Имя и Фамилия',name='username',validators=[DataRequired()])
     email = EmailField(label='Email',name='email',validators=[Email(),DataRequired()])
     phone = StringField(label='Телефон',name="register-phone", validators=[DataRequired()])
     is_rieltor=BooleanField(label='Вы риелтор?',name='is_rieltor')
     experience=IntegerField(label='Стаж работы',name='experience')
     company= StringField(label='Компания',name='company')
     info=TextAreaField(label='Дополнительная информация',name='info')
     submit = SubmitField('Зарегистрироваться')

     def validate_email_phone(self,email,phone):
            model=Client
            if self.is_rieltor.data:
                    model=Rieltor
            user = model.query.filter(or_(model.email==email,model.phone==phone) ).first()
            if user != None:
                raise ValidationError("Вы уже зарегистрированы!")
     def validate_fields_by_rieltor(self):
                if self.experience.data is None or self.company.data is None or self.info.data is None: 
                     raise ValidationError("Поля для риелтора должны быть все заполнены!")
                
         
        

                
 


