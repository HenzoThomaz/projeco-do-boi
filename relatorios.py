from flask import Blueprint, render_template, redirect, url_for
import mysql.connector

relatorios_bp = Blueprint('relatorios', __name__,)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projeto-boi"
    )

@relatorios_bp.route('/relatorios.html')
def relatorio():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)
    cursor.execute
    dados= []
    try:
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True) 
        cursor.execute("SELECT vacina, animais, data_aplicacao, observacoes FROM registros_vacina") 

        dados = cursor.fetchall()

        return render_template('relatorios.html',dados=dados)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()