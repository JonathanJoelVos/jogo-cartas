from DAOs.dao import DAO
from models.carta import Carta


class CartaDAO(DAO):
    def __init__(self):
        super().__init__('cartas.pkl')

    def add(self, carta: Carta):
        if ((carta is not None)
            and isinstance(carta, Carta)
                and isinstance(carta.codigo, str)):
            super().add(carta.codigo, carta)

    def update(self, carta: Carta):
        if ((carta is not None)
            and isinstance(carta, Carta)
                and isinstance(carta.codigo, str)):
            super().update(carta.codigo, carta)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key: str):
        if (isinstance(key, str)):
            return super().remove(key)

    def get_all(self):
        return super().get_all()
