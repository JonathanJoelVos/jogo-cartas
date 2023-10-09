class CartaNaoExiste(Exception):
    def __init__(self):
        super().__init__('Carta não existe')
