class NumeroDeCopiasExcedidas(Exception):
    def __init__(self):
        super().__init__('Número de cópias excedidas!')
