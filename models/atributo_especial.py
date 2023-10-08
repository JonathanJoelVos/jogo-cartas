class AtributoEspecial:
    def __init__(self, efeito: str):
        self.__efeito = efeito

    @property
    def efeito(self):
        return self.__efeito

    @efeito.setter
    def efeito(self, efeito):
        self.__efeito = efeito

