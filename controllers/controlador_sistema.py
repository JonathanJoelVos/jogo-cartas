from views.tela_sistema import TelaSistema
from controllers.controlador_carta import ControladorCarta
from controllers.controlador_jogador import ControladorJogador
from controllers.controlador_jogo import ControladorJogo


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carta = ControladorCarta(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_jogo = ControladorJogo(self)

    @property
    def controlador_carta(self):
        return self.__controlador_carta

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_jogo(self):
        return self.__controlador_jogo

    def inicializa_sistema(self):
        self.abre_tela()

    def opcoes_cartas(self):
        self.__controlador_carta.abre_tela()

    def opcoes_jogadores(self):
        self.__controlador_jogador.abre_tela()

    def opcoes_jogo(self):
        self.__controlador_jogo.abre_tela()

    def rank_jogadores(self):
        self.__controlador_jogador.rank_jogadores()

    def sair(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.opcoes_jogadores,
            2: self.opcoes_jogo,
            3: self.rank_jogadores,
            4: self.opcoes_cartas,
            0: self.sair
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
