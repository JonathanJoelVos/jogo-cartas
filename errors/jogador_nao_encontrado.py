class JogadorNaoEncontrado(Exception):
    def __init__(self):
        super().__init__('❗️❗️Jogador não encontrado❗️❗️')
