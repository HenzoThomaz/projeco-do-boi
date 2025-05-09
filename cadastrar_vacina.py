from flask import Blueprint, render_template, request, redirect
import mysql.connector

cadastrar_vacina_bp = Blueprint('cadastrar_vacina', __name__, url_prefix='/vacina')

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projeto-boi"
    )

@cadastrar_vacina_bp.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vacinas (nome, descricao) VALUES (%s, %s)", (nome, descricao))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('cadastrar_vacina.html', mensagem="Vacina cadastrada com sucesso!")
    return render_template('cadastrar_vacina.html')