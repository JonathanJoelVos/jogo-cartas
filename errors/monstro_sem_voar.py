class MonstroSemVoar(Exception):
    def __init__(self):
        super().__init__("Esse monstro não pode bloquear um monstro voador!")