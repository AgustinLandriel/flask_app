import email
from flask import flash,redirect,url_for,render_template
from werkzeug.security import check_password_hash
from flask_login import login_manager,login_required, login_user,logout_user
from appLogin.basededatos import Usuario
from appLogin import db,app,gestor
from appLogin.formularios import FormularioLogin, FormularioRegistro


@gestor.user_loader
def cargador_usuario(usuarioID):
    return Usuario.query.get(usuarioID)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bienvenido')
@login_required
def bienvenido():
    return render_template('bienvenido.html')

@app.route('/registro',methods=['GET','POST'])
def registro():
    formulario = FormularioRegistro()
    if formulario.validate_on_submit():
        formulario.verificarEmail(formulario.email)
        usuario = Usuario(nombre=formulario.nombre.data,apellido=formulario.apellido.data,edad=formulario.edad.data,email=formulario.email.data,password=formulario.password.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Registrado correctamente.')
        return redirect(url_for('login'))
        
    return render_template('registro.html',form=formulario) 


@app.route('/login',methods=['GET','POST'])
def login():
    formulario=FormularioLogin()
    if formulario.validate_on_submit():
        usuario=Usuario.query.filter_by(email=formulario.email.data).first()
        if usuario is not None:
            if check_password_hash(usuario.password_encriptada,formulario.password.data):
                login_user(usuario)
                flash('Has iniciado sesión correctamente.')
                return redirect(url_for('bienvenido'))
    return render_template('login.html',form=formulario)


@app.route('/salir')
@login_required
def salir():
    logout_user()
    flash('Has cerrado sesión')
    return render_template('index.html')    


if __name__ == '__main__':
    app.run(debug=True)    