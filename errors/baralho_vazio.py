class BaralhoVazio(Exception):
    def __init__(self):
        super().__init__('Baralho vazio!')
