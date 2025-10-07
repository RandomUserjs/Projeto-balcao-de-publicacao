class Publicacao:
    publicacoes = []
    def __init__(self, titulo, codigo, quantidade):
        self._titulo = titulo.title()
        self._codigo = codigo
        self._quantidade = quantidade
        Publicacao.publicacoes.append(self)
    
    @property
    def titulo(self):
        return self._titulo
    @property
    def codigo(self):
        return self._codigo.lower()
    @property
    def quantidade(self):
        return self._quantidade

    @classmethod
    def listar_publicacoes(cls):
        if not cls.publicacoes:
            print("Nenhuma publicação cadastrada.")
        else:
            print(f"{"Código".ljust(10)} | {"Título".ljust(30)} | Quantidade")
            for publicacao in cls.publicacoes:
                print(f"{publicacao.codigo.ljust(10)} | {publicacao._titulo.ljust(30)} | {publicacao._quantidade}")
    
    @classmethod
    def remover_publicacao(cls, codigo):
        for publicacao in cls.publicacoes:
            if publicacao.codigo == codigo.lower():
                confirmacao = input(f"Tem certeza que deseja remover a publicação '{publicacao._titulo}'? (s/N): ")
                if confirmacao.lower() == 's':
                    cls.publicacoes.remove(publicacao)
                    print(f"A publicação com o código {codigo} foi removida com sucesso.")
                    return
                else:
                    print("Remoção cancelada.")
                    return
            elif codigo == "":
                print("Erro! Digite um código.")
                return
            else:
                print(f"Nenhuma publicação foi encontrada com o código '{codigo}'.")
                
    @classmethod
    def editar_quantidade(cls, codigo, nova_quantidade):
        for publicacao in cls.publicacoes:
            if publicacao.codigo == codigo.lower():
                quantidade_antiga = publicacao.quantidade
                confirmacao = input(f"Tem certeza que deseja alterar a quantidade da publicação '{publicacao.titulo}' de {quantidade_antiga} para {nova_quantidade}? (s/N): ")
                if confirmacao.lower() != 's':
                    print("Edição cancelada.")
                    return
                if nova_quantidade < 0:
                    print("Erro! A quantidade não pode ser negativa.")
                    return
                else:
                    publicacao._quantidade = nova_quantidade
                    print(f"A quantidade da publicação '{publicacao.titulo}' foi atualizada de {quantidade_antiga} para {nova_quantidade}.")
                    return
            else:
                print(f"Nenhuma publicação foi encontrada com o código '{codigo}'.")
    
       
