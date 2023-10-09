from baralho import Baralho
from errors.baralho_nao_existe import BaralhoNaoExiste
from carta import Carta


class Jogador():
    def __init__(
        self,
        nome: str,
    ):
        self.__nome = nome
        self.__baralhos: list[Baralho] = []
        self.__partidas_jogadas = 0
        self.__vitorias = 0
        self.__derrotas = 0
        self.__pontos = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def baralhos(self):
        return self.__baralhos

    @baralhos.setter
    def baralhos(self, baralhos):
        self.__baralhos = baralhos

    @property
    def partidas_jogadas(self):
        return self.__partidas_jogadas

    @partidas_jogadas.setter
    def partidas_jogadas(self, partidas_jogadas):
        self.__partidas_jogadas = partidas_jogadas

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, vitorias):
        self.__vitorias = vitorias

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, derrotas):
        self.__derrotas = derrotas

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    def cria_baralho(self, nome_baralho: str):
        baralho = Baralho([], nome_baralho)
        self.__baralhos.append(baralho)

    def remove_baralho(self, nome_baralho: str):
        for b in self.__baralhos:
            if b.nome == nome_baralho:
                self.__baralhos.remove(b)
                return
        raise BaralhoNaoExiste()

    def add_carta_ao_baralho(self, nome_baralho, carta: Carta):
        for b in self.__baralhos:
            if b.nome == nome_baralho:
                b.add_carta(carta)
                return
        raise BaralhoNaoExiste()

    def remover_carta_do_baralho(self, nome_baralho, codigo_carta):
        for b in self.__baralhos:
            if b.nome == nome_baralho:
                b.del_carta(codigo_carta)
                return
        raise BaralhoNaoExiste()
