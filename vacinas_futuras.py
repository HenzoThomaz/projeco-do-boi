from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

vacinas_futuras_bp = Blueprint('vacinas_futuras', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@vacinas_futuras_bp.route('/vacinasfuturo.html', methods=[ 'POST'])
def proximavac():
    if request.method == 'POST':
        nome = request.form['nome_vacina']
        descricao = request.form['descricao']
        data = request.form['data']
        animais = request.form['animais']
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vacinas_futuras (nome_vacina, descricao_vacinacao, data, animais) VALUES (%s, %s, %s, %s)", (nome, descricao, data, animais))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('vacinas_futuras')) and render_template('vacinasfuturo.html',mensagem ="Vacina cadastrada com sucesso!")
    return render_template('vacinasfuturo.html')