import sqlite3
import os
import json
from platformdirs import user_data_dir
from Categorias.publicacao import Publicacao

APP_NAME = "Publicapy"
APP_AUTHOR = "RandomUserjs" # Ou o nome que você quiser

# Encontra a pasta padrão do sistema para dados de usuário (ex: ~/.local/share/Publicapy)
DATA_DIR = user_data_dir(APP_NAME, APP_AUTHOR)

DB_FILE_PATH = os.path.join(DATA_DIR, 'publicapy_session.db')

def configurar_base_de_dados():
    # Cria a pasta de dados do app se não existir
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()

    # A tabela terá apenas uma linha para armazenar os dados da sessão.
    # Usaremos uma coluna TEXT para guardar um JSON dos dados.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS session_data (
            id INTEGER PRIMARY KEY,
            data TEXT
        )
    ''')
    conn.commit()
    return conn, cursor

def salvar_sessao(publicacoes):
    """
    Salva os dados da sessão no banco de dados.
    """
    conn, cursor = configurar_base_de_dados()

    serializable_publicacoes = [publicacao.para_dicionario() for publicacao in publicacoes]

    session_data_dict = {
        'publicacoes_salvas': serializable_publicacoes,
    }
    json_data = json.dumps(session_data_dict)
    
    cursor.execute('''
        INSERT OR REPLACE INTO session_data (id, data)
        VALUES (1, ?)
    ''', (json_data,))

    conn.commit()
    conn.close()

# Exemplo de como você chamaria isso:
# current_session = {
#     'ultima_consulta': 'nome_do_usuario',
#     'caminho_salvamento': '/home/user/publicapy_files',
#     'janela_maximizada': True
# }
# save_session(current_session)

def carregar_sessao():
    """
    Carrega os dados da sessão do banco de dados.

    :return: Dicionário com os dados da sessão, ou um dicionário vazio se não houver dados.
    """
    conn, cursor = configurar_base_de_dados()

    # Tenta buscar o registro único
    cursor.execute('SELECT data FROM session_data WHERE id = 1')
    row = cursor.fetchone()

    conn.close()

    if row:
        # Desserializa a string JSON de volta para um dicionário Python
        json_data = row[0]
        session_data_dict = json.loads(json_data)
        print("Dados da sessão restaurados com sucesso.")
        return session_data_dict
    else:
        print("Nenhum dado de sessão anterior encontrado. Iniciando do zero.")
        return {} # Retorna um dicionário vazio para o app iniciar com valores padrão

# Exemplo de como você chamaria isso ao iniciar o Publicapy:
# session_config = load_session()
# ultima_consulta = session_config.get('ultima_consulta', 'valor_padrao')
# janela_maximizada = session_config.get('janela_maximizada', False)