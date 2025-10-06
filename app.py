import os
from Categorias.publicacao import Publicacao
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

def retornar_ao_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    tela_de_boas_vindas()
    escolha_de_opçoes()
    
def escolha_de_opçoes():
    print("Escolha uma das opções abaixo:")
    print("1. Listar publicações:")
    print("2. Adicionar publicação:")
    print("3. Remover publicação:")
    print("4. Sair")
    opcao_escolhida = int(input("Digite o número da opção desejada: "))
    if opcao_escolhida == 1:
        print("Listando publicações...")
    elif opcao_escolhida == 2:
        print("Adicionando publicação...")
        Publicacao.criar_publicacao()
        retornar_ao_menu()
    elif opcao_escolhida == 3:
        print("Removendo publicação...")
    elif opcao_escolhida == 4:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
        escolha_de_opçoes()

def __main__():
    tela_de_boas_vindas() 
    escolha_de_opçoes()  
    
if __name__ == "__main__":
    __main__()


