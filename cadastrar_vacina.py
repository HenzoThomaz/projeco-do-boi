from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector

cadastrar_vacina_bp = Blueprint('cadastrarvac', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@cadastrar_vacina_bp.route('/cadastrarvac.html', methods=['GET', 'POST'])
def cadastrar():

    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login'))
    
    id_usuario_logado = session['user_id']

    if request.method == 'POST':
        nome = request.form.get('nome')       
        descricao = request.form.get('descricao')

        if not nome or not descricao:
            return render_template('cadastrarvac.html', mensagem2='Preencha todos os campos para continuar')

        conn = conectar_bd()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO vacinas (nome_vacina, descricao_vacina, id_usuario) VALUES (%s, %s, %s)",
                (nome, descricao, id_usuario_logado) 
            )
            conn.commit()
            
            return redirect(url_for('cadastrarvac.cadastrar')) and render_template('cadastrarvac.html',mensagem='Vacina cadastrada com sucesso!')
            
        except mysql.connector.Error as err:
            conn.rollback() 
            flash(f"Erro ao cadastrar vacina: {err}", 'danger')
        finally:
            cursor.close()
            conn.close()
        
    return render_template('cadastrarvac.html')
