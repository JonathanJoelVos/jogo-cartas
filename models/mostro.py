from carta import Carta
from atributo_especial import AtributoEspecial


class Mostro(Carta):

    def __init__(
        self,
        custo_mana: int,
        codigo: str,
        ataque: int,
        vida: int,
        atributos: list[AtributoEspecial]
    ):
        super().__init__(custo_mana, codigo)
        self.__ataque = ataque
        self.__vida = vida
        self.__atributos = atributos

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, ataque):
        self.__ataque = ataque

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos):
        self.__atributos = atributos

    def diminuir_vida(self, quantidade: int):
        self.__vida -= quantidade

    def aumentar_vida(self, quantidade: int):
        self.__vida += quantidade
