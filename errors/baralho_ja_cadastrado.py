class BaralhoJaCadastrado(Exception):
    def __init__(self):
        super().__init__('❗️❗️Este baralho já foi cadastrado❗️❗️')
