class ManaInsuficiente(Exception):
    def __init__(self):
        super().__init__('Mana Insuficiente. O turno será reiniciado')
