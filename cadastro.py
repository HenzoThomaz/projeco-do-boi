from flask import Flask, render_template, request, url_for,redirect,Blueprint

#aqui estoy trasnformando o arquivo em um blueprint, que serve para conectar ao arquivo princpal e meio que mandar suas fuções, o app.py sendo o principal, isso serve para que possamos ter varios codicos python em vez de um só no back-end, dexando mais organizado
cadastro_bp = Blueprint('cadastro',__name__, url_prefix='/cadastro')

app = Flask(__name__)

#aqui nos vamos colocar a importação do banco de dados 
def conectar_bd():
#temo que aprender a conectar o bd e colocar aqui então por enquanto so vai ter um pass
    pass

#falta criar a função propriamnete dita
@cadastro_bp.route('/')
def pagina_cadastro():
    return render_template('cadastro.html')

@cadastro_bp.route('/criar_conta', methods=['POST'])
def criar_conta():
    pass


