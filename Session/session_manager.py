import sqlite3
import os
import json
try:
    from platformdirs import user_data_dir
except Exception:
    # Se platformdirs não estiver disponível (ambiente mínimo), usa fallback
    def user_data_dir(app_name, app_author=None):
        # padrão Linux: ~/.local/share/<app_name>
        if os.name == 'nt':
            base = os.getenv('LOCALAPPDATA') or os.getenv('APPDATA') or os.path.expanduser('~')
            if app_author:
                return os.path.join(base, app_author, app_name)
            return os.path.join(base, app_name)
        # POSIX (Linux / macOS) fallback
        return os.path.join(os.path.expanduser('~'), '.local', 'share', app_name)
from Categorias.publicacao import Publicacao
from Categorias.ano import Ano

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

def salvar_sessao(anos):
    """
    Salva os dados da sessão no banco de dados.

    Aceita:
    - lista de instâncias de Ano (serializa anos -> meses -> publicações)
    - lista de Publicacao (compatibilidade retroativa): salva sob chave 'publicacoes_salvas'
    """
    conn, cursor = configurar_base_de_dados()

    session_data_dict = {}

    # Caso vazio: salva anos vazios
    if not anos:
        session_data_dict['Anos cadastrados'] = []
    else:
        first = anos[0]
        # Se for lista de objetos Ano
        if isinstance(first, Ano):
            serializable_anos = []
            for ano in anos:
                meses_list = []
                # percorre meses na ordem
                for mes in ano._meses:
                    pubs = [pub.para_dicionario() for pub in mes.publicacoes]
                    meses_list.append({
                        "num": mes.num,
                        "publicacoes": pubs
                    })
                serializable_anos.append({
                    "ano": ano.ano,
                    "meses": meses_list
                })
            session_data_dict['Anos cadastrados'] = serializable_anos
        # Se for lista de publicações (compatibilidade com código antigo)
        elif isinstance(first, Publicacao):
            session_data_dict['publicacoes_salvas'] = [pub.para_dicionario() for pub in anos]
        else:
            # Tentativa genérica: se os itens forem dicts já serializáveis, grava diretamente
            try:
                json.dumps(anos)
                session_data_dict['raw'] = anos
            except TypeError:
                # fallback: salva vazio
                session_data_dict['Anos cadastrados'] = []

    json_data = json.dumps(session_data_dict, ensure_ascii=False)
    
    cursor.execute('''
        INSERT OR REPLACE INTO session_data (id, data)
        VALUES (1, ?)
    ''', (json_data,))

    conn.commit()
    conn.close()
    
def carregar_sessao():
    """
    Carrega os dados da sessão do banco de dados.

    Reconstrói objetos Ano -> Mes -> Publicacao em memória, preservando ordem.

    :return: Dicionário com os dados brutos da sessão (mesmo formato usado por salvar_sessao).
    """
    conn, cursor = configurar_base_de_dados()

    # Tenta buscar o registro único
    cursor.execute('SELECT data FROM session_data WHERE id = 1')
    row = cursor.fetchone()

    conn.close()

    if not row:
        print("Nenhum dado de sessão anterior encontrado. Iniciando do zero.")
        return {}

    json_data = row[0]
    try:
        session_data_dict = json.loads(json_data)
    except json.JSONDecodeError:
        print("Erro ao desserializar os dados da sessão. Ignorando.")
        return {}

    # Reconstrução: se houver 'Anos cadastrados', cria objetos Ano/Mes/Publicacao mantendo ordem
    if 'Anos cadastrados' in session_data_dict:
        # limpa anos atuais
        Ano.anos = []
        for ano_dict in session_data_dict.get('Anos cadastrados', []):
            ano_val = ano_dict.get('ano')
            # cria o Ano (o construtor já cria 12 meses e adiciona em Ano.anos)
            ano_obj = Ano(ano_val)
            # preenche publicações por mês
            for mes_dict in ano_dict.get('meses', []):
                num = mes_dict.get('num')
                mes_obj = ano_obj.obter_mes(num)
                if mes_obj is None:
                    continue
                for pub_dict in mes_dict.get('publicacoes', []):
                    pub_obj = Publicacao.de_dicionario(pub_dict)
                    mes_obj.publicacoes.append(pub_obj)
        print("Dados da sessão (anos) restaurados com sucesso.")
    # Compatibilidade retroativa: se houver 'publicacoes_salvas', popula Publicacao.publicacoes
    if 'publicacoes_salvas' in session_data_dict:
        pubs = session_data_dict.get('publicacoes_salvas', [])
        # garante existência da lista de publicações na classe
        if not hasattr(Publicacao, 'publicacoes'):
            Publicacao.publicacoes = []
        else:
            Publicacao.publicacoes.clear()
        for pub_dict in pubs:
            pub_obj = Publicacao.de_dicionario(pub_dict)
            Publicacao.publicacoes.append(pub_obj)
        print("Dados da sessão (publicações avulsas) restaurados com sucesso.")

    return session_data_dict

# Exemplo de como você chamaria isso ao iniciar o Publicapy:
# session_config = carregar_sessao()
# -> se havia 'Anos cadastrados' os objetos Ano/Mes/Publicacao já estarão reconstruídos em memória