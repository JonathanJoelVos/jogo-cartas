class ManaInsuficiente(Exception):
    def __init__(self):
        super().__init__('Mana Insuficiente!')
