from views.tela_carta import TelaCarta
from models.carta import Carta
from models.monstro import Monstro
from models.feitico import Feitico
from models.atributo_especial import AtributoEspecial
from errors.carta_ja_existe import CartaJaExiste
from errors.carta_nao_encontrada import CartaNaoEncontrada
from errors.opcao_invalida import OpcaoInvalida
from DAOs.cartas_dao import CartaDAO


class ControladorCarta():
    def __init__(self, controlador_sistema):
        self.__cartas_dao = CartaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_carta = TelaCarta()

    def pegar_carta_pelo_codigo(self, codigo):
        for carta in self.__cartas_dao.get_all():
            if (carta.codigo == codigo):
                return carta
        return None

    def seleciona_carta(self):
        codigo = self.__tela_carta.seleciona_carta()
        carta = self.pegar_carta_pelo_codigo(codigo)
        if (carta is not None):
            return carta
        else:
            raise CartaNaoEncontrada()

    def incluir_carta(self):
        dados_carta = self.__tela_carta.pega_dados_iniciais_carta()
        print(dados_carta)
        if (dados_carta['codigo'] == 0):
            self.__tela_carta.mostra_msg('Código inválido')
            return
        carta = self.pegar_carta_pelo_codigo(dados_carta['codigo'])
        if (carta is None):
            if (dados_carta['tipo'] == 'Monstro'):
                self.__cartas_dao.add(
                    Monstro(
                        dados_carta['nome'],
                        dados_carta['custo_mana'],
                        dados_carta['codigo'],
                        dados_carta['ataque'],
                        dados_carta['vida'],
                        [AtributoEspecial(dados_carta['atributos'])]
                    )
                )
            else:
                self.__cartas_dao.add(
                    Feitico(
                        dados_carta['nome'],
                        dados_carta['custo_mana'],
                        dados_carta['codigo'],
                        dados_carta['modificacao'],
                        dados_carta['atributo_modificado'],
                        dados_carta['valor']
                    )
                )
        else:
            raise CartaJaExiste()

    def lista_carta(self, carta: Carta): #controlador de jogo usa
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
        dados = []
        for carta in self.__cartas_dao.get_all():
            if isinstance(carta, Monstro):
                dados.append('Monstro')
                dados.append(carta.nome)
                dados.append(carta.codigo)
                dados.append(carta.custo_mana)
                dados.append(carta.ataque)
                dados.append(carta.vida)
                if carta.atributos:
                    dados.append(carta.atributos[0].efeito)
                else:
                    dados.append('')
            else:
                dados.append('Feitiço')
                dados.append(carta.nome)
                dados.append(carta.codigo)
                dados.append(carta.custo_mana)
                dados.append(carta.modificacao)
                dados.append(carta.atributo_modificado)
                dados.append(carta.valor)

        self.__tela_carta.mostra_carta(dados)

    def exclui_carta(self):
        self.lista_cartas()
        carta = self.seleciona_carta()
        self.__cartas_dao.remove(carta.codigo)

    def altera_carta(self):
        self.lista_cartas()
        carta = self.seleciona_carta()
        carta_eh_mostro = isinstance(carta, Monstro)
        carta_eh_feitico = isinstance(carta, Feitico)
        if (carta_eh_mostro):
            dados_monstro = self.__tela_carta.pega_dados_monstro()
            carta.custo_mana = dados_monstro['custo_mana']
            carta.ataque = dados_monstro['ataque']
            carta.atributos = [AtributoEspecial(dados_monstro['atributos'])]
            carta.nome = dados_monstro['nome']
            carta.vida = dados_monstro['vida']
        elif (carta_eh_feitico):
            dados_feitico = self.__tela_carta.pega_dados_feitico()
            carta.custo_mana = dados_feitico['custo_mana']
            carta.atributo_modificado = dados_feitico['atributo_modificado']
            carta.modificacao = dados_feitico['modificacao']
            carta.valor = dados_feitico['valor']
            carta.nome = dados_feitico['nome']
        self.__cartas_dao.update(carta)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        valores_possiveis = [1, 2, 3, 4, 0]
        lista_opcoes = {
            1: self.incluir_carta,
            2: self.lista_cartas,
            3: self.exclui_carta,
            4: self.altera_carta,
            0: self.retornar,
        }

        while True:
            try:
                opcao_escolhida = self.__tela_carta.tela_opcoes()
                if (opcao_escolhida not in valores_possiveis):
                    raise OpcaoInvalida()
                lista_opcoes[opcao_escolhida]()
            except CartaJaExiste as e:
                self.__tela_carta.mostra_msg(e)
            except CartaNaoEncontrada as e:
                self.__tela_carta.mostra_msg(e)
            except OpcaoInvalida as e:
                self.__tela_carta.mostra_msg(e)