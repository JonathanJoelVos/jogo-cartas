class AtaqueSemMonstros(Exception):
    def __init__(self):
        super().__init__('Não pode iniciar um ataque sem monstros.')
