from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
from appLogin import db

class Usuario(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    nombre= db.Column(db.String(30))
    apellido= db.Column(db.String(30))
    edad=db.Column(db.Integer)
    email=db.Column(db.String(50),unique=True)
    password_encriptada = db.Column(db.String(50))

    def __init__(self,nombre,apellido,edad,password,email):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.email=email
        self.password_encriptada=generate_password_hash(password)

    def verificar_pass(self,password):
        return check_password_hash(self.password_encriptada,password)    