from flask import Flask, render_template, request, redirect, url_for,Blueprint, session, flash
from datetime import timedelta
from cadastro import cadastro_bp
from login import login_bp
from cadastrar_vacina import cadastrar_vacina_bp
from calendario import calendario_bp
from registros import registros_bp
from relatorios import relatorios_bp
from senha import senha_bp
from vacinas_futuras import vacinas_futuras_bp
from principal import principal_bp

app = Flask(__name__)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastrar_vacina_bp)
app.register_blueprint(calendario_bp)
app.register_blueprint(registros_bp)
app.register_blueprint(relatorios_bp)
app.register_blueprint(senha_bp)
app.register_blueprint(vacinas_futuras_bp)
app.register_blueprint(principal_bp)

app.secret_key = 'chave_secreta' 
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)

@app.route('/cadastro.html')
def cadastro():
    return render_template("cadastro.html")

@app.route('/vacinasfuturo.html')
def vacinas_futuras():
    return render_template("vacinasfuturo.html")

#teste de rota do redefinir senha
@app.route('/senha.html')
def nova_senha():
    return render_template("senha.html")

@app.route('/sobre.html')
def sobre():
    return render_template("sobre.html")

@app.route('/principal.html')
def principal():
    return render_template("/principal.html")

#@app.route('/login.html')
#def login():
 #   return render_template("login.html")

@app.route('/cadastrarvac.html')
def cadastro_vac():
    return render_template("cadastrarvac.html")

@app.route('/calendario.html')
def calendario():
    return render_template("calendario.html")

@app.route('/registro.html')
def registros():
    return render_template("registro.html")

@app.route('/relatorios.html')
def relatorios():
    return render_template("relatorios.html")

@app.route('/')
def homepage():
    return render_template("login.html") 


if __name__ == '__main__':
    app.run(debug=True)
    pass