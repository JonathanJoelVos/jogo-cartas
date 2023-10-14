class TipoDeCartaErrado(Exception):
    def __init__(self):
        super().__init__("Essa carta não pode ser jogada nesse momento!")
