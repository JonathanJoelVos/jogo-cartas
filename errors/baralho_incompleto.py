class BaralhoIncompleto(Exception):
    def __init__(self):
        super().__init__("O baralho deve ter 20 cartas!")

