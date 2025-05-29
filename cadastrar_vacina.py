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
    # --- 1. VERIFICAÇÃO DE LOGIN ---
    # É CRUCIAL que o usuário esteja logado para cadastrar uma vacina.
    # Se 'user_id' não estiver na sessão, redirecione para a página de login.
    if 'user_id' not in session:
        flash('Você precisa estar logado para cadastrar vacinas.', 'warning')
        # Redireciona para o endpoint de login (assumindo que seja 'auth.login' ou 'login.pagina_login')
        # Adapte o 'url_for' para o nome correto do seu endpoint de login.
        return redirect(url_for('login.login'))
    
    # --- 2. PEGAR O ID DO USUÁRIO LOGADO DA SESSÃO ---
    id_usuario_logado = session['user_id']

    if request.method == 'POST':
        nome = request.form.get('nome')        # Use .get() para evitar KeyError
        descricao = request.form.get('descricao') # Use .get() para evitar KeyError

        # Validação básica de campos
        if not nome or not descricao:
            flash("Por favor, preencha todos os campos da vacina.", 'danger')
            return render_template('cadastrarvac.html')

        conn = conectar_bd()
        cursor = conn.cursor()
        
        try:
            # --- 3. INCLUIR O ID DO USUÁRIO NA INSERÇÃO ---
            # Agora a query SQL inclui a coluna 'id_usuario' e o valor do 'id_usuario_logado'
            cursor.execute(
                "INSERT INTO vacinas (nome_vacina, descricao_vacina, id_usuario) VALUES (%s, %s, %s)",
                (nome, descricao, id_usuario_logado) # Passe o id_usuario_logado aqui!
            )
            conn.commit()
            flash("Vacina cadastrada com sucesso!", 'success')
            
            # --- CORREÇÃO NO REDIRECIONAMENTO ---
            # url_for() para o próprio endpoint 'cadastrar' do blueprint 'cadastrarvac'
            # Isso evita que o formulário seja reenviado se o usuário atualizar a página
            return redirect(url_for('cadastrarvac.cadastrar')) 
            
        except mysql.connector.Error as err:
            conn.rollback() # Em caso de erro, desfaça a operação no banco de dados
            flash(f"Erro ao cadastrar vacina: {err}", 'danger')
        finally:
            cursor.close()
            conn.close()
        
    # Se o método for GET, ou se houve um POST com erro, renderiza o template
    return render_template('cadastrarvac.html')
