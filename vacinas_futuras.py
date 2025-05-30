from flask import Blueprint, render_template, request, redirect, url_for,session,flash
import mysql.connector

vacinas_futuras_bp = Blueprint('vacinas_futuras', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="projeto-boi"
    )

@vacinas_futuras_bp.route('/vacinasfuturo.html', methods=[ 'POST'])
def proximavac():
    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        return redirect(url_for('login.login'))
    
    id_usuario_logado = session['user_id']

    if request.method == 'POST':
        nome = request.form['nome_vacina']
        descricao = request.form['descricao']
        data = request.form['data']
        animais = request.form['animais']

        if not nome or not data:
            return render_template('vacinasfuturo.html', mensagem2='Preencha todos os campos para continuar')

        conn = conectar_bd()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO vacinas_futuras (nome_vacina, descricao_vacinacao, data, animais, id_usuario) VALUES (%s, %s, %s, %s,%s)", (nome, descricao, data, animais,id_usuario_logado))
            conn.commit()

            return redirect(url_for('vacinas_futuras.proximavac')) and render_template('vacinasfuturo.html',mensagem ="Vacina futura cadastrada com sucesso!")

        except mysql.connector.Error as err:
            conn.rollback() 
            flash(f"Erro ao registrar vacina futura: {err}", 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('vacinasfuturo.html')