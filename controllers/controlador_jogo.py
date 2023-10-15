from errors.alvo_invalido import AlvoInvalido
from errors.ataque_ja_realizado import AtaqueJaRealizado
from errors.ataque_sem_monstros import AtaqueSemMonstros
from errors.baralho_incompleto import BaralhoIncompleto
from errors.baralho_nao_existe import BaralhoNaoExiste
from errors.jogador_nao_existe import JogadorNaoExiste
from errors.mana_insuficiente import ManaInsuficiente
from errors.monstro_sem_voar import MonstroSemVoar
from errors.nao_condiz import NaoCondiz
from errors.tabuleiro_cheio import TabuleiroCheio
from errors.tipo_de_carta_errado import TipoDeCartaErrado
from errors.voltar import Voltar
from models.feitico import Feitico
from models.jogo import Jogo
from models.monstro import Monstro
from views.tela_jogo import TelaJogo


class ControladorJogo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__jogos = []
        self.__tela_jogo = TelaJogo()
        self.__codigo_atual = 0

    @property
    def jogos(self):
        return self.__jogos

    @property
    def tela_jogo(self):
        return self.__tela_jogo

    @property
    def codigo_atual(self):
        return self.__codigo_atual

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_jogo.opcoes_tela()

            if opcao == 0:
                break

            elif opcao == 1:
                while True:
                    self.__tela_jogo.mostra_msg("Digite '1' para voltar"
                                                " para a tela"
                                                " inicial ou 0 para"
                                                " continuar.")

                    escolha = self.__tela_jogo.pega_inteiro()
                    if escolha == 1:
                        break
                    try:
                        self.seleciona_dados_para_jogar()
                        break
                    except JogadorNaoExiste:
                        self.__tela_jogo.mostra_msg(
                            "O jogador não existe. Tente novamente.")
                    except BaralhoNaoExiste:
                        self.__tela_jogo.mostra_msg(
                            "O baralho não existe. Tente novamente.")
                    except BaralhoIncompleto:
                        self.__tela_jogo.mostra_msg(
                            'Baralho incompleto. Tente novamente.')

            else:
                while True:
                    self.__tela_jogo.mostra_msg("Digite '1' para voltar para a"
                                                " tela inicial ou outra"
                                                " tecla para"
                                                " continuar.")
                    escolha = self.__tela_jogo.pega_inteiro()
                    if escolha == 1:
                        break
                    try:
                        self.tela_de_historico()
                        break
                    except JogadorNaoExiste:
                        self.__tela_jogo.mostra_msg(
                            "O jogador não existe. Tente novamente.")
        self.retornar()

    def seleciona_dados_para_jogar(self):
        self.__tela_jogo.mostra_msg('Selecione o primeiro jogador:')
        j1 = self.__controlador_sistema.controlador_jogador.seleciona_jogador()
        if j1 is None:
            raise JogadorNaoExiste

        self.__tela_jogo.mostra_msg('Selecione o baralho do primeiro jogador:')
        self.__controlador_sistema.controlador_jogador.lista_baralhos_jogador(
            j1)
        b1 = self.__controlador_sistema.controlador_jogador \
            .seleciona_baralho_do_jogador(
                j1)
        if b1 is None:
            raise BaralhoNaoExiste()
        if len(b1.cartas) < 20:
            raise BaralhoIncompleto()

        self.__tela_jogo.mostra_msg('Selecione o segundo jogador:')
        j2 = self.__controlador_sistema.controlador_jogador.seleciona_jogador()
        print(j2.nome)
        if j2 is None:
            raise JogadorNaoExiste()

        self.__tela_jogo.mostra_msg('Selecione o baralho do segundo jogador')
        self.__controlador_sistema.controlador_jogador.lista_baralhos_jogador(
            j2)
        b2 = self.__controlador_sistema.controlador_jogador \
            .seleciona_baralho_do_jogador(j2)
        if b2 is None:
            raise BaralhoNaoExiste
        if len(b2.cartas) < 20:
            raise BaralhoIncompleto

        self.jogar(j1, j2, b1, b2)

    def tela_de_historico(self):
        self.__tela_jogo.mostra_msg('Tela de históricos')
        self.__tela_jogo.mostra_msg(
            'Digite o nome de um jogador para ver o historico')
        jogador_selecionado = self.__controlador_sistema.controlador_jogador \
            .seleciona_jogador()

        if jogador_selecionado is None:
            raise JogadorNaoExiste()

        for jogo in self.__jogos:
            for jogador in jogo.jogadores:
                if jogador is jogador_selecionado:
                    self.__tela_jogo.mostra_dados_jogo(jogo)

    def realizar_turno(self, jogo: Jogo):
        em_batalha = jogo.em_batalha
        self.__tela_jogo.mostra_msg('')
        self.__tela_jogo.mostra_msg(
            f'Vez de {jogo.tabuleiro_do_turno.jogador.nome}.')
        while True:
            try:
                opcao = self.__tela_jogo.opcoes_turno(em_batalha)
                break  # Sai do loop se a entrada for válida
            except ValueError:
                self.__tela_jogo.mostra_msg('Digite um número válido')

        if opcao == -1:
            jogo.tabuleiro_do_turno.vida_torre -= 100
            jogo.ambos_vivos = False
            return

        if opcao == 0:
            self.__tela_jogo.mostra_msg(
                f'Jogador(a) {jogo.tabuleiro_do_turno.jogador.nome} passou a vez.')
            jogo.passar_a_vez()
            return

        if not em_batalha:
            self.__tela_jogo.mostra_msg(
                f'Atacante da rodada: {jogo.atacante_rodada.jogador.nome}')
            self.__tela_jogo.mostra_msg(
                f'Ataque já realizado: {jogo.ataque_ja_realizado}')

            if opcao == 1:
                self.__tela_jogo.mostra_msg('Cartas na mão:')
                self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                    jogo.tabuleiro_do_turno.cartas_na_mao)
                monstro = jogo.tabuleiro_do_turno.cartas_na_mao[self.__tela_jogo.pega_posicao_carta_em_lista
                                                                (jogo.tabuleiro_do_turno.cartas_na_mao) - 1]
                if not isinstance(monstro, Monstro):
                    raise TipoDeCartaErrado

                try:
                    jogo.jogar_monstro(jogo.tabuleiro_do_turno, monstro)
                except TabuleiroCheio:
                    self.__tela_jogo.mostra_msg('Tabuleiro cheio. Digite "v" para voltar para a tela de opções ou '
                                                'outra tecla para escolher um monstro aliado para ser'
                                                ' eliminado.')

                    self.__tela_jogo.pega_string()

                    self.__tela_jogo.mostra_msg('Selecione um monstro aliado para ser substituido'
                                                ' pela carta escolhida:')
                    self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                        jogo.tabuleiro_do_turno.monstros)
                    eliminado = jogo.tabuleiro_do_turno.monstros[(self.__tela_jogo.pega_posicao_carta_em_lista
                                                                  (jogo.tabuleiro_do_turno.monstros)) - 1]

                    jogo.tabuleiro_do_turno.eliminar_monstro(eliminado)
                    jogo.jogar_monstro(jogo.tabuleiro_do_turno, monstro)

            if opcao == 2:
                if jogo.ataque_ja_realizado:
                    raise AtaqueJaRealizado
                if jogo.tabuleiro_do_turno is not jogo.atacante_rodada:
                    raise NaoCondiz

                monstros = []
                confirmar_ataque = False
                while not confirmar_ataque:
                    self.__tela_jogo.mostra_msg('Monstros no seu tabuleiro:')
                    self.__tela_jogo.mostra_msg(
                        'Selecione o monstro que vai entrar na batalha')
                    self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                        jogo.tabuleiro_do_turno.monstros)
                    carta = jogo.tabuleiro_do_turno.monstros[self.__tela_jogo.pega_posicao_carta_em_lista
                                                             (jogo.tabuleiro_do_turno.monstros) - 1]
                    # escolheu o monstro que vai entrar na batalha
                    monstros.append(carta)
                    self.__tela_jogo.mostra_msg(
                        'Monstro movido para o campo de batalha')
                    self.__tela_jogo.mostra_msg(
                        'Digite 1 para confirmar ou outra tecla para desfazer a ação.')
                    desfazer = self.__tela_jogo.pega_inteiro()
                    if not desfazer == 1:
                        monstros.remove(carta)
                        self.__tela_jogo.mostra_msg(
                            'Monstro voltou para o tabuleiro')

                    self.__tela_jogo.mostra_msg('Digite 1 para iniciar o ataque ou outra tecla para selecionar mais'
                                                ' monstros')

                    if self.__tela_jogo.pega_inteiro() == 1:
                        confirmar_ataque = True
                        jogo.iniciar_ataque(monstros)

        else:
            if opcao == 1:
                self.__tela_jogo.mostra_msg(
                    'Selecione o feitiço que será jogado')
                self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                    jogo.tabuleiro_do_turno.cartas_na_mao)
                posicao = self.__tela_jogo.pega_posicao_carta_em_lista(
                    jogo.tabuleiro_do_turno.cartas_na_mao)
                feitico = jogo.tabuleiro_do_turno.cartas_na_mao[posicao - 1]
                if not isinstance(feitico, Feitico):
                    raise TipoDeCartaErrado
                self.__tela_jogo.mostra_msg(
                    'O feitiço será aplicado em um monstro aliado ou um inimigo?')
                self.__tela_jogo.mostra_msg('Digite "a" para aliado, "i" para inimigo ou "v" para voltar para'
                                            ' a tela de opções')
                escolha = self.__tela_jogo.pega_string()
                while escolha.lower() != 'a' and escolha.lower != 'i':
                    self.__tela_jogo.mostra_msg(
                        'Digite uma opção válida ou "v" para voltar para a tela de opções')
                    escolha = self.__tela_jogo.pega_string()

                for tabuleiro in jogo.tabuleiros:
                    if escolha == 'a':
                        tabuleiro_aplicado = jogo.tabuleiro_do_turno

                    else:
                        tabuleiro_aplicado = tabuleiro

                self.__tela_jogo.mostra_msg(
                    'Escolha o monstro afetado no campo de batalha')
                self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                    tabuleiro_aplicado)
                posicao_monstro = self.__tela_jogo.pega_posicao_carta_em_lista(
                    tabuleiro_aplicado.monstros_em_batalha)

                jogo.jogar_feitico(jogo.tabuleiro_do_turno,
                                   feitico, tabuleiro_aplicado, posicao_monstro)

            if opcao == 2:
                self.__tela_jogo.mostra_msg(
                    'Escolha uma posicao para bloquear')
                self.__tela_jogo.mostra_msg('Monstros atacando:')
                self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                    jogo.tabuleiro_do_turno.monstros_em_batalha)
                self.__tela_jogo.mostra_msg('Monstros no seu tabuleiro:')
                self.__tela_jogo.mostra_dados_em_lista_de_cartas(
                    jogo.tabuleiro_do_turno.monstros)
                self.__tela_jogo.mostra_msg(
                    'Escolha um monstro aliado para bloquear um atacante')
                posicao_bloqueador = self.__tela_jogo.pega_posicao_carta_em_lista(
                    jogo.tabuleiro_do_turno.monstros)
                monstro = jogo.tabuleiro_do_turno.monstros[posicao_bloqueador - 1]
                self.__tela_jogo.mostra_msg('Escolha a posição de defesa (deve coincidir com a posição do monstro'
                                            ' no ataque), ou digite "v" para voltar para a tela de opções:')
                posicao_defesa = self.__tela_jogo.pega_string()
                jogo.realizar_bloqueio(
                    jogo.tabuleiro_do_turno, posicao_defesa, monstro)

    def jogar(self, j1, j2, b1, b2):
        self.__codigo_atual += 1

        jogo = Jogo(self.__codigo_atual, j1, j2, b1, b2)
        self.__jogos.append(jogo)

        j1.partidas_jogadas += 1
        j2.partidas_jogadas += 1

        while True:
            self.__tela_jogo.mostra_msg(f'Rodada {jogo.rodada}:')
            for tabuleiro in jogo.tabuleiros:
                self.__tela_jogo.mostra_msg('')
                self.__tela_jogo.mostra_msg(
                    f'Jogador {tabuleiro.jogador.nome}:')
                self.__tela_jogo.mostra_msg(
                    f'Vida da torre: {tabuleiro.vida_torre}')
                self.__tela_jogo.mostra_msg(
                    f'Monstros no tabuleiro: {tabuleiro.monstros}')

            self.__tela_jogo.mostra_msg(
                f'Atacante da rodada: {jogo.tabuleiro_do_turno.jogador.nome}')

            try:
                self.realizar_turno(jogo)

            except TipoDeCartaErrado:
                self.__tela_jogo.mostra_msg(
                    'Esse tipo de carta não pode ser jogada nesse momento!')

            except ManaInsuficiente:
                self.__tela_jogo.mostra_msg('Mana Insuficiente.')

            except Voltar:
                self.__tela_jogo.mostra_msg(
                    'Voltando para a tela de opções do turno:')

            except AtaqueJaRealizado:
                self.__tela_jogo.mostra_msg(
                    'Já houve uma batalha nessa rodada!')

            except NaoCondiz:
                self.__tela_jogo.mostra_msg(
                    'Jogador não condiz com o atacante/defensor da rodada')

            except AtaqueSemMonstros:
                self.__tela_jogo.mostra_msg(
                    'Não pode iniciar um ataque sem monstros.')

            except AlvoInvalido:
                self.__tela_jogo.mostra_msg('Alvo inválido!')

            except MonstroSemVoar:
                self.__tela_jogo.mostra_msg(
                    "Esse monstro não pode bloquear um monstro voador!")

            if jogo.rodada == 16:
                self.__tela_jogo.mostra_msg('')
                self.__tela_jogo.mostra_msg('Rodada 16: Fim de jogo!')
                self.__tela_jogo.mostra_msg('')
                i = 1
                for tabuleiro in jogo.tabuleiros:
                    if i == 1:
                        v1 = tabuleiro.vida
                        t1 = tabuleiro
                    if i == 1:
                        v2 = tabuleiro.vida
                        t2 = tabuleiro
                    i += 1

                if v1 == v2:
                    jogo.empate = True
                    self.__tela_jogo.mostra_msg(
                        'Jogo empatado! Ambos os jogadores serão registrados como vencedores!')
                    j1.vitorias += 1
                    j2.vitorias += 1
                    j1.pontos += 3
                    j2.pontos += 3

                elif v1 > v2:
                    jogo.vencedor = t1.jogador
                    jogo.vencedor.vitorias += 1
                    jogo.vencedor.pontos += 3

                    jogo.perdedor = t2.jogador
                    jogo.perdedor.derrotas += 1
                    jogo.perdedor.pontos -= 1

                    self.__tela_jogo.mostra_msg(
                        f'Vitória do(a) {jogo.vencedor} ')
                    self.__tela_jogo.mostra_msg('')

                else:
                    jogo.vencedor = t2.jogador
                    jogo.vencedor.vitorias += 1
                    jogo.vencedor.pontos += 3

                    jogo.perdedor = t1.jogador
                    jogo.perdedor.derrotas += 1
                    jogo.perdedor.pontos -= 1

                    self.__tela_jogo.mostra_msg(
                        f'Vitória do(a) {jogo.vencedor} ')
                    self.__tela_jogo.mostra_msg('')

                break

            if not jogo.ambos_vivos:
                for tabuleiro in jogo.tabuleiros:
                    if tabuleiro.vida_torre <= 0:
                        jogo.perdedor = tabuleiro.jogador
                        jogo.perdedor.derrotas += 1
                        jogo.perdedor.pontos -= 1
                    elif tabuleiro.vida_torre > 0:
                        jogo.vencedor = tabuleiro.jogador
                        jogo.vencedor.vitorias += 1
                        jogo.vencedor.pontos += 3
                self.__tela_jogo.mostra_msg('Jogo Encerrado.')
                self.__tela_jogo.mostra_msg(f'Vitória do(a) {jogo.vencedor} ')
                self.__tela_jogo.mostra_msg('')
                break
