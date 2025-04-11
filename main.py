from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#banco de dados
usuarios = {
    "admin": "1234",  
    "usuario": "senha"
}

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