from flask import flash
from flask_wtf import FlaskForm
from wtforms import SubmitField,EmailField,StringField,PasswordField,ValidationError,IntegerField
from wtforms.validators import DataRequired,EqualTo
from appLogin.basededatos import Usuario

class FormularioRegistro(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    apellido = StringField('Apellido',validators=[DataRequired()])
    edad = IntegerField('Edad')
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('check_password',message='No coinciden las pass')])
    check_password = PasswordField('Confirmar password',validators=[DataRequired()])
    boton= SubmitField('Registrarme')
    
    def verificarEmail(self,emailCheck):
        if Usuario.query.filter_by(email=emailCheck.data).first():
            raise ValidationError('EMAIL YA REGISTRADO!')       

class FormularioLogin(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    boton= SubmitField('Entrar')