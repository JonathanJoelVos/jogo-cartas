class Voltar(Exception):
    def __init__(self):
        super().__init__("Voltando para tela de opções")
