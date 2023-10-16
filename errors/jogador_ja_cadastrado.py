class JogadorJaCadastrado(Exception):
    def __init__(self):
        super().__init__('❗️❗️Este jogador já foi cadastrado❗️❗️')
