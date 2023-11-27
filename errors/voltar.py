class Voltar(Exception):
    def __init__(self):
        super().__init__("O Turno será reiniciado.")
