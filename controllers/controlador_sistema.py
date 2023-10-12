from views.tela_sistema import TelaSistema
from controllers.controlador_carta import ControladorCarta


class ControladorSistema():
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_teste = ControladorCarta(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def teste(self):
        self.__controlador_teste.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.teste,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
