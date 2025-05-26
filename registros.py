from flask import Blueprint, render_template, request, url_for, redirect
import mysql.connector

registros_bp = Blueprint('registros', __name__,)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port=3307, 
        user="root",
        password="",
        database="projeto-boi"
    )

@registros_bp.route('/', methods=['GET', 'POST'])
def registrar():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        animais = request.form['animal']
        vacina = request.form['vacina']
        data_aplicacao = request.form['data_aplicacao']
        observacoes = request.form['observacoes']
        cursor.execute("""
            INSERT INTO registros_vacina (animais, vacina, data_aplicacao, observacoes)
            VALUES (%s, %s, %s, %s)
        """, (animais, vacina, data_aplicacao, observacoes))
        conn.commit()

    #registros = cursor.fetchall()

    cursor.close()
    conn.close()

    return redirect(url_for('registros.registrar')) and render_template('registro.html', mensagem ="Registro feito com sucesso!")
