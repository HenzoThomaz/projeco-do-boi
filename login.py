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

@login_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        nome_digitado = request.form['nome']
        senha_digitada = request.form['senha']

        
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True)


        query = "SELECT id_usuario, nome, senha FROM usuarios WHERE nome = %s AND senha = %s"
        cursor.execute(query, (nome_digitado, senha_digitada))
        usuario = cursor.fetchone() 

        cursor.close()
        conn.close()

        if usuario:
                session['user_id'] = usuario['id_usuario']                                                     
                session['user_name'] = usuario['nome']

                return redirect(url_for('principal'))

        else:
                return render_template('login.html', mensagem='Usuario ou senha estão incorretos' ) 