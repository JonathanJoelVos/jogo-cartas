class BaralhoNaoExiste(Exception):
    def __init__(self):
        super().__init__("Baralho não existe")
