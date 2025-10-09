from Categorias.mes import Mes
class Ano:
    anos = []
    def __init__(self, ano):
        self._ano = ano
        self._meses = [Mes(i) for i in range(1, 13)]  # Cria 12 meses para o ano
        Ano.anos.append(self)

    @property
    def ano(self):
        return self._ano
    @classmethod
    def listar_anos(cls):
        if not cls.anos:
            print("Nenhum ano cadastrado.")
            return
        else:
            i = 1
            print("Anos cadastrados:\n")
            for ano in cls.anos:
                print(f"{i}. {ano.ano}")
                i += 1
    
    def listar_meses(self):
        if not self._meses:
            print(f"Nenhum mês cadastrado para o ano {self.ano}.\n")
            return
        else:
            i = 1
            for mes in self._meses:
                print(f"{i}. {mes}")
                i += 1

    def obter_mes(self, num):
        if 1 <= num <= 12:
            return self._meses[num - 1]
        else:
            print("Número do mês inválido. Deve ser entre 1 e 12.")
            return None
    
    @classmethod
    def remover_ano(cls, obj_ano):
        for obj_ano in cls.anos:
            if obj_ano.ano == obj_ano:
                confirmacao = input(f"Você tem certeza que deseja remover o ano '{obj_ano}' e seus meses, junto de suas publicações? Digite [confirmar] para confirmar a exclusão: ")
                if confirmacao.lower() == 'confirmar':
                    cls.anos.remove(obj_ano)
                    print(f"O ano {obj_ano} foi removido com sucesso.")
                    return
                else:
                    print("Remoção cancelada.")
                    return
            elif obj_ano == "":
                print("Erro! Digite um ano.")
                return