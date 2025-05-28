from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

cadastrar_vacina_bp = Blueprint('cadastrarvac', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@cadastrar_vacina_bp.route('/cadastrarvac.html', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vacinas (nome_vacina, descricao_vacina) VALUES (%s, %s)", (nome, descricao))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('cadastro_vac')) and render_template('cadastrarvac.html',mensagem ="Vacina cadastrada com sucesso!")
    return render_template('cadastrarvac.html')