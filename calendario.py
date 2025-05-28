from flask import Blueprint, render_template
import mysql.connector
from datetime import date

calendario_bp = Blueprint('calendario', __name__,)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@calendario_bp.route('/calendario.html')
def ver_calendario():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    # filtrar as vacinas
    cursor.execute("""
        SELECT
            vf.nome_vacina AS vacina,
            vf.descricao_vacinacao,
            vf.data,
            vf.animais
        FROM vacinas_futuras vf
        WHERE vf.data >= %s
        ORDER BY vf.data ASC
    """, (date.today(),))

    dados = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('calendario.html', dados=dados)