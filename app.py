from flask import Flask, render_template, request, redirect, url_for,Blueprint
from cadastro import cadastro_bp
from login import login_bp

app = Flask(__name__)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)

@app.route('/cadastro.html')
def cadastro():
    return render_template("cadastro.html")

#teste de rota do redefinir senha
@app.route('/senha.html')
def senha():
    return render_template("senha.html")

@app.route('/sobre.html')
def sobre():
    return render_template("sobre.html")

@app.route('/principal.html')
def principal():
    return render_template("principal.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/')
def homepage():
    return render_template("login.html") 


if __name__ == '__main__':
    app.run(debug=True)
    pass