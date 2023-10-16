class MesmoJogador(Exception):
    def __init__(self):
        super().__init__('Esse jogador já foi selecionado!')
