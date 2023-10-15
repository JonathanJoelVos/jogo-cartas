class LimiteDeCartaExcedido(Exception):
    def __init__(self):
        super().__init__('Limite de cartas excedido!')
