from flask import Flask, render_template, request, url_for,redirect,Blueprint
import mysql.connector
from cadastro import conexão_bd

login_bp = Blueprint('login',__name__, url_prefix='/login')

app = Flask(__name__)

conexão_bd

@login_bp.route('/')
def pagina_login():
    return render_template('login.html')

@login_bp.route('/login.html', methods=['POST'])
def login(nome,senha):
    if request.method == 'POST':
        request.form.get['nome'] == nome 
        request.form.get['senha'] == senha

#(cursor = conexão_bd.cursor()
        #query = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
        #cursor.execute(query, (nome, senha))
        #usuario = cursor.fetchone()
        #cursor.close()

    #if usuario:
            # Se as credenciais forem válidas, redirecione para a página principal
            #return render_template('principal.html')
        #else:
            # Se as credenciais forem inválidas, exiba a mensagem de erro novamente no formulário de login
            #return render_template('login.html', mensagem="Nome de usuário ou senha incorretos")
    #else:
        # Se o método da requisição não for POST (por exemplo, GET), apenas renderize a página de login
        #return render_template('login.html', mensagem="Insira as informações para continuar.")


