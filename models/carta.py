from abc import ABC, abstractmethod


class Carta(ABC):
    @abstractmethod
    def __init__(self, custo_mana: int, codigo: str):
        self.__custo_mana = custo_mana
        self.__codigo = codigo

    @property
    def custo_mana(self):
        return self.__custo_mana

    @custo_mana.setter
    def custo_mana(self, custo_mana):
        self.__custo_mana = custo_mana

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
