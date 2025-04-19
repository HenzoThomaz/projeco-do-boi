from flask import Flask, render_template, request, redirect, url_for,Blueprint
from cadastro import cadastro_bp

app = Flask(__name__)
app.register_blueprint(cadastro_bp)

#banco de dados
usuarios = {
    "admin": "1234",  
    "usuario": "senha"
}
@app.route('/cadastro.html')
def cadastro():
    return render_template("cadastro.html")

@app.route('/sobre.html')
def sobre():
    return render_template("sobre.html")

@app.route('/login.html')
def retorno_homepage():
    return render_template("login.html")

@app.route('/')
def homepage():
    return render_template("login.html") 

@app.route('/login', methods=['POST'])
def login():
    
    nome = request.form['nome']
    senha = request.form['senha']

    if nome in usuarios and usuarios[nome] == senha:
        return f"<h1>Bem-vindo, {nome}!</h1><p>Login realizado com sucesso.</p>"
    else:
        return "<h1>Falha no login</h1><p>Usuário ou senha incorretos.</p>"

if __name__ == '__main__':
    app.run(debug=True)