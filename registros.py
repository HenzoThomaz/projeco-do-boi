from flask import Blueprint, render_template, request
import mysql.connector

registros_bp = Blueprint('registros', __name__, url_prefix='/registros')

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projeto-boi"
    )

@registros_bp.route('/', methods=['GET', 'POST'])
def registrar():
    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        id_animal = request.form['animal']
        id_vacina = request.form['vacina']
        data_aplicacao = request.form['data_aplicacao']
        observacoes = request.form['observacoes']
        cursor.execute("""
            INSERT INTO registros_vacina (id_animal, id_vacina, data_aplicacao, observacoes)
            VALUES (%s, %s, %s, %s)
        """, (id_animal, id_vacina, data_aplicacao, observacoes))
        conn.commit()

    cursor.execute("SELECT * FROM animais")
    animais = cursor.fetchall()

    cursor.execute("SELECT * FROM vacinas")
    vacinas = cursor.fetchall()

    cursor.execute("""
        SELECT a.nome AS animal, v.nome AS vacina, r.data_aplicacao, r.observacoes
        FROM registros_vacina r
        JOIN animais a ON r.id_animal = a.id
        JOIN vacinas v ON r.id_vacina = v.id
        ORDER BY r.data_aplicacao DESC
    """)
    registros = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('registros.html', animais=animais, vacinas=vacinas, registros=registros)