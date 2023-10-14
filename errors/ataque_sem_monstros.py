class AtaqueSemMonstros(Exception):
    def __init__(self):
        super().__init__('Nenhum monstro foi selecionado para atacar!')
