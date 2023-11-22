from DAOs.dao import DAO
from models.jogo import Jogo


class JogosDAO(DAO):
    def __init__(self):
        super().__init__('jogos.pkl')

    def add(self, jogo: Jogo):
        if ((jogo is not None)
            and isinstance(jogo, Jogo)
                and isinstance(jogo.codigo, int)):
            super().add(jogo.codigo, int)

    def update(self, jogo: Jogo):
        if ((jogo is not None)
                and isinstance(jogo, Jogo)
                and isinstance(jogo.codigo, int)):
            super().update(jogo.codigo, int)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(int)

    def remove(self, key: int):
        if (isinstance(key, int)):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
