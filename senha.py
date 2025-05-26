from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

senha_bp = Blueprint('nova_senha', __name__)

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="projeto-boi"
    )

@senha_bp.route('/senha.html', methods=[ 'POST'])
def redefinir():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['nova_senha']
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET senha = %s WHERE nome = %s", (senha, nome))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('nova_senha')) and render_template('senha.html',mensagem ="Sua senha foi redefinida!")
    return render_template('senha.html')