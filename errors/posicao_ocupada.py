class PosicaoOcupada(Exception):
    def __init__(self):
        super().__init__('Posição já ocupada!')
