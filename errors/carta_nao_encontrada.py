class CartaNaoEncontrada(Exception):
    def __init__(self):
        super().__init__("Carta não foi encontrada!")
