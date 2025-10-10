class Mes:
    def __init__(self, num):
        self._num = num # Número do mês (1-12)
        self.publicacoes = []
    
    @property
    def num(self):
        return self._num
    
    def __str__(self):
        if self._num == 1:
            return "Janeiro"
        elif self._num == 2:
            return "Fevereiro"
        elif self._num == 3:
            return "Março"
        elif self._num == 4:
            return "Abril"
        elif self._num == 5:
            return "Maio"
        elif self._num == 6:    
            return "Junho"
        elif self._num == 7:
            return "Julho"
        elif self._num == 8:
            return "Agosto"
        elif self._num == 9:
            return "Setembro"
        elif self._num == 10:   
            return "Outubro"
        elif self._num == 11:
            return "Novembro"
        elif self._num == 12:
            return "Dezembro"
        else:
            return "Mês inválido"
    
    def adicionar_publicacao(self, publicacao):
        self.publicacoes.append(publicacao)
    
    def remover_publicacao(self, codigo):
        for publicacao in self.publicacoes:
            if publicacao.codigo == codigo.lower():
                confirmacao = input(f"Tem certeza que deseja remover a publicação '{publicacao._titulo}'? (s/N): ")
                if confirmacao.lower() == 's':
                    self.publicacoes.remove(publicacao)
                    print(f"A publicação com o código {codigo} foi removida com sucesso.")
                    return
                else:
                    print("Remoção cancelada.")
                    return
            elif codigo == "":
                print("Erro! Digite um código.")
                return
        else:
            print(f"Nenhuma publicação encontrada com o código {codigo}.")
            return

    def para_dicionario(self):
        for publicacao in self.publicacoes:
            publicacao.para_dicionario()
        return

    def listar_publicacoes(self):
        if not self.publicacoes:
            print("Nenhuma publicação cadastrada neste mês.")
        else:
            print(f"{"Código".ljust(10)} | {"Título".ljust(30)} | Quantidade")
            for publicacao in self.publicacoes:
                print(f"{publicacao.codigo.ljust(10)} | {publicacao._titulo.ljust(30)} | {publicacao._quantidade}")
    
    def editar_quantidade_publicacao(self, codigo, nova_quantidade):
        for publicacao in self.publicacoes:
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
 