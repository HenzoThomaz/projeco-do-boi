from flask import Blueprint, render_template
import mysql.connector

calendario_bp = Blueprint('calendario', __name__, url_prefix='/calendario')

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="projeto-boi"
    )

@calendario_bp.route('/')
def ver_calendario():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT a.nome AS animal, v.nome AS vacina, c.data_vacinacao
        FROM calendario_vacinacao c
        JOIN animais a ON c.id_animal = a.id
        JOIN vacinas v ON c.id_vacina = v.id
        ORDER BY c.data_vacinacao
    """)
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('calendario.html', dados=dados)