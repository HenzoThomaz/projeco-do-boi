

from flask import Blueprint, render_template, redirect, url_for
import mysql.connector
from datetime import date 

principal_bp = Blueprint('rpincipal', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="",
        database="projeto-boi"
    )

@principal_bp.route('/principal.html')
def vacina_proxima():
    conn = None
    cursor = None
    proxima_vacina = None
    try:
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True) 

        # Consulta SQL para pegar a vacina futura mais próxima
        # Assumindo que você tem uma tabela como 'vacinas_futuras' com as colunas:
        # id, nome_vacina, descricao, data_prevista, animais
        sql_query = """
            SELECT nome_vacina, descricao, DATE_FORMAT(data, '%d/%m/%Y') as data_formatada, animais
            FROM vacinas_futuras
            WHERE data >= CURDATE()
            ORDER BY data ASC
            LIMIT 1
        """
        cursor.execute(sql_query)
        proxima_vacina = cursor.fetchone() 

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou consultar o banco de dados: {err}")
        
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return render_template('principal.html', proxima_vacina=proxima_vacina)