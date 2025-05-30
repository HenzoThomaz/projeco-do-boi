from flask import Blueprint, render_template, request, url_for, redirect,flash, session
import mysql.connector

registros_bp = Blueprint('registros', __name__,)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@registros_bp.route('/', methods=['GET', 'POST'])
def registrar():

    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login'))
    
    id_usuario_logado = session['user_id']

    if request.method == 'POST':
        animais = request.form['animal']
        vacina = request.form['vacina']
        data_aplicacao = request.form['data_aplicacao']
        observacoes = request.form['observacoes']

        if not vacina or not data_aplicacao:
            return render_template('registro.html', mensagem2='Preencha todos os campos para continuar')
        
        conn = conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO registros_vacina (animais, nome_vacina, data_aplicacao, observacoes, id_usuario)
                VALUES (%s, %s, %s, %s,%s) """, (animais, vacina, data_aplicacao, observacoes, id_usuario_logado))
            conn.commit()

            return redirect(url_for('registros.registrar')) and render_template('registro.html', mensagem ="Registro feito com sucesso!")


        except mysql.connector.Error as err:
            conn.rollback() 
            flash(f"Erro ao registrar relatorio: {err}", 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('registro.html')
