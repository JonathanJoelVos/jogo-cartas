class OpcaoInvalida(Exception):
    def __init__(self) -> None:
        super().__init__('❗️❗️Digite uma opção válida❗️❗️')
