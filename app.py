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


def _salvar_sessao_auto():
    """Salva a sessão escolhendo automaticamente o formato correto.

    Se houver anos cadastrados usa `Ano.anos` (salva anos -> meses -> publicações).
    Caso contrário, salva a lista legado `Publicacao.publicacoes` para
    compatibilidade retroativa.
    """
    if getattr(Ano, 'anos', None):
        salvar_sessao(Ano.anos)
    else:
        if not hasattr(Publicacao, 'publicacoes'):
            Publicacao.publicacoes = []
        salvar_sessao(Publicacao.publicacoes)

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
        
def retornar_ao_menu(id = 0, ano = None, mes = None):
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
    elif id == 3:
        limpar_buffer_teclado()
        input("\nPressione Enter para retornar ao menu...")
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_meses()
    elif id == 4:
        limpar_buffer_teclado()
        input("\nPressione Enter para retornar ao menu...")
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_mes(ano, mes)
        
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
        _salvar_sessao_auto()
        print(f"A publicação '{titulo}' foi adicionada com sucesso!")
        retornar_ao_menu(1)
    elif opcao_escolhida == 3:
        mostrar_subtitulo("Removendo publicação")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação a ser removida: ")
        Publicacao.remover_publicacao(codigo)
        _salvar_sessao_auto()
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
        _salvar_sessao_auto()
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
    print("2. Adicionar ano")
    print("3. Remover ano")
    print("4. Voltar ao menu principal")
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
    elif opcao_escolhida == 3:
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
        retornar_ao_menu(2)
    elif opcao_escolhida == 4:
        print("\nVoltando ao menu principal...")
        time.sleep(1)
        retornar_ao_menu()
    else:
        print("Opção inválida. Tente novamente.")
        retornar_ao_menu(2)
        
def menu_meses():
    mostrar_subtitulo("Menu de Gerenciamento de Meses")
    print("1. Listar meses de um ano")
    print("2. Selecionar um mês para gerenciar publicações")
    print("3. Remover publicação de um mês")
    print("4. Voltar ao menu principal")
    try:
        limpar_buffer_teclado()
        opcao_escolhida = int(input("\nDigite o número da opção desejada: "))
    except ValueError:
        print("Erro! Digite uma opção válida.")       
        retornar_ao_menu(3)
        return
    if opcao_escolhida == 1:
        mostrar_subtitulo("Listando meses de um ano")
        Ano.listar_anos()
        if not Ano.anos:
            retornar_ao_menu(3)
            return
        time.sleep(0.5)
        limpar_buffer_teclado()
        input_ano = input("\nDigite o ano que deseja listar os meses: ")
        if input_ano == "":
            print("Erro! Digite um ano.")
            retornar_ao_menu(3)
            return
        time.sleep(0.5)
        for ano in Ano.anos:
            if ano.ano == input_ano:
                mostrar_subtitulo(f"Listando meses do ano {input_ano}")
                ano.listar_meses()
                break
        else:
            print(f"Nenhum ano '{input_ano}' encontrado.")
        retornar_ao_menu(3)
    elif opcao_escolhida == 2:
        mostrar_subtitulo("Selecionando mês para gerenciar publicações")
        Ano.listar_anos()
        if not Ano.anos:
            retornar_ao_menu(3)
            return
        time.sleep(0.5)
        limpar_buffer_teclado()
        input_ano = input("\nSelecione um ano para gerenciar seus meses: ")
        if input_ano == "":
            print("Erro! Digite um ano.")
            retornar_ao_menu(3)
            return
        time.sleep(0.5)
        for ano in Ano.anos:
            if ano.ano == input_ano:
                mostrar_subtitulo(f"Listando meses do ano {input_ano}")
                ano.listar_meses()
                break
        else:
            print(f"O ano '{input_ano}' não foi encontrado.")
            retornar_ao_menu(3)
            return
        try:
            limpar_buffer_teclado()
            input_mes = int(input("\nDigite o número do mês que deseja gerenciar (1-12): "))
            time.sleep(0.5)
        except ValueError:
            print("Erro! Digite um número válido para o mês.")
            retornar_ao_menu(3)
            return
        if not (1 <= input_mes <= 12):
            print("Erro! O número do mês deve estar entre 1 e 12.")
            retornar_ao_menu(3)
            return
        mes = ano.obter_mes(input_mes)
        if mes is None:
            print("Erro ao obter o mês. Tente novamente.")
            retornar_ao_menu(3)
            return
        menu_mes(ano, mes)
    elif opcao_escolhida == 3:
        print("Funcionalidade de remover mês ainda não implementada.")
        retornar_ao_menu(3)
    elif opcao_escolhida == 4:
        print("\nVoltando ao menu principal...")
        time.sleep(1)
        retornar_ao_menu()
    else:
        print("Opção inválida. Tente novamente.")
        retornar_ao_menu(3)

