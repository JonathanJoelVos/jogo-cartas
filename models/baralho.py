from carta import Carta
from errors.carta_ja_existe import CartaJaExiste
from errors.carta_nao_existe import CartaNaoExiste


class Baralho():
    def __init__(self, cartas: list[Carta], nome: str):
        self.__cartas = cartas
        self.__nome = nome

    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, cartas):
        self.__cartas = cartas

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def add_carta(self, carta: Carta):
        for c in self.__cartas:
            if c.codigo == carta.codigo:
                raise CartaJaExiste()
        self.__cartas.append(carta)

    def del_carta(self, codigo: int):
        for c in self.__cartas:
            if c.codigo == codigo:
                self.__cartas.remove(c)
                return
        raise CartaNaoExiste()
