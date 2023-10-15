from views.tela_carta import TelaCarta
from models.carta import Carta
from models.monstro import Monstro
from models.feitico import Feitico
from models.atributo_especial import AtributoEspecial


class ControladorCarta():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_carta = TelaCarta()
        self.__cartas: list[Carta] = [
            Monstro('Teemo', 1, 'Teemo', 1, 10, [AtributoEspecial('ataque')]),
            Monstro('Poppy', 2, 'Poppy', 2, 10, [AtributoEspecial('ataque')]),
            Monstro('Fiora', 2, 'Fiora', 10, 10, [AtributoEspecial('ataque')]),
            Feitico('teste', 4, '4', 'aumentar', 'vida', 1),
            Feitico('teste', 5, '5', 'aumentar', 'ataque', 1),
            Feitico('teste', 6, '6', 'diminuir', 'vida', 1),
            Feitico('teste', 7, '7', 'diminuir', 'ataque', 1),
        ]

    @property
    def cartas(self):
        return self.__cartas

    def pegar_carta_pelo_codigo(self, codigo):
        for carta in self.__cartas:
            if (carta.codigo == codigo):
                return carta
        return None

    def seleciona_carta(self):
        codigo = self.__tela_carta.seleciona_carta()
        carta = self.pegar_carta_pelo_codigo(codigo)
        if (carta is not None):
            return carta
        else:
            self.__tela_carta.mostra_msg('Carta não encontrada')
            return None

    def incluir_carta(self):
        dados_carta = self.__tela_carta.pega_dados_carta()
        if (dados_carta['codigo'] == 0):
            self.__tela_carta.mostra_msg('Código inválido')
            return
        carta = self.pegar_carta_pelo_codigo(dados_carta['codigo'])
        if (carta is None):
            if (dados_carta['tipo'] == 'Monstro'):
                self.__cartas.append(
                    Monstro(
                        dados_carta['custo_mana'],
                        dados_carta['codigo'],
                        dados_carta['ataque'],
                        dados_carta['vida'],
                        dados_carta['atributos']
                    )
                )
            else:
                self.__cartas.append(
                    Feitico(
                        dados_carta['custo_mana'],
                        dados_carta['codigo'],
                        dados_carta['modificacao'],
                        dados_carta['atributo_modificado'],
                        dados_carta['valor']
                    )
                )
        else:
            self.__tela_carta.mostra_msg('Carta já existente')

    def lista_carta(self, carta: Carta):
        if (isinstance(carta, Monstro)):
            self.__tela_carta.mostra_monstro({
                'nome': carta.nome,
                'custo_mana': carta.custo_mana,
                'codigo': carta.codigo,
                'ataque': carta.ataque,
                'vida': carta.vida,
                'atributos': carta.atributos
            })
        elif (isinstance(carta, Feitico)):
            self.__tela_carta.mostra_feitico({
                'nome': carta.nome,
                'custo_mana': carta.custo_mana,
                'codigo': carta.codigo,
                'modificacao': carta.modificacao,
                'atributo_modificado': carta.atributo_modificado,
                'valor': carta.valor
            })

    def lista_cartas(self):
        for carta in self.__cartas:
            self.lista_carta(carta)

    def exclui_carta(self):
        self.lista_cartas()
        carta = self.seleciona_carta()
        if (carta is not None):
            self.__cartas.remove(carta)

    def altera_carta(self):
        self.lista_cartas()
        carta = self.seleciona_carta()
        if (carta is not None):
            carta_eh_mostro = isinstance(carta, Monstro)
            carta_eh_feitico = isinstance(carta, Feitico)
            if (carta_eh_mostro):
                dados_monstro = self.__tela_carta.pega_dados_monstro()
                carta.codigo = dados_monstro['codigo']
                carta.custo_mana = dados_monstro['custo_mana']
                carta.ataque = dados_monstro['ataque']
                carta.atributos = dados_monstro['atributos']
            elif (carta_eh_feitico):
                dados_feitico = self.__tela_carta.pega_dados_feitico()
                carta.codigo = dados_feitico['codigo']
                carta.custo_mana = dados_feitico['custo_mana']
                carta.atributo_modificado = \
                    dados_feitico['atributo_modificado']
                carta.modificacao = dados_feitico['modificacao']
                carta.valor = dados_feitico['valor']

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_carta,
            2: self.lista_cartas,
            3: self.exclui_carta,
            4: self.altera_carta,
            0: self.retornar,
        }

        while True:
            lista_opcoes[self.__tela_carta.tela_opcoes()]()
