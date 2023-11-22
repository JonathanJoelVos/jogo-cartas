class CartaJaExiste(Exception):
    def __init__(self):
        super().__init__("Código da carta já existe!")
