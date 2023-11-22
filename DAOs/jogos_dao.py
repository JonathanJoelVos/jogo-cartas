from DAOs.dao import DAO
from models.jogo import Jogo


class JogosDAO(DAO):
    def __init__(self):
        super().__init__('jogos.pkl')

    def add(self, jogo: Jogo):
        if jogo is not None and isinstance(jogo, Jogo) and isinstance(jogo.codigo, int):
            super().add(jogo.codigo, jogo)

    def update(self, jogo: Jogo):
        if jogo is not None and isinstance(jogo, Jogo) and isinstance(jogo.codigo, int):
            super().update(jogo.codigo, jogo)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
