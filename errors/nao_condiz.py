class NaoCondiz(Exception):
    def __init__(self):
        super().__init__("O jogador não condiz com o atacante/defensor da rodada!")
