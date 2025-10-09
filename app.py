# Imports
## Sleep, clear, and input buffer clear 
import os
import sys
import time
## Outras classes
from Categorias.ano import Ano
from Categorias.mes import Mes
from Categorias.publicacao import Publicacao
## Gerenciamento da sessão
from Session.session_manager import configurar_base_de_dados, salvar_sessao, carregar_sessao

def tela_de_boas_vindas():
    print("Seja bem-vindo ao\n")
    print(""" ███████████             █████     ████   ███                                         
  ███     ███             ███       ███                                               
  ███     ███ █████ ████  ███████   ███  ████   ██████   ██████   ████████  █████ ████
  ██████████   ███  ███   ███  ███  ███   ███  ███  ███      ███   ███  ███  ███  ███ 
  ███          ███  ███   ███  ███  ███   ███  ███       ███████   ███  ███  ███  ███ 
  ███          ███  ███   ███  ███  ███   ███  ███  ███ ███  ███   ███  ███  ███  ███ 
 █████          ████████ ████████  █████ █████  ██████   ████████  ███████    ███████ 
                                                                   ███            ███ 
                                                                   ███       ███  ███ 
                                                                  █████       ██████  
                                                                                      """)

def limpar_buffer_teclado():
    """Limpa o buffer do teclado antes de um input (Linux e Windows)."""
    if os.name == 'nt':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
        
def retornar_ao_menu(id = 0):
    if id == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_de_boas_vindas()
        menu_principal()
    elif id == 1:
        limpar_buffer_teclado()
        input("\nPressione Enter para retornar ao menu...")
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_publicacoes()
    elif id == 2:
        limpar_buffer_teclado()
        input("\nPressione Enter para retornar ao menu...")
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_anos()
        
def mostrar_subtitulo(subtitulo):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "*" * len(subtitulo))
    print(subtitulo)
    print("*" * len(subtitulo) + "\n")

def menu_publicacoes():
    mostrar_subtitulo("Menu Publicações")
    print("1. Listar publicações")
    print("2. Adicionar publicação")
    print("3. Remover publicação")
    print("4. Editar quantidade de uma publicação")
    print("5. Voltar ao menu principal")
    try:
        limpar_buffer_teclado()
        opcao_escolhida = int(input("\nDigite o número da opção desejada: "))
    except ValueError:
        print("Erro! Digite uma opção válida.")       
        retornar_ao_menu(1)
        return
    if opcao_escolhida == 1:
        mostrar_subtitulo("Listando publicações")
        Publicacao.listar_publicacoes()
        retornar_ao_menu(1)
    elif opcao_escolhida == 2:
        mostrar_subtitulo("Adicionando publicação")
        limpar_buffer_teclado()
        titulo = input("Digite o título da publicação: ")
        time.sleep(0.5)
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação: ")
        time.sleep(0.5)
        try:
            limpar_buffer_teclado()
            quantidade = int(input("Digite a quantidade da publicação: "))
            time.sleep(0.5)
        except ValueError:
            print("Erro! Digite um número válido para a quantidade.")
            retornar_ao_menu(1)
            return
        nova_publicacao = Publicacao(titulo, codigo, quantidade)
        salvar_sessao(Publicacao.publicacoes)
        print(f"A publicação '{titulo}' foi adicionada com sucesso!")
        retornar_ao_menu(1)
    elif opcao_escolhida == 3:
        mostrar_subtitulo("Removendo publicação")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação a ser removida: ")
        Publicacao.remover_publicacao(codigo)
        salvar_sessao(Publicacao.publicacoes)
        retornar_ao_menu(1)
    elif opcao_escolhida == 4:
        mostrar_subtitulo("Editando quantidade de uma publicação")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação que deseja editar a quantidade: ")
        time.sleep(0.5)
        try:
            limpar_buffer_teclado()
            nova_quantidade = int(input("Digite a nova quantidade: "))
            time.sleep(0.5)
        except ValueError:
            print("Erro! Digite um número válido para a quantidade.")
            retornar_ao_menu(1)
            return
        Publicacao.editar_quantidade(codigo, nova_quantidade)
        salvar_sessao(Publicacao.publicacoes)
        retornar_ao_menu(1)
    elif opcao_escolhida == 5:
        print("Voltando ao menu principal...")
        time.sleep(1)
        retornar_ao_menu()
    else:
        print("Opção inválida. Tente novamente.")
        menu_publicacoes(1)

