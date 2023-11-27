class TipoDeCartaErrado(Exception):
    def __init__(self):
        super().__init__("Esse tipo de carta não pode ser jogada nesse momento! O turno será reiniciado")
