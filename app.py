import os
import sys
import time
import sqlite3
from Categorias.publicacao import Publicacao
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
        print(f"A publicação '{titulo}' foi adicionada com sucesso!")
        retornar_ao_menu(1)
    elif opcao_escolhida == 3:
        mostrar_subtitulo("Removendo publicação")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação a ser removida: ")
        Publicacao.remover_publicacao(codigo)
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
        retornar_ao_menu(1)
    elif opcao_escolhida == 5:
        print("Voltando ao menu principal...")
        time.sleep(1)
        retornar_ao_menu()
    else:
        print("Opção inválida. Tente novamente.")
        menu_publicacoes(1)

def menu_principal():
    print("Escolha uma das opções abaixo:")
    print("1. Menu publicações:")
    print("2. Adicionar publicação:")
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
        mostrar_subtitulo("Adicionando publicação")
        limpar_buffer_teclado()
        titulo = input("Digite o título da publicação: ")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação: ")
        limpar_buffer_teclado()
        try:
            quantidade = int(input("Digite a quantidade da publicação: "))
        except ValueError:
            print("Erro! Digite um número válido para a quantidade.")
            retornar_ao_menu()
            return
        nova_publicacao = Publicacao(titulo, codigo, quantidade)
        print(f"A publicação '{titulo}' adicionada com sucesso!")
        retornar_ao_menu()
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
        menu_principal()

def __main__():
    for dicio in carregar_sessao().get('publicacoes_salvas', []):
        Publicacao.de_dicionario(dicio)
    configurar_base_de_dados()
    tela_de_boas_vindas() 
    menu_principal()  
    
if __name__ == "__main__":
    __main__()