def menu_anos():
    mostrar_subtitulo("Menu de Gerenciamento de Anos")
    print("1. Listar anos")
    print("2. Listar meses de um ano")
    print("3. Adicionar ano")
    print("4. Remover ano")
    print("5. Voltar ao menu principal")
    try:
        limpar_buffer_teclado()
        opcao_escolhida = int(input("\nDigite o número da opção desejada: "))
    except ValueError:
        print("Erro! Digite uma opção válida.")       
        retornar_ao_menu(2)
        return
    if opcao_escolhida == 1:
        mostrar_subtitulo("Listando anos")
        Ano.listar_anos()
        retornar_ao_menu(2)
    elif opcao_escolhida == 2:
        mostrar_subtitulo("Listando meses de um ano")
        Ano.listar_anos()
        if not Ano.anos:
            retornar_ao_menu(2)
            return
        time.sleep(0.5)
        limpar_buffer_teclado()
        input_ano = input("\nDigite o ano que deseja listar os meses: ")
        if input_ano == "":
            print("Erro! Digite um ano.")
            retornar_ao_menu(2)
            return
        time.sleep(0.5)
        for ano in Ano.anos:
            if ano.ano == input_ano:
                mostrar_subtitulo(f"Listando meses do ano {input_ano}")
                ano.listar_meses()
                break
        else:
            print(f"Nenhum ano '{input_ano}' encontrado.")
        retornar_ao_menu(2)
    elif opcao_escolhida == 3:
        mostrar_subtitulo("Adicionando ano")
        limpar_buffer_teclado()
        novo_ano = input("Digite o ano que deseja adicionar (ex: 2025): ")
        for ano in Ano.anos:
            if ano.ano == novo_ano:
                print(f"O ano '{novo_ano}' já está cadastrado.")
                retornar_ao_menu(2)
                return
        Ano(novo_ano)
        print(f"O ano '{novo_ano}' foi adicionado com sucesso!")
        time.sleep(0.25)
        retornar_ao_menu(2)
    elif opcao_escolhida == 4:
        mostrar_subtitulo("Removendo ano")
        limpar_buffer_teclado()
        input_ano = input("Digite o ano que deseja remover: ")
        for ano in Ano.anos:
            if ano.ano == input_ano:
                print(f"Você tem certeza que deseja remover o ano '{input_ano}'? Esta ação não pode ser desfeita.")
                time.sleep(0.5)
                limpar_buffer_teclado()
                Ano.remover_ano(ano)
                break
        else:
            print(f" O ano '{input_ano}' não foi encontrado.")
        print("Funcionalidade de remover ano ainda não implementada.")
        retornar_ao_menu(2)
    elif opcao_escolhida == 5:
        print("\nVoltando ao menu principal...")
        time.sleep(1)
        retornar_ao_menu()
    else:
        print("Opção inválida. Tente novamente.")
        retornar_ao_menu(2)

def menu_principal():
    print("Escolha uma das opções abaixo:")
    print("1. Menu publicações:")
    print("2. Menu de Gerenciamento de Anos:")
    print("3. Remover publicação:")
    print("4. Sair")
    try:
        limpar_buffer_teclado()
        opcao_escolhida = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Erro! Digite uma opção válida.")       
        retornar_ao_menu()
        return
    if opcao_escolhida == 1:
        menu_publicacoes()
    elif opcao_escolhida == 2:
        menu_anos()
    elif opcao_escolhida == 3:
        mostrar_subtitulo("Removendo publicação")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação a ser removida: ")
        Publicacao.remover_publicacao(codigo)
        retornar_ao_menu()
    elif opcao_escolhida == 4:
        salvar_sessao(Publicacao.publicacoes)
        print("\nTchau! ;)")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Opção inválida. Tente novamente.")
        retornar_ao_menu()

def __main__():
    configurar_base_de_dados()
    for dicio in carregar_sessao().get('publicacoes_salvas', []):
        Publicacao.de_dicionario(dicio)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    tela_de_boas_vindas() 
    menu_principal()  
    
if __name__ == "__main__":
    __main__()


