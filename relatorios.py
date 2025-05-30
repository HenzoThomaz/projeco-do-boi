from flask import Blueprint, render_template, redirect, url_for,session,flash
import mysql.connector

relatorios_bp = Blueprint('relatorios', __name__,)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@relatorios_bp.route('/relatorios.html')
def relatorio():
    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login')) 
    else:
        id_usuario_logado = session['user_id']
        
        conn = conectar_bd()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT nome_vacina, animais, data_aplicacao, observacoes FROM registros_vacina WHERE id_usuario = %s""", (id_usuario_logado,)) 

        dados = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('relatorios.html', dados=dados)