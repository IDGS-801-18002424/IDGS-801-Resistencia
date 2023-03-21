from flask import Flask, render_template, redirect, url_for, request, make_response, flash
import forms
from Resistencias import Resistencia
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
csrf = CSRFProtect(app)


@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'), 404


@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    resistors = Resistencia()
    res = {}
    banda1 = ''
    banda2 = ''
    banda3 = ''
    tolerancia = ''
    resistencia = forms.ResistenciaForm(request.form)
    if request.method == 'POST' and resistencia.validate():
        banda1 = resistors.setColor(resistencia.banda1.data)
        banda2 = resistors.setColor(resistencia.banda2.data)
        banda3 = resistors.setColor(resistencia.banda3.data)
        tolerancia = resistors.setTolerancia(resistencia.tolerancia.data)
        res = resistors.calcular(resistencia)
        flash('Calculo registrado', 'success')
    return render_template('resistencia.html', form=resistencia, banda1=banda1, banda2=banda2, banda3=banda3, tolerancia=tolerancia, res=res)

@app.route("/cookies", methods=['GET', 'POST'])
def cookies():
    reg_user = forms.LoginForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)

    response = make_response(render_template('cookies.html', form=reg_user))
    if len(datos) > 0:
        response.set_cookie('datos_user', datos)

    return response


@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html', nom=nombres[0])


@app.route("/formulario")
def formulario():
    return render_template('formulario.html')


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template('alumnos.html', form=alum_form)


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, host="10.1.1.11", port=3000)
