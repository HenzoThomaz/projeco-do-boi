from flask import Flask, render_template, request, url_for,redirect,Blueprint
import mysql.connector

#aqui estoy trasnformando o arquivo em um blueprint, que serve para conectar ao arquivo princpal e meio que mandar suas fuções, o app.py sendo o principal, isso serve para que possamos ter varios codicos python em vez de um só no back-end, dexando mais organizado
cadastro_bp = Blueprint('cadastro',__name__, url_prefix='/cadastro')

app = Flask(__name__)

def salvar_no_bd(nome, telefone, senha):
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="projeto-boi" )
  
  cursor = conn.cursor()
  query = "INSERT INTO usuarios (nome, telefone, senha) VALUES (%s, %s, %s)"
  cursor.execute(query, (nome, telefone, senha))
  conn.commit()
  cursor.close()
  conn.close()

@cadastro_bp.route('/')
def pagina_cadastro():
    return render_template('cadastro.html')

    #falta fazer funcionar pqp
@cadastro_bp.route('/cadastro.html', methods=['POST'])
def criar_conta():
  
  if request.method == 'POST':
    nome = request.form['nome']
    telefone = request.form['telefone']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']
    
    if request.form['confirmar_senha'] != request.form['senha']:
      return render_template("/cadastro.html",mensagem="As senhas inseridas não são iguais!")   
  
  salvar_no_bd(nome,telefone,senha)
  return render_template("/cadastro.html",mensagem="Sua conta foi criada com sucesso!")

    
    



