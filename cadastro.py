from flask import Flask, render_template, request, url_for,redirect,Blueprint
import mysql.connector

#aqui estoy trasnformando o arquivo em um blueprint, que serve para conectar ao arquivo princpal e meio que mandar suas fuções, o app.py sendo o principal, isso serve para que possamos ter varios codicos python em vez de um só no back-end, dexando mais organizado
cadastro_bp = Blueprint('cadastro',__name__, url_prefix='/cadastro')



app = Flask(__name__)

#aqui nos vamos colocar a importação do banco de dados 
def conectar_bd():
    banco = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha",
  database="seu_banco_de_dados"
)

@cadastro_bp.route('/')
def pagina_cadastro():
    return render_template('cadastro.html')

#falta criar a função propriamnete dita
@cadastro_bp.route('/criar_conta', methods=['POST'])
def criar_conta():
    pass


