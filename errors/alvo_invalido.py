class AlvoInvalido(Exception):
    def __init__(self):
        super().__init__('Alvo inválido!')
