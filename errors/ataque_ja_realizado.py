class AtaqueJaRealizado(Exception):
    def __init__(self):
        super().__init__("Já houve uma batalha nessa rodada!")
