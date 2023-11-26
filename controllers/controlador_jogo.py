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
from models.atributo_especial import AtributoEspecial
from models.monstro import Monstro
from views.tela_jogo_gui import TelaJogo
from DAOs.jogos_dao import JogosDAO
from DAOs.jogador_dao import JogadorDAO
import random


class ControladorJogo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__jogos = JogosDAO()
        self.__jogador_dao = JogadorDAO()
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
            for jogador in jogo.jogadores:
                if jogador.nome == jogador_selecionado.nome:
                    self.__tela_jogo.mostra_dados_jogo({'codigo': jogo.codigo,
                                                        'j1': jogo.jogadores[0].nome,
                                                        'j2': jogo.jogadores[1].nome,
                                                        'b1': jogo.t1.baralho.nome,
                                                        'b2': jogo.t2.baralho.nome,
                                                        'vencedor': jogo.vencedor.nome,
                                                        'perdedor': jogo.perdedor.nome,
                                                        'empate': jogo.empate
                                                        })

    def pegar_dados_monstros_turno(self, jogo):
        dados_passar = []
        dados_t1_monstros = []
        dados_t1_monstros.append(len(jogo.t1.monstros))
        dados_t1_monstros_batalha = []
        dados_t1_monstros_batalha.append(len(jogo.t1.monstros_em_batalha))
        dados_t2_monstros = []
        dados_t2_monstros.append(len(jogo.t2.monstros))
        dados_t2_monstros_batalha = []
        dados_t2_monstros_batalha.append(len(jogo.t2.monstros_em_batalha))
        for monstro in jogo.t1.monstros:
            dados_t1_monstros.append(monstro.nome)
            dados_t1_monstros.append(monstro.ataque)
            dados_t1_monstros.append(monstro.vida)
            dados_t1_monstros.append(monstro.atributos[0].efeito[0])
        for monstro in jogo.t1.monstros_em_batalha:
            if monstro is not None:
                dados_t1_monstros_batalha.append(monstro.nome)
                dados_t1_monstros_batalha.append(monstro.ataque)
                dados_t1_monstros_batalha.append(monstro.vida)
                dados_t1_monstros_batalha.append(monstro.atributos[0].efeito[0])
            else:
                dados_t1_monstros_batalha.append(None)
        for monstro in jogo.t2.monstros:
            dados_t2_monstros.append(monstro.nome)
            dados_t2_monstros.append(monstro.ataque)
            dados_t2_monstros.append(monstro.vida)
            dados_t2_monstros.append(monstro.atributos[0].efeito[0])
        for monstro in jogo.t2.monstros_em_batalha:
            if monstro is not None:
                dados_t2_monstros_batalha.append(monstro.nome)
                dados_t2_monstros_batalha.append(monstro.ataque)
                dados_t2_monstros_batalha.append(monstro.vida)
                dados_t2_monstros_batalha.append(monstro.atributos[0].efeito[0])
            else:
                dados_t2_monstros_batalha.append(None)

        dados_passar.append(dados_t1_monstros)
        dados_passar.append(dados_t1_monstros_batalha)
        dados_passar.append(dados_t2_monstros)
        dados_passar.append(dados_t2_monstros_batalha)
        return dados_passar  # 4 listas de (len(lista)-1) informações

    def realizar_turno(self, jogo: Jogo):
        em_batalha = jogo.em_batalha
        opcao, janela_turno = self.__tela_jogo.mostra_dados_do_turno({
            'rodada': jogo.rodada,
            'j1': jogo.t1.jogador.nome,
            'j2': jogo.t2.jogador.nome,
            'atacante': jogo.atacante_rodada.jogador.nome,
            'atacou': jogo.ataque_ja_realizado,
            'turno': jogo.tabuleiro_do_turno.jogador.nome,
            'vida_j1': jogo.t1.vida_torre,
            'vida_j2': jogo.t2.vida_torre,
            'mana_j1': jogo.t1.mana_atual,
            'mana_j2': jogo.t2.mana_atual,
            'spellmana_j1': jogo.t1.spellmana,
            'spellmana_j2': jogo.t2.spellmana,
            'contador_de_passes': jogo.contador_de_passes,
            'em_batalha': em_batalha,
            'dados_monstros': self.pegar_dados_monstros_turno(jogo)
        })
        if opcao == 'GAME OVER':
            self.__tela_jogo.mostra_msg('Desista para sair do jogo')
            self.__tela_jogo.fechar_janela(janela_turno)
            return

        if opcao is None:
            self.__tela_jogo.mostra_msg('Selecione uma opção!')
        if opcao == -1:
            self.__tela_jogo.mostra_msg(
                f'{jogo.tabuleiro_do_turno.jogador.nome} desistiu da partida!')
            jogo.tabuleiro_do_turno.vida_torre -= 100
            jogo.ambos_vivos = False
            self.__tela_jogo.fechar_janela(janela_turno)
            return

        if opcao == 0:
            self.__tela_jogo.mostra_msg(f'{jogo.tabuleiro_do_turno.jogador.nome} Passou a vez!')
            if jogo.contador_de_passes == 1:
                if not jogo.em_batalha:
                    self.__tela_jogo.mostra_msg('Nova Rodada!')
                else:
                    self.__tela_jogo.mostra_msg('A batalha será realizada.')
            jogo.passar_a_vez()
            self.__tela_jogo.fechar_janela(janela_turno)
            return

        if not em_batalha:

            if opcao == 1:
                cartas = []
                for carta in jogo.tabuleiro_do_turno.cartas_na_mao:
                    cartas.append(carta)
                self.__controlador_sistema.controlador_carta.lista_cartas(cartas)


                #Retorna None ou a posição
                posicao_escolhida = self.__tela_jogo.pega_posicao_carta_em_lista(len(jogo.tabuleiro_do_turno.cartas_na_mao), janela_turno)
                if posicao_escolhida is None:
                    self.__tela_jogo.fechar_janela(janela_turno)
                    raise Voltar
                monstro = jogo.tabuleiro_do_turno.cartas_na_mao[posicao_escolhida - 1]
                if not isinstance(monstro, Monstro):
                    self.__tela_jogo.fechar_janela(janela_turno)
                    raise TipoDeCartaErrado

                try:
                    jogo.jogar_monstro(jogo.tabuleiro_do_turno, monstro)
                except ManaInsuficiente:
                    self.__tela_jogo.fechar_janela(janela_turno)
                    raise ManaInsuficiente
                except TabuleiroCheio:
                    janela = self.__tela_jogo.tela_tabuleiro_cheio({'nome': monstro.nome, 'ataque': monstro.ataque, 'vida': monstro.vida, 'atributo': monstro.atributos[0].efeito}, janela_turno)

                    while True:
                        pos_eliminado = self.__tela_jogo.pega_posicao_carta_em_lista((len(jogo.tabuleiro_do_turno.monstros)), janela_turno)
                        if pos_eliminado is not None:
                            break
                        self.__tela_jogo.mostra_msg('Escolha a posição para substituir o monstro')

                    pos_eliminado -= 1

                    jogo.tabuleiro_do_turno.monstros[pos_eliminado] = monstro

                    self.__tela_jogo.fechar_janela(janela)

            if opcao == 2:
                if jogo.ataque_ja_realizado:
                    self.__tela_jogo.fechar_janela(janela_turno)
                    raise AtaqueJaRealizado
                if jogo.tabuleiro_do_turno is not jogo.atacante_rodada:
                    self.__tela_jogo.fechar_janela(janela_turno)
                    raise NaoCondiz

                self.__tela_jogo.mostra_msg('Escolha um monstro do tabuleiro para entrar em batalha')
                monstros = []
                confirmar_ataque = False
                cancelou = False
                jafoi = []
                while not confirmar_ataque:
                    if cancelou:
                        posicoes_none = []
                        posicao = -1
                        for monstro_tabuleiro in jogo.tabuleiro_do_turno.monstros:
                            posicao += 1
                            if monstro_tabuleiro.codigo == '0':
                                posicoes_none.append(posicao)

                        for monstro in monstros:
                            for i in range(3):
                                if len(monstros) == 0:
                                    break
                                if i in posicoes_none:
                                    jogo.tabuleiro_do_turno.monstros[i] = monstro

                        self.__tela_jogo.fechar_janela(janela_turno)
                        raise Voltar
                    try:
                        pos_carta = ((self.__tela_jogo.pega_posicao_carta_em_lista(len(jogo.tabuleiro_do_turno.monstros), janela_turno)) - 1)
                    except Exception:
                        posicoes_none = []
                        posicao = -1
                        for monstro_tabuleiro in jogo.tabuleiro_do_turno.monstros:
                            posicao += 1
                            if monstro_tabuleiro.codigo == '0':
                                posicoes_none.append(posicao)

                        for monstro in monstros:
                            for i in range(3):
                                if len(monstros) == 0:
                                    break
                                if i in posicoes_none:
                                    jogo.tabuleiro_do_turno.monstros[i] = monstro
                        self.__tela_jogo.fechar_janela(janela_turno)
                        raise Voltar
                    if pos_carta is None:
                        if monstros:
                            posicoes_none = []
                            posicao = -1
                            for monstro_tabuleiro in jogo.tabuleiro_do_turno.monstros:
                                posicao += 1
                                if monstro_tabuleiro.codigo == '0':
                                    posicoes_none.append(posicao)

                            for monstro in monstros:
                                for i in range(3):
                                    if len(monstros) == 0:
                                        break
                                    if i in posicoes_none:
                                        jogo.tabuleiro_do_turno.monstros[i] = monstro
                        self.__tela_jogo.fechar_janela(janela_turno)
                        raise Voltar
                    if pos_carta in jafoi:
                        self.__tela_jogo.mostra_msg('Esse monstro já foi selecionado para batalha')
                        if monstros:
                            posicoes_none = []
                            posicao = -1
                            for monstro_tabuleiro in jogo.tabuleiro_do_turno.monstros:
                                posicao += 1
                                if monstro_tabuleiro.codigo == '0':
                                    posicoes_none.append(posicao)

                            for monstro in monstros:
                                for i in range(3):
                                    if len(monstros) == 0:
                                        break
                                    if i in posicoes_none:
                                        jogo.tabuleiro_do_turno.monstros[i] = monstro
                        self.__tela_jogo.fechar_janela(janela_turno)
                        raise Voltar

                    carta = jogo.tabuleiro_do_turno.monstros[pos_carta]
                    jafoi.append(pos_carta)
                    monstros.append(carta)
                    jogo.tabuleiro_do_turno.monstros[pos_carta] = Monstro('ESPAÇO VAZIO', 0, '0', 0, 0, [AtributoEspecial([''])])
                    #quando add e da erro o espaço vazio fica no bagui
                    self.__tela_jogo.mostra_msg(
                        f'{carta.nome.upper()} será movido para o campo de batalha ao iniciar ataque')

                    confirmar, cancelou = self.__tela_jogo.tela_confirmar_ataque(janela_turno)
                    if confirmar == '1':
                        confirmar_ataque = True
                        jogo.iniciar_ataque(monstros)
                    #if confirmar == '0':



            self.__tela_jogo.fechar_janela(janela_turno)

        else:
            if opcao == 1:
                self.__tela_jogo.mostra_msg(
                    '\n --------- CARTAS NA MÃO:  -----------\n')
                posicao = 0
                cartas = []
                for carta in jogo.tabuleiro_do_turno.cartas_na_mao:
                    posicao += 1
                    self.__tela_jogo.mostra_msg(f'POSICAO: {posicao}')
                    cartas.append(carta)
                self.__controlador_sistema.controlador_carta.lista_cartas(cartas)
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
                    len(jogo.tabuleiro_do_turno.cartas_na_mao), janela_turno)

                feitico = jogo.tabuleiro_do_turno.cartas_na_mao[posicao_escolhida - 1]
                if not isinstance(feitico, Feitico):
                    self.__tela_jogo.fechar_janela(janela_turno)
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
                self.__controlador_sistema.controlador_carta.lista_cartas(
                    [feitico])
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
                    len(tabuleiro_aplicado.monstros_em_batalha), janela_turno)

                jogo.jogar_feitico(jogo.tabuleiro_do_turno,
                                   feitico, tabuleiro_aplicado, posicao_monstro)

            if opcao == 2:
                if jogo.tabuleiro_do_turno.codigo == jogo.atacante_rodada.codigo:
                    self.__tela_jogo.fechar_janela(janela_turno)
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
                                  (len(jogo.atacante_rodada.monstros_em_batalha)), janela_turno)
                self.__tela_jogo.mostra_msg('Agora, selecione a posição de um monstro aliado'
                                            ' no tabuleiro para envia-lo à batalha na posição escolhida.')
                pos_monstro = self.__tela_jogo.pega_posicao_carta_em_lista(
                    len(jogo.tabuleiro_do_turno.monstros), janela_turno)
                monstro = jogo.tabuleiro_do_turno.monstros[pos_monstro - 1]

                jogo.realizar_bloqueio(
                    jogo.tabuleiro_do_turno, posicao_defesa, monstro)

        self.__tela_jogo.fechar_janela(janela_turno)

    def jogar(self, j1, j2, b1, b2):
        self.__codigo_atual = len(self.__jogos.get_all()) + 1

        jogo = Jogo(self.__codigo_atual, j1, j2, b1, b2)

        j1.partidas_jogadas += 1
        j2.partidas_jogadas += 1

        while True:
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
                '''
                self.__tela_jogo.mostra_msg('')
                self.__tela_jogo.mostra_msg('Rodada 16: Fim de jogo!')
                self.__tela_jogo.mostra_msg('')
                '''

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

                    '''
                    self.__tela_jogo.mostra_msg(
                        f'Vitória do(a) {jogo.vencedor} ')
                    self.__tela_jogo.mostra_msg('')
                    '''

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

                '''
                self.__tela_jogo.mostra_msg('Jogo Encerrado.')
                self.__tela_jogo.mostra_msg(
                    f'Vitória do(a) {jogo.vencedor.nome} ')
                self.__tela_jogo.mostra_msg('')
                '''
                break
        self.__jogador_dao.update(jogo.vencedor)
        self.__jogador_dao.update(jogo.perdedor)
        self.__jogos.add(jogo)
