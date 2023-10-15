class JogadorNaoExiste(Exception):
    def __init__(self):
        super().__init__('Esse Jogador não existe')
