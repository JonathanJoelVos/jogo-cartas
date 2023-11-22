from errors.alvo_invalido import AlvoInvalido
from errors.ataque_ja_realizado import AtaqueJaRealizado
from errors.ataque_sem_monstros import AtaqueSemMonstros
from errors.baralho_incompleto import BaralhoIncompleto
from errors.baralho_nao_existe import BaralhoNaoExiste
from errors.jogador_nao_existe import JogadorNaoExiste
from errors.mana_insuficiente import ManaInsuficiente
from errors.mesmo_jogador import MesmoJogador
from errors.monstro_sem_voar import MonstroSemVoar
from errors.nao_condiz import NaoCondiz
from errors.tabuleiro_cheio import TabuleiroCheio
from errors.tipo_de_carta_errado import TipoDeCartaErrado
from errors.voltar import Voltar
from errors.posicao_ocupada import PosicaoOcupada
from models.feitico import Feitico
from models.jogo import Jogo
from models.monstro import Monstro
from views.tela_jogo import TelaJogo
from DAOs.jogo_dao import JogosDAO
import random


class ControladorJogo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__jogos = JogosDAO()
        self.__tela_jogo = TelaJogo()
        self.__codigo_atual = 0

    @property
    def jogos(self):
        return self.__jogos.get_all()

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

            if opcao == '0':
                break

            elif opcao == '1':
                while True:

                    try:
                        self.seleciona_dados_para_jogar()
                        break
                    except JogadorNaoExiste as e:
                        self.__tela_jogo.mostra_msg(e)
                    except BaralhoNaoExiste as e:
                        self.__tela_jogo.mostra_msg(e)
                    except BaralhoIncompleto as e:
                        self.__tela_jogo.mostra_msg(e)
                    except MesmoJogador as e:
                        self.__tela_jogo.mostra_msg(e)

                    self.__tela_jogo.mostra_msg("Digite '-1' para voltar"
                                                " para a tela"
                                                " inicial outra tecla para"
                                                " tentar novamente.")

                    escolha = self.__tela_jogo.pega_string()
                    if escolha.strip() == '-1':
                        break

            else:
                while True:
                    try:
                        self.tela_de_historico()
                        break
                    except JogadorNaoExiste as e:
                        self.__tela_jogo.mostra_msg(e)

                    self.__tela_jogo.mostra_msg("Digite '-1' para voltar para a"
                                                " tela inicial ou 0"
                                                " para"
                                                " tentar novamente.")
                    escolha = self.__tela_jogo.pega_string()
                    if escolha.strip() == '-1':
                        break
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
            raise BaralhoNaoExiste
        if len(b1.cartas) < 20:
            print(len(b1.cartas))
            raise BaralhoIncompleto

        self.__tela_jogo.mostra_msg('Selecione o segundo jogador:')
        j2 = self.__controlador_sistema.controlador_jogador.seleciona_jogador()
        if j2 is None:
            raise JogadorNaoExiste
        if j1.nome == j2.nome:
            raise MesmoJogador

        self.__tela_jogo.mostra_msg('Selecione o baralho do segundo jogador')
        self.__controlador_sistema.controlador_jogador.lista_baralhos_jogador(
            j2)
        b2 = self.__controlador_sistema.controlador_jogador \
            .seleciona_baralho_do_jogador(j2)
        if b2 is None:
            raise BaralhoNaoExiste
        if len(b2.cartas) < 20:
            print(len(b2.cartas))
            raise BaralhoIncompleto

        random.shuffle(b1.cartas)
        random.shuffle(b2.cartas)
        self.jogar(j1, j2, b1, b2)

    def tela_de_historico(self):
        self.__tela_jogo.mostra_msg('Tela de históricos')
        self.__tela_jogo.mostra_msg(
            'Digite o nome de um jogador para ver o historico')
        jogador_selecionado = self.__controlador_sistema.controlador_jogador \
            .seleciona_jogador()

        if jogador_selecionado is None:
            raise JogadorNaoExiste()

        for jogo in self.__jogos.get_all():
            print(jogo)
            for jogador in jogo.jogadores:
                if jogador is jogador_selecionado:
                    self.__tela_jogo.mostra_dados_jogo({'codigo': jogo.codigo,
                                                        'j1': jogo.jogadores[0].nome,
                                                        'j2': jogo.jogadores[1].nome,
                                                        'b1': jogo.t1.baralho.nome,
                                                        'b2': jogo.t2.baralho.nome,
                                                        'vencedor': jogo.vencedor.nome,
                                                        'perdedor': jogo.perdedor.nome,
                                                        'empate': jogo.empate
                                                        })

    def realizar_turno(self, jogo: Jogo):
        em_batalha = jogo.em_batalha

        self.__tela_jogo.mostra_dados_do_turno({
            'jogador_atual': jogo.tabuleiro_do_turno.jogador.nome,
            'mana': jogo.tabuleiro_do_turno.mana_atual,
            'spellmana': jogo.tabuleiro_do_turno.spellmana,
        })

        while True:
            try:
                opcao = self.__tela_jogo.opcoes_turno(
                    em_batalha, jogo.tabuleiro_do_turno.jogador.nome)
                break  # Sai do loop se a entrada for válida
            except ValueError:
                self.__tela_jogo.mostra_msg('Digite um número válido')

        if opcao == -1:
            self.__tela_jogo.mostra_msg(
                f'{jogo.tabuleiro_do_turno.jogador.nome} desistiu da partida!')
            jogo.tabuleiro_do_turno.vida_torre -= 100
            jogo.ambos_vivos = False
            return

        if opcao == 0:
            jogo.passar_a_vez()
            return

        if not em_batalha:

            if opcao == 1:
                self.__tela_jogo.mostra_msg(
                    '\n --------- CARTAS NA MÃO:  -----------\n')
                posicao = 0
                for carta in jogo.tabuleiro_do_turno.cartas_na_mao:
                    posicao += 1
                    self.__tela_jogo.mostra_msg(f'POSICAO: {posicao}')
                    self.__controlador_sistema.controlador_carta.lista_carta(
                        carta)

                self.__tela_jogo.mostra_dados_do_turno({
                    'jogador_atual': jogo.tabuleiro_do_turno.jogador.nome,
                    'mana': jogo.tabuleiro_do_turno.mana_atual,
                    'spellmana': jogo.tabuleiro_do_turno.spellmana,
                })

                posicao_escolhida = self.__tela_jogo \
                    .pega_posicao_carta_em_lista(
                        len(jogo.tabuleiro_do_turno.cartas_na_mao))
                monstro = jogo.tabuleiro_do_turno.cartas_na_mao[posicao_escolhida - 1]
                if not isinstance(monstro, Monstro):
                    raise TipoDeCartaErrado

                try:
                    jogo.jogar_monstro(jogo.tabuleiro_do_turno, monstro)
                except TabuleiroCheio:
                    self.__tela_jogo.tela_tabuleiro_cheio({'monstros_tabuleiro_1': jogo.t1.monstros,
                                                           'monstros_em_batalha_1': jogo.t1.monstros_em_batalha,
                                                           'jogador_1': jogo.t1.jogador.nome,
                                                           'jogador_2': jogo.t2.jogador.nome,
                                                           'monstros_tabuleiro_2': jogo.t2.monstros,
                                                           'monstros_em_batalha_2': jogo.t2.monstros_em_batalha,
                                                           'vida_torre_t1': jogo.t1.vida_torre,
                                                           'vida_torre_t2': jogo.t2.vida_torre
                                                           })
                    self.__tela_jogo.mostra_msg(
                        f'----- MONSTRO SELECIONADO: {monstro.nome.upper()} -----')
                    self.__controlador_sistema.controlador_carta.lista_carta(
                        monstro)
                    eliminado = jogo.tabuleiro_do_turno.monstros[(self.__tela_jogo.pega_posicao_carta_em_lista
                                                                  (len(jogo.tabuleiro_do_turno.monstros))) - 1]

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
                    self.__tela_jogo.mostra_msg(
                        'Selecione um monstro aliado para entrar no campo de batalha')
                    self.__tela_jogo.mostrar_tabuleiros({'monstros_tabuleiro_1': jogo.t1.monstros,
                                                         'monstros_em_batalha_1': jogo.t1.monstros_em_batalha,
                                                         'jogador_1': jogo.t1.jogador.nome,
                                                         'jogador_2': jogo.t2.jogador.nome,
                                                         'monstros_tabuleiro_2': jogo.t2.monstros,
                                                         'monstros_em_batalha_2': jogo.t2.monstros_em_batalha,
                                                         'vida_torre_t1': jogo.t1.vida_torre,
                                                         'vida_torre_t2': jogo.t2.vida_torre
                                                         })
                    try:
                        carta = jogo.tabuleiro_do_turno.monstros[self.__tela_jogo.pega_posicao_carta_em_lista
                                                                 (len(jogo.tabuleiro_do_turno.monstros)) - 1]
                    except Voltar:
                        for monstro in monstros:
                            jogo.tabuleiro_do_turno.monstros.append(monstro)
                        raise Voltar
                    # escolheu o monstro que vai entrar na batalha
                    monstros.append(carta)
                    jogo.tabuleiro_do_turno.monstros.remove(carta)

                    self.__tela_jogo.mostra_msg(
                        f'{carta.nome.upper()} será movido para o campo de batalha ao iniciar ataque')
                    if (len(jogo.tabuleiro_do_turno.monstros) == 0):
                        self.__tela_jogo.mostra_msg('Tabuleiro vazio. O ataque será iniciado')
                        jogo.iniciar_ataque(monstros)
                        confirmar_ataque = True
                    else:
                        self.__tela_jogo.mostra_msg('Digite 1 para iniciar o ataque ou 0 para selecionar mais'
                                                    ' monstros')
                        confirmar = self.__tela_jogo.pega_string()
                        if confirmar == '1':
                            confirmar_ataque = True
                            jogo.iniciar_ataque(monstros)

        else:
            if opcao == 1:
                self.__tela_jogo.mostra_msg(
                    '\n --------- CARTAS NA MÃO:  -----------\n')
                posicao = 0
                for carta in jogo.tabuleiro_do_turno.cartas_na_mao:
                    posicao += 1
                    self.__tela_jogo.mostra_msg(f'POSICAO: {posicao}')
                    self.__controlador_sistema.controlador_carta.lista_carta(
                        carta)
                self.__tela_jogo.mostra_dados_do_turno({
                    'jogador_atual': jogo.tabuleiro_do_turno.jogador.nome,
                    'mana': jogo.tabuleiro_do_turno.mana_atual,
                    'spellmana': jogo.tabuleiro_do_turno.spellmana,
                })
                self.__tela_jogo.mostrar_tabuleiros({'monstros_tabuleiro_1': jogo.t1.monstros,
                                                     'monstros_em_batalha_1': jogo.t1.monstros_em_batalha,
                                                     'jogador_1': jogo.t1.jogador.nome,
                                                     'jogador_2': jogo.t2.jogador.nome,
                                                     'monstros_tabuleiro_2': jogo.t2.monstros,
                                                     'monstros_em_batalha_2': jogo.t2.monstros_em_batalha,
                                                     'vida_torre_t1': jogo.t1.vida_torre,
                                                     'vida_torre_t2': jogo.t2.vida_torre
                                                     })
                self.__tela_jogo.mostra_msg(
                    'Selecione a posição do feitiço aplicado na mão.')
                posicao_escolhida = self.__tela_jogo \
                    .pega_posicao_carta_em_lista(
                        len(jogo.tabuleiro_do_turno.cartas_na_mao))

                feitico = jogo.tabuleiro_do_turno.cartas_na_mao[posicao_escolhida - 1]
                if not isinstance(feitico, Feitico):
                    raise TipoDeCartaErrado

                escolha = self.__tela_jogo.tela_escolhe_tabuleiro_feitico()

                for tabuleiro in jogo.tabuleiros:
                    if tabuleiro.codigo != jogo.atacante_rodada.codigo:
                        defensor = tabuleiro

                if escolha == 'a':
                    tabuleiro_aplicado = jogo.tabuleiro_do_turno

                else:
                    if jogo.tabuleiro_do_turno.codigo == jogo.atacante_rodada.codigo:
                        tabuleiro_aplicado = defensor

                    if jogo.tabuleiro_do_turno.codigo == defensor.codigo:
                        tabuleiro_aplicado = jogo.atacante_rodada

                self.__tela_jogo.mostra_msg(
                    F'\n ---------- FEITICO ESCOLHIDO: {feitico.nome.upper()} ----------\n')
                self.__controlador_sistema.controlador_carta.lista_carta(
                    feitico)
                self.__tela_jogo.mostra_msg(
                    f'Tabuleiro aplicado: {tabuleiro_aplicado.jogador.nome}')

                self.__tela_jogo.mostrar_tabuleiros({'monstros_tabuleiro_1': jogo.t1.monstros,
                                                     'monstros_em_batalha_1': jogo.t1.monstros_em_batalha,
                                                     'jogador_1': jogo.t1.jogador.nome,
                                                     'jogador_2': jogo.t2.jogador.nome,
                                                     'monstros_tabuleiro_2': jogo.t2.monstros,
                                                     'monstros_em_batalha_2': jogo.t2.monstros_em_batalha,
                                                     'vida_torre_t1': jogo.t1.vida_torre,
                                                     'vida_torre_t2': jogo.t2.vida_torre
                                                     })
                self.__tela_jogo.mostra_msg(
                    'Escolha a posição do monstro afetado no campo de batalha')
                posicao_monstro = self.__tela_jogo \
                    .pega_posicao_carta_em_lista(
                        len(tabuleiro_aplicado.monstros_em_batalha))

                jogo.jogar_feitico(jogo.tabuleiro_do_turno,
                                   feitico, tabuleiro_aplicado, posicao_monstro)

            if opcao == 2:
                if jogo.tabuleiro_do_turno.codigo == jogo.atacante_rodada.codigo:
                    raise NaoCondiz
                self.__tela_jogo.mostra_msg(
                    f'Atacante da rodada: {jogo.atacante_rodada.jogador.nome}')
                self.__tela_jogo.mostra_msg('')
                self.__tela_jogo.mostrar_tabuleiros({'monstros_tabuleiro_1': jogo.t1.monstros,
                                                     'monstros_em_batalha_1': jogo.t1.monstros_em_batalha,
                                                     'jogador_1': jogo.t1.jogador.nome,
                                                     'jogador_2': jogo.t2.jogador.nome,
                                                     'monstros_tabuleiro_2': jogo.t2.monstros,
                                                     'monstros_em_batalha_2': jogo.t2.monstros_em_batalha,
                                                     'vida_torre_t1': jogo.t1.vida_torre,
                                                     'vida_torre_t2': jogo.t2.vida_torre
                                                     })
                self.__tela_jogo.mostra_msg('Escolha uma posição do campo de batalha para inserir um monstro aliado'
                                            '(irá bloquear o atacante dessa posição na batalha)')
                posicao_defesa = (self.__tela_jogo.pega_posicao_carta_em_lista
                                  (len(jogo.atacante_rodada.monstros_em_batalha)))
                self.__tela_jogo.mostra_msg('Agora, selecione a posição de um monstro aliado'
                                            ' no tabuleiro para envia-lo à batalha na posição escolhida.')
                pos_monstro = self.__tela_jogo.pega_posicao_carta_em_lista(
                    len(jogo.tabuleiro_do_turno.monstros))
                monstro = jogo.tabuleiro_do_turno.monstros[pos_monstro-1]

                jogo.realizar_bloqueio(
                    jogo.tabuleiro_do_turno, posicao_defesa, monstro)

    def jogar(self, j1, j2, b1, b2):
        self.__codigo_atual += 1

        jogo = Jogo(self.__codigo_atual, j1, j2, b1, b2)
        self.__jogos.add(jogo)

        j1.partidas_jogadas += 1
        j2.partidas_jogadas += 1

        while True:
            self.__tela_jogo.mostra_dados_da_rodada({
                'rodada': jogo.rodada,
                'tabuleiro_turno': jogo.tabuleiro_do_turno.jogador.nome,
                'atacante_rodada': jogo.atacante_rodada,
                'ataque_realizado': jogo.ataque_ja_realizado,
                'em_batalha': jogo.em_batalha,
                'contador_de_passes': jogo.contador_de_passes

            })
            self.__tela_jogo.mostrar_dados_jogador_rodada({
                'nome': j1.nome,
                'vida_torre': jogo.t1.vida_torre,
                'mana': jogo.t1.mana_atual,
                'spellmana': jogo.t1.spellmana,
                'monstros_tabuleiro': jogo.t1.monstros,
                'monstros_em_batalha': jogo.t1.monstros_em_batalha,
            })
            self.__tela_jogo.mostrar_dados_jogador_rodada({
                'nome': j2.nome,
                'vida_torre': jogo.t2.vida_torre,
                'mana': jogo.t2.mana_atual,
                'spellmana': jogo.t2.spellmana,
                'monstros_tabuleiro': jogo.t2.monstros,
                'monstros_em_batalha': jogo.t2.monstros_em_batalha,
            })
            try:
                self.realizar_turno(jogo)

            except TipoDeCartaErrado as e:
                self.__tela_jogo.mostra_msg(e)

            except ManaInsuficiente as e:
                self.__tela_jogo.mostra_msg(e)

            except Voltar as e:
                self.__tela_jogo.mostra_msg(e)

            except AtaqueJaRealizado as e:
                self.__tela_jogo.mostra_msg(e)

            except NaoCondiz as e:
                self.__tela_jogo.mostra_msg(e)

            except AtaqueSemMonstros as e:
                self.__tela_jogo.mostra_msg(e)

            except AlvoInvalido as e:
                self.__tela_jogo.mostra_msg(e)

            except MonstroSemVoar as e:
                self.__tela_jogo.mostra_msg(e)

            except PosicaoOcupada as e:
                self.__tela_jogo.mostra_msg(e)
            if jogo.rodada == 16:
                self.__tela_jogo.mostra_msg('')
                self.__tela_jogo.mostra_msg('Rodada 16: Fim de jogo!')
                self.__tela_jogo.mostra_msg('')

                v1 = jogo.t1.vida_torre
                v2 = jogo.t2.vida_torre

                if v1 == v2:
                    jogo.empate = True
                    self.__tela_jogo.mostra_msg(
                        'Jogo empatado! Ambos os jogadores serão registrados como vencedores!')
                    j1.vitorias += 1
                    j2.vitorias += 1
                    j1.pontos += 3
                    j2.pontos += 3

                elif v1 > v2:
                    jogo.vencedor = jogo.t1.jogador
                    jogo.vencedor.vitorias += 1
                    jogo.vencedor.pontos += 3

                    jogo.perdedor = jogo.t2.jogador
                    jogo.perdedor.derrotas += 1
                    jogo.perdedor.pontos -= 1

                    self.__tela_jogo.mostra_msg(
                        f'Vitória do(a) {jogo.vencedor} ')
                    self.__tela_jogo.mostra_msg('')

                else:
                    jogo.vencedor = jogo.t2.jogador
                    jogo.vencedor.vitorias += 1
                    jogo.vencedor.pontos += 3

                    jogo.perdedor = jogo.t1.jogador
                    jogo.perdedor.derrotas += 1
                    jogo.perdedor.pontos -= 1

                    self.__tela_jogo.mostra_msg(
                        f'Vitória do(a) {jogo.vencedor.nome} ')
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
                self.__tela_jogo.mostra_msg(
                    f'Vitória do(a) {jogo.vencedor.nome} ')
                self.__tela_jogo.mostra_msg('')
                break
