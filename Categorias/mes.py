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
    
    @classmethod
    def adicionar_publicacao(self, publicacao):
        self.publicacoes.append(publicacao)

    @classmethod
    def listar_publicacoes(cls):
        if not cls.publicacoes:
            print("Nenhuma publicação cadastrada neste mês.")
        else:
            print(f"{"Código".ljust(10)} | {"Título".ljust(30)} | Quantidade")
            for publicacao in cls.publicacoes:
                print(f"{publicacao.codigo.ljust(10)} | {publicacao._titulo.ljust(30)} | {publicacao._quantidade}")