from flask import Flask, render_template, request, url_for,redirect,Blueprint
import mysql.connector


login_bp = Blueprint('login',__name__)

app = Flask(__name__)

def conectar_bd():
    conn = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )
    return conn

@login_bp.route('/')
def pagina_login():
    return render_template('login.html')

@login_bp.route('/login.html', methods=['POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')

        try:
                conn = conectar_bd()
                cursor = conn.cursor()
                query = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
                cursor.execute(query, (nome, senha))
                usuario = cursor.fetchone()
                cursor.close()
                conn.close()    

                if usuario:
                # Se tudo estiver certinho no bd, redirecione para a página principal
                    return redirect(url_for('principal'))
                else:
                # Se n exiba a mensagem de erro novamente no formulário de login do html
                    return render_template('login.html', mensagem="Nome de usuário ou senha incorretos")
        except mysql.connector.Error as err:
            mensagem = f"Erro ao conectar ao banco de dados: {err}"
            return render_template('login.html', mensagem=f"Erro no servidor: {mensagem}")
