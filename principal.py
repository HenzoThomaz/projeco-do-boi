
from flask import Blueprint, render_template, redirect, url_for,session,flash
import mysql.connector
from datetime import date 

principal_bp = Blueprint('principal', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@principal_bp.route('/principal.html')
def vacina_proxima():
    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login')) 
    else:
        id_usuario_logado = session['user_id']

        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT
    vf.nome_vacina,
    vf.descricao_vacinacao,
    DATE_FORMAT(vf.data, '%d/%m/%Y') AS data_formatada,
    vf.animais FROM vacinas_futuras vf WHERE
    vf.data >= %s AND vf.id_usuario = %s
ORDER BY vf.data ASC LIMIT 1
            """, (date.today(),id_usuario_logado))

        dados = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('principal.html', dados=dados)