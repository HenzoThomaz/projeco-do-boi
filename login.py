from flask import Flask, render_template, request, url_for,redirect,Blueprint, flash, session
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

@login_bp.route('/login', methods=['POST']) # Removendo .html do nome da rota
def login():
    if request.method == 'POST':
        nome_digitado = request.form['nome']
        senha_digitada = request.form['senha']

        
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True)


        query = "SELECT id_usuario, nome, senha FROM usuarios WHERE nome = %s AND senha = %s"
        cursor.execute(query, (nome_digitado, senha_digitada))
        usuario = cursor.fetchone() # usuario será um dicionário se encontrado

        cursor.close()
        conn.close()

        if usuario:
                # --- AQUI É ONDE USAMOS A SESSION! ---
                # Armazene o ID do usuário (gerado automaticamente pelo BD) na sessão
                session['user_id'] = usuario['id_usuario']
                # Armazene o nome do usuário também para exibir na interface, se quiser
                session['user_name'] = usuario['nome']

                flash(f"Login realizado com sucesso! Bem-vindo(a), {usuario['nome']}!", 'success')
                return redirect(url_for('principal')) # Redirecione para a página principal

        else:
                # Se não encontrar o usuário ou a senha estiver incorreta
                flash("Nome de usuário ou senha incorretos.", 'danger')
                return render_template('login.html') # Renderiza o formulário de login novamente com a mensagem de erro