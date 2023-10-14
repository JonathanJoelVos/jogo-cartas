from carta import Carta


class Feitico(Carta):
    # - modificacao: "aumentar" | "diminuir"
    # - atributo_modificado: "vida" | "ataque"
    # - valor: int

    def __init__(
        self,
        nome: str,
        custo_mana: int,
        codigo: str,
        modificacao: str,
        atributo_modificado: str,
        valor: int
    ):
        super().__init__(custo_mana, codigo)
        self.__modificacao = modificacao
        self.__atributo_modificado = atributo_modificado
        self.__valor = valor
        self.__nome = nome

    @property
    def modificacao(self):
        return self.__modificacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @modificacao.setter
    def modificacao(self, modificacao):
        self.__modificacao = modificacao

    @property
    def atributo_modificado(self):
        return self.__atributo_modificado

    @atributo_modificado.setter
    def atributo_modificado(self, atributo_modificado):
        self.__atributo_modificado = atributo_modificado

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
