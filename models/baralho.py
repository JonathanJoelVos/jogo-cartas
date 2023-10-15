from models.carta import Carta
from errors.carta_nao_existe import CartaNaoExiste
from errors.numero_de_copias_excedidos import NumeroDeCopiasExcedidas


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
        if (len(self.__cartas) == 20):
            raise NumeroDeCopiasExcedidas()
        count_copias = 0
        for c in self.__cartas:
            if c.codigo == carta.codigo:
                count_copias += 1
                if count_copias == 3:
                    raise NumeroDeCopiasExcedidas()
        self.__cartas.append(carta)

    def del_carta(self, codigo: int):
        for c in self.__cartas:
            if c.codigo == codigo:
                self.__cartas.remove(c)
                return
        raise CartaNaoExiste()
