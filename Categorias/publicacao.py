class Publicacao:
    def __init__(self, titulo, codigo, quantidade):
        self._titulo = titulo
        self._codigo = codigo
        self._quantidade = quantidade
        self.publicacoes = []
    
    @classmethod
    def criar_publicacao(cls):
        try:   
            titulo = input("Digite o título da publicação: ")
            codigo = input("Digite o código da publicação: ")
            quantidade = int(input("Digite a quantidade disponível: "))
            cls.publicacoes.append(cls(titulo, codigo, quantidade))
            return cls(titulo, codigo, quantidade)
        except ValueError:
            print("\nEntrada inválida. Certifique-se de inserir um número para a quantidade.")
            input("\nPressione Enter para continuar...")
        
        
