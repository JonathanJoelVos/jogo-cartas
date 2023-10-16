from views.tela_jogador import TelaJogador
from models.jogador import Jogador
from models.baralho import Baralho
from models.monstro import Monstro
from models.feitico import Feitico
from models.atributo_especial import AtributoEspecial


class ControladorJogador():
    def __init__(self, controlador_sistema):
        # excluir jogadores
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__jogadores: list[Jogador] = [
            Jogador('LEONARDO', [
                Baralho([
                    Monstro('Poppy', 10, '1', 2, 10, []),
                    Feitico('Bola de Fogo', 10, '1', 'diminuir', 'vida', 10),
                    Feitico("Chama do Guerreiro", 3, "2",
                            "aumentar", "ataque", 3),
                    Feitico("Raiva Implacável", 4, "3",
                            "aumentar", "ataque", 4),
                    Feitico("Fúria Divina", 5, "4", "aumentar", "ataque", 5),
                    Feitico("Vitalidade Fortificada", 2,
                            "5", "aumentar", "vida", 2),
                    Feitico("Cura Abençoada", 3, "6", "aumentar", "vida", 3),
                    Feitico("Escudo Celestial", 4, "7", "aumentar", "vida", 4),
                    Feitico("Resistência Infinita", 5,
                            "8", "aumentar", "vida", 5),

                    Feitico("Maldição das Sombras", 2,
                            "9", "diminuir", "ataque", 2),
                    Feitico("Veneno Traiçoeiro", 3, "10",
                            "diminuir", "vida", 3),
                    Monstro("Lendário Grifo", 8, "4", 7, 8, [
                            AtributoEspecial("Sobrepujar"),
                            AtributoEspecial("Voar")]),


                    Monstro("Gigante Sombrio", 5, "5", 6, 6, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Touro Selvagem", 4, "6", 5, 7, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Colosso Furioso", 8, "7", 7, 9, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Campeão de Ferro", 3, "8", 3, 4,
                            [AtributoEspecial("Sobrepujar")]),


                    Monstro("Wyvern Veloz", 3, "9", 2, 4,
                            [AtributoEspecial("Voar")]),


                    Monstro("Sombra Celestial", 4, "10", 3,
                            5, [AtributoEspecial("Voar")]),


                    Monstro("Gavião de Aço", 2, "11", 2,
                            3, [AtributoEspecial("Voar")]),


                    Monstro("Dragão das Tempestades", 5, "12",
                            4, 6, [AtributoEspecial("Voar")]),
                ], 'b1'),
            ]),
            Jogador('JONATHAN', [
                Baralho([
                    Monstro('Poppy', 10, '1', 2, 10, []),
                    Feitico('Bola de Fogo', 10, '1', 'diminuir', 'vida', 10),
                    Feitico("Chama do Guerreiro", 3, "2",
                            "aumentar", "ataque", 3),
                    Feitico("Raiva Implacável", 4, "3",
                            "aumentar", "ataque", 4),
                    Feitico("Fúria Divina", 5, "4", "aumentar", "ataque", 5),
                    Feitico("Vitalidade Fortificada", 2,
                            "5", "aumentar", "vida", 2),
                    Feitico("Cura Abençoada", 3, "6", "aumentar", "vida", 3),
                    Feitico("Escudo Celestial", 4, "7", "aumentar", "vida", 4),
                    Feitico("Resistência Infinita", 5,
                            "8", "aumentar", "vida", 5),

                    Feitico("Maldição das Sombras", 2,
                            "9", "diminuir", "ataque", 2),
                    Feitico("Veneno Traiçoeiro", 4, "10",
                            "diminuir", "vida", 4),
                    Monstro("Lendário Grifo", 8, "4", 7, 8, [
                            AtributoEspecial("Sobrepujar"),
                            AtributoEspecial("Voar")]),


                    Monstro("Gigante Sombrio", 5, "5", 6, 6, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Touro Selvagem", 4, "6", 5, 7, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Colosso Furioso", 8, "7", 7, 9, [
                            AtributoEspecial("Sobrepujar")]),


                    Monstro("Campeão de Ferro", 3, "8", 3, 4,
                            [AtributoEspecial("Sobrepujar")]),


                    Monstro("Wyvern Veloz", 3, "9", 2, 4,
                            [AtributoEspecial("Voar")]),


                    Monstro("Sombra Celestial", 4, "10", 3,
                            5, [AtributoEspecial("Voar")]),


                    Monstro("Gavião de Aço", 2, "11", 2,
                            3, [AtributoEspecial("Voar")]),


                    Monstro("Dragão das Tempestades", 5, "12",
                            4, 6, [AtributoEspecial("Voar")]),
                ], 'b2'),
            ]),
        ]

    @ property
    def jogadores(self):
        return self.__jogadores

    def pega_jogador_pelo_nome(self, nome):
        for jogador in self.__jogadores:
            if (jogador.nome == nome):
                return jogador
        return None

    def seleciona_jogador(self):
        self.lista_jogadores()
        nome_jogador = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_pelo_nome(nome_jogador)
        if (jogador is not None):
            return jogador
        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')
            return None

    def lista_jogadores(self):
        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_jogador({
                'nome': jogador.nome,
                'partidas_jogadas': jogador.partidas_jogadas,
                'vitorias': jogador.vitorias,
                'derrotas': jogador.derrotas,
                'pontos': jogador.pontos
            })

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.pega_dados_jogador()
        jogador = self.pega_jogador_pelo_nome(dados_jogador['nome'])
        if (jogador is None):
            jogador = Jogador(
                nome=dados_jogador['nome']
            )
            self.__jogadores.append(jogador)
            self.__tela_jogador.mostra_msg('Jogador cadastrado com sucesso')
        else:
            self.__tela_jogador.mostra_msg('Jogador já cadastrado')

    def exclui_jogador(self):
        jogador = self.seleciona_jogador()
        if (jogador is not None):
            self.__jogadores.remove(jogador)
            self.__tela_jogador.mostra_msg('Jogador removido com sucesso')

    def altera_jogador(self):
        jogador = self.seleciona_jogador()
        if (jogador is not None):
            dados_jogador = self.__tela_jogador.pega_dados_jogador()
            jogador.nome = dados_jogador['nome']
            self.__tela_jogador.mostra_msg('Jogador alterado com sucesso')

    def pega_baralho_jogador_pelo_nome(self, jogador: Jogador, nome):
        for baralho in jogador.baralhos:
            if (baralho.nome == nome):
                return baralho
        return None

    def seleciona_baralho_do_jogador(self, jogador: Jogador):
        nome_baralho = self.__tela_jogador.seleciona_baralho()
        baralho = self.pega_baralho_jogador_pelo_nome(jogador, nome_baralho)
        if (baralho is not None):
            return baralho
        else:
            self.__tela_jogador.mostra_msg('Baralho não encontrado')
            return None

    def lista_baralhos_jogador(self, jogador: Jogador):
        if (jogador is not None):
            for baralho in jogador.baralhos:
                self.__tela_jogador.mostra_baralho({
                    'nome': baralho.nome,
                    'cartas': baralho.cartas
                })

    def incluir_baralho_jogador(self, jogador: Jogador):
        if (jogador is not None):
            dados_baralho = self.__tela_jogador.pega_dados_baralho()
            if (self
                    .pega_baralho_jogador_pelo_nome(jogador,
                                                    dados_baralho['nome'])
                    is None):
                jogador.cria_baralho(dados_baralho['nome'])
                self.__tela_jogador.mostra_msg(
                    'Baralho cadastrado com sucesso')
            else:
                self.__tela_jogador.mostra_msg('Baralho já cadastrado')

    def alterar_baralho_jogador(self, jogador: Jogador):
        if (jogador is not None):
            self.lista_baralhos_jogador(jogador)
            baralho = self.seleciona_baralho_do_jogador(jogador)
            if (baralho is not None):
                dados_baralho = self.__tela_jogador.pega_dados_baralho()
                jogador.altera_baralho(baralho.nome, dados_baralho['nome'])
                self.__tela_jogador.mostra_msg('Baralho alterado com sucesso')

    def exclui_baralho_jogador(self, jogador: Jogador):
        if (jogador is not None):
            self.lista_baralhos_jogador(jogador)
            baralho = self.seleciona_baralho_do_jogador(jogador)
            if (baralho is not None):
                jogador.remove_baralho(baralho.nome)
                self.__tela_jogador.mostra_msg('Baralho removido com sucesso')

    def add_carta_ao_baralho_jogador(self, jogador: Jogador):
        try:
            self.lista_baralhos_jogador(jogador)
            baralho = self.seleciona_baralho_do_jogador(jogador)
            if (jogador is not None and baralho is not None):
                self.__tela_jogador.mostra_msg(
                    'Selecione a carta (0 para sair):')
                while (True):
                    self.__controlador_sistema.controlador_carta.lista_cartas()
                    carta = self.__controlador_sistema.controlador_carta \
                        .seleciona_carta()
                    if (carta is not None):
                        jogador.add_carta_ao_baralho(baralho.nome, carta)
                        self.__tela_jogador.mostra_msg(
                            'Carta adicionada com sucesso')
                    else:
                        break
        except Exception:
            self.__tela_jogador.mostra_msg('Erro ao adicionar carta')

    def lista_cartas_do_baralho(self, baralho):
        if (len(baralho.cartas) == 0):
            return self.__tela_jogador.mostra_msg('Baralho vazio')
        for carta in baralho.cartas:
            self.__controlador_sistema.controlador_carta.lista_carta(carta)

    def remover_carta_do_baralho_jogador(self, jogador: Jogador):
        self.lista_baralhos_jogador(jogador)
        baralho = self.seleciona_baralho_do_jogador(jogador)
        if (jogador is not None):
            self.lista_cartas_do_baralho(baralho)
            carta = self.__controlador_sistema.controlador_carta \
                .seleciona_carta()
            if (carta is not None):
                jogador.remover_carta_do_baralho(baralho.nome, carta.codigo)
                self.__tela_jogador.mostra_msg('Carta removida com sucesso')

    def listar_cartas_do_baralho_jogador(self, jogador: Jogador):
        self.lista_baralhos_jogador(jogador)
        baralho = self.seleciona_baralho_do_jogador(jogador)
        if (jogador is not None and baralho is not None):
            self.__tela_jogador.mostra_baralho({
                'nome': baralho.nome
            })
            self.lista_cartas_do_baralho(baralho)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def voltar(self):
        self.abre_tela()

    def opcoes_baralho(self):
        jogador = self.seleciona_jogador()

        lista_opcoes = {
            0: self.voltar,
            1: self.lista_baralhos_jogador,
            2: self.incluir_baralho_jogador,
            3: self.alterar_baralho_jogador,
            4: self.exclui_baralho_jogador,
            5: self.add_carta_ao_baralho_jogador,
            6: self.remover_carta_do_baralho_jogador,
            7: self.listar_cartas_do_baralho_jogador
        }

        continua = True
        while (continua):
            opcao = self.__tela_jogador.tela_opcoes_baralho()
            if (opcao == 0):
                lista_opcoes[opcao]()
                continua = False
            lista_opcoes[opcao](jogador)

    def abre_tela(self):
        lista_opcoes = {
            0: self.retornar,
            1: self.incluir_jogador,
            2: self.altera_jogador,
            3: self.exclui_jogador,
            4: self.lista_jogadores,
            5: self.opcoes_baralho
        }

        continua = True
        while (continua):
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()