def menu_mes(ano, mes):
    mostrar_subtitulo(f"Gerenciando publicações do mês de {mes} do ano {ano.ano}")
    print("1. Listar publicações deste mês")
    print("2. Adicionar publicação a este mês")
    print("3. Remover publicação deste mês")
    print("4. Editar quantidade de uma publicação deste mês")
    print(f"5. Selecionar outro mês do ano {ano.ano}")
    print("6. Voltar ao menu de meses")
    print("7. Voltar ao menu principal")
    try:
        limpar_buffer_teclado()
        opcao_escolhida = int(input("\nDigite o número da opção desejada: "))
    except ValueError:
        print("Erro! Digite uma opção válida.")       
        retornar_ao_menu(4, ano, mes)
        return
    if opcao_escolhida == 1:
        mostrar_subtitulo(f"Listando publicações do mês de {mes} do ano {ano.ano}")
        mes.listar_publicacoes()
        retornar_ao_menu(4, ano, mes)
    elif opcao_escolhida == 2:
        mostrar_subtitulo(f"Adicionando publicação ao mês de {mes} do ano {ano.ano}")
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
            retornar_ao_menu(4, ano, mes)
            return
        nova_publicacao = Publicacao(titulo, codigo, quantidade)
        mes.adicionar_publicacao(nova_publicacao)
        _salvar_sessao_auto()
        print(f"A publicação '{titulo}' foi adicionada com sucesso ao mês de {mes} do ano {ano.ano}!")
        retornar_ao_menu(4, ano, mes)
    elif opcao_escolhida == 3:
        mostrar_subtitulo(f"Removendo publicação do mês de {mes} do ano {ano.ano}")
        limpar_buffer_teclado()
        codigo = input("Digite o código da publicação a ser removida: ")
        mes.remover_publicacao(codigo)
        _salvar_sessao_auto()
        retornar_ao_menu(4, ano, mes)
    elif opcao_escolhida == 4:
        mostrar_subtitulo(f"Editando quantidade de uma publicação de {mes} do ano {ano.ano}")
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
        mes.editar_quantidade_publicacao(codigo, nova_quantidade)
        _salvar_sessao_auto()
        retornar_ao_menu(4, ano, mes)
    elif opcao_escolhida == 5:
        mostrar_subtitulo("Selecionando mês para gerenciar publicações")
        input_ano = ano.ano
        for ano in Ano.anos:
            if ano.ano == input_ano:
                mostrar_subtitulo(f"Listando meses do ano {input_ano}")
                ano.listar_meses()
                break
        else:
            print(f"O ano '{input_ano}' não foi encontrado.")
            retornar_ao_menu(3)
            return
        try:
            limpar_buffer_teclado()
            input_mes = int(input("\nDigite o número do mês que deseja gerenciar (1-12): "))
            time.sleep(0.5)
        except ValueError:
            print("Erro! Digite um número válido para o mês.")
            retornar_ao_menu(3)
            return
        if not (1 <= input_mes <= 12):
            print("Erro! O número do mês deve estar entre 1 e 12.")
            retornar_ao_menu(3)
            return
        mes = ano.obter_mes(input_mes)
        if mes is None:
            print("Erro ao obter o mês. Tente novamente.")
            retornar_ao_menu(3)
            return
        menu_mes(ano, mes)
    elif opcao_escolhida == 6:
        print("Voltando ao menu de meses...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_meses()
    elif opcao_escolhida == 7:
        print("Voltando ao menu principal...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        tela_de_boas_vindas()
        menu_principal()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_mes(ano, mes)

def menu_principal():
    print("Escolha uma das opções abaixo:")
    print("1. Menu publicações:")
    print("2. Menu de Gerenciamento de Anos:")
    print("3. Menu de Gerenciamento de Meses:")
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
        menu_meses()
    elif opcao_escolhida == 4:
        _salvar_sessao_auto()
        print("\nTchau! ;)")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Opção inválida. Tente novamente.")
        retornar_ao_menu()

def __main__():
    configurar_base_de_dados()
    # carregar_sessao reconstrói Anos/Meses/Publicações em memória quando possível.
    carregar_sessao()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    tela_de_boas_vindas() 
    menu_principal()  
    
if __name__ == "__main__":
    __main__()


