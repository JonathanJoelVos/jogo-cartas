class CartaJaExiste(Exception):
    def __init__(self):
        super().__init__("Carta já existe no baralho!")
