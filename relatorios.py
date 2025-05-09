from flask import Blueprint, render_template
import mysql.connector

relatorios_bp = Blueprint('relatorios', __name__, url_prefix='/relatorios')

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projeto-boi"
    )

@relatorios_bp.route('/')
def relatorio():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            v.nome AS vacina, 
            COUNT(*) AS total_aplicacoes
        FROM registros_vacina r
        JOIN vacinas v ON r.id_vacina = v.id
        GROUP BY v.nome
    """)
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('relatorios.html', dados=dados)