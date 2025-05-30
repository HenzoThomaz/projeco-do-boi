from flask import Blueprint, render_template,session,flash,redirect,url_for
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
    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login')) 
    else:
        id_usuario_logado = session['user_id']

        conn = conectar_bd()
        cursor = conn.cursor()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT
                    vf.nome_vacina AS vacina,
                    vf.descricao_vacinacao,
                    vf.data,
                    vf.animais
                FROM vacinas_futuras vf
                WHERE vf.data >= %s AND vf.id_usuario = %s
                ORDER BY vf.data ASC
            """, (date.today(),id_usuario_logado))

        dados = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('calendario.html', dados=dados)