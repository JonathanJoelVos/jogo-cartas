from views.tela_sistema import TelaSistema
from controllers.controlador_carta import ControladorCarta
from controllers.controlador_jogador import ControladorJogador


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carta = ControladorCarta(self)
        self.__controlador_jogador = ControladorJogador(self)

    @property
    def controlador_carta(self):
        return self.__controlador_carta

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    def inicializa_sistema(self):
        self.abre_tela()

    def opcoes_cartas(self):
        self.__controlador_carta.abre_tela()

    def opcoes_jogadores(self):
        self.__controlador_jogador.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.opcoes_cartas,
            2: self.opcoes_jogadores,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
