class TabuleiroCheio(Exception):
    def __init__(self):
        super().__init__("Tabuleiro cheio!")
