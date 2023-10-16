from random import choice

from errors.ataque_sem_monstros import AtaqueSemMonstros
from errors.mana_insuficiente import ManaInsuficiente
from errors.monstro_sem_voar import MonstroSemVoar
from errors.nao_condiz import NaoCondiz
from errors.tabuleiro_cheio import TabuleiroCheio
from models.tabuleiro import Tabuleiro
from models.monstro import Monstro
from errors.posicao_ocupada import PosicaoOcupada


class Jogo:
    def __init__(self, codigo, j1, j2, b1, b2):
        self.__t1 = Tabuleiro('1', j1, b1)
        self.__t2 = Tabuleiro('2', j2, b2)
        self.__jogadores = [j1, j2]
        self.__tabuleiros = [self.__t1, self.__t2]
        self.__tabuleiro_inicial = choice([self.__t1, self.__t2])
        self.__codigo = codigo
        self.__ambos_vivos = True
        self.__vencedor = None
        self.__perdedor = None
        self.__empate = False
        self.__baralho_vencedor = None
        self.__baralho_perdedor = None
        self.__rodada = 1
        self.__atacante_rodada = self.__tabuleiro_inicial
        self.__ataque_ja_realizado = False
        self.__bloqueio_ja_realizado = False
        self.__tabuleiro_do_turno = self.__tabuleiro_inicial
        self.__contador_de_passes = 0
        self.__em_batalha = False

        self.compra_inicial()

    def compra_inicial(self):
        for i in range(5):
            self.__t1.comprar_carta()
            self.__t2.comprar_carta()

    @property
    def t1(self):
        return self.__t1

    @property
    def t2(self):
        return self.__t2

    @property
    def tabuleiros(self):
        return self.__tabuleiros

    @property
    def empate(self):
        return self.__empate

    @empate.setter
    def empate(self, valor):
        self.__empate = valor

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def codigo(self):
        return self.__codigo

    @property
    def ambos_vivos(self):
        return self.__ambos_vivos

    @ambos_vivos.setter
    def ambos_vivos(self, valor):
        self.__ambos_vivos = valor

    @property
    def vencedor(self):
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor):
        self.__vencedor = vencedor

    @property
    def perdedor(self):
        return self.__perdedor

    @perdedor.setter
    def perdedor(self, perdedor):
        self.__perdedor = perdedor

    @property
    def baralho_vencedor(self):
        return self.__baralho_vencedor

    @baralho_vencedor.setter
    def baralho_vencedor(self, baralho):
        self.__baralho_vencedor = baralho

    @property
    def baralho_perdedor(self):
        return self.__baralho_perdedor

    @baralho_perdedor.setter
    def baralho_perdedor(self, baralho):
        self.__baralho_perdedor = baralho

    @property
    def rodada(self):
        return self.__rodada

    def avancar_rodada(self):
        self.__rodada += 1
        for tabuleiro in self.__tabuleiros:
            if tabuleiro is not self.__atacante_rodada:
                self.__atacante_rodada = tabuleiro
                self.__tabuleiro_do_turno = tabuleiro
                break

        self.__t1.spellmana = min(
            self.__t1.spellmana + self.__t1.mana_atual, 3)
        self.__t2.spellmana = min(
            self.__t2.spellmana + self.__t2.mana_atual, 3)

        self.__t1.comprar_carta()
        self.__t2.comprar_carta()

        self.__ataque_ja_realizado = False
        self.__bloqueio_ja_realizado = False

        if self.__rodada <= 10:
            self.__t1.mana_total = self.__rodada
            self.__t1.mana_atual = self.__rodada
            self.__t2.mana_total = self.__rodada
            self.__t2.mana_atual = self.__rodada
        else:
            self.__t1.mana_total = 10
            self.__t1.mana_atual = 10
            self.__t2.mana_total = 10
            self.__t2.mana_atual = 10

    @property
    def atacante_rodada(self):
        return self.__atacante_rodada

    @property
    def ataque_ja_realizado(self):
        return self.__ataque_ja_realizado

    @property
    def tabuleiro_do_turno(self):
        return self.__tabuleiro_do_turno

    @property
    def contador_de_passes(self):
        return self.__contador_de_passes

    def contar_passe(self):
        self.__contador_de_passes += 1

    @property
    def em_batalha(self):
        return self.__em_batalha

    def realizar_batalha(self):
        for tabuleiro in self.__tabuleiros:
            if tabuleiro.codigo == self.__atacante_rodada.codigo:
                atacante = tabuleiro
            else:
                defensor = tabuleiro

        for i in range(len(atacante.monstros_em_batalha)):
            sobrepujar = False
            if atacante.monstros_em_batalha[i] is not None:
                if defensor.monstros_em_batalha[i] is not None:
                    for atributo in atacante.monstros_em_batalha[i].atributos:
                        if atributo.efeito == 'Sobrepujar':
                            sobrepujar = True

                    if sobrepujar:
                        dano_excedente = atacante.monstros_em_batalha[i].ataque - \
                            defensor.monstros_em_batalha[i].vida
                        if dano_excedente > 0:
                            defensor.vida_torre -= dano_excedente

                    atacante.monstros_em_batalha[i].vida -= defensor.monstros_em_batalha[i].ataque
                    defensor.monstros_em_batalha[i].vida -= atacante.monstros_em_batalha[i].ataque
                    if atacante.monstros_em_batalha[i].vida <= 0:
                        atacante.monstros_em_batalha[i] = None
                    else:
                        atacante.monstros.append(
                            atacante.monstros_em_batalha[i])

                    if defensor.monstros_em_batalha[i].vida <= 0:
                        defensor.monstros_em_batalha[i] = None
                    else:
                        defensor.monstros.append(
                            defensor.monstros_em_batalha[i])
                else:
                    defensor.vida_torre -= atacante.monstros_em_batalha[i].ataque
                    atacante.monstros.append(atacante.monstros_em_batalha[i])

        atacante.monstros_em_batalha = []
        defensor.monstros_em_batalha = []
        self.__em_batalha = False
        self.__tabuleiro_do_turno = defensor

        if defensor.vida_torre <= 0:
            self.__ambos_vivos = False

    def passar_a_vez(self):
        self.__contador_de_passes += 1
        self.mudar_turno()
        if self.__contador_de_passes == 2:
            self.__contador_de_passes = 0
            if not self.__em_batalha:
                self.avancar_rodada()
            else:
                self.realizar_batalha()

    def jogar_monstro(self, tabuleiro, monstro):
        if monstro.custo_mana > tabuleiro.mana_atual:
            raise ManaInsuficiente
        if len(tabuleiro.monstros) > 2:
            raise TabuleiroCheio
        tabuleiro.mana_atual -= monstro.custo_mana
        tabuleiro.jogar_monstro(monstro)
        self.__contador_de_passes = 0
        self.mudar_turno()

    def iniciar_ataque(self, monstros):
        if not monstros:
            raise AtaqueSemMonstros
        for tabuleiro in self.__tabuleiros:
            if tabuleiro.codigo != self.__atacante_rodada.codigo:
                tabuleiro.monstros_em_batalha = [None, None, None]
        self.__tabuleiro_do_turno.atacar(monstros)
        self.__contador_de_passes = 0
        self.__em_batalha = True
        self.__ataque_ja_realizado = True

    def realizar_bloqueio(self, tabuleiro, posicao, monstro):
        if (tabuleiro.monstros_em_batalha[posicao-1] is None):
            voar = False
            atacante_com_voar = False
            for atributo in monstro.atributos:
                if atributo.efeito == 'Voar':
                    voar = True
            if voar:
                tabuleiro.monstros.remove(monstro)
                tabuleiro.monstros_em_batalha[posicao-1] = monstro
            else:
                for atributo in self.__atacante_rodada.monstros_em_batalha[posicao-1].atributos:
                    if atributo.efeito == 'Voar':
                        atacante_com_voar = True
                if atacante_com_voar:
                    raise MonstroSemVoar
                tabuleiro.monstros.remove(monstro)
                tabuleiro.monstros_em_batalha[posicao-1] = monstro
        else:
            raise PosicaoOcupada
        self.__contador_de_passes = 0
        self.mudar_turno()

    def jogar_feitico(self, tabuleiro, feitico, tabuleiro_aplicado, posicao_em_batalha):
        if feitico.custo_mana > (tabuleiro.mana_atual + tabuleiro.spellmana):
            raise ManaInsuficiente
        custoinicial = feitico.custo_mana
        feitico.custo_mana -= tabuleiro.spellmana
        tabuleiro.spellmana -= min(custoinicial, 3)
        tabuleiro.mana_atual -= feitico.custo_mana
        tabuleiro.jogar_feitico(
            feitico, tabuleiro_aplicado, posicao_em_batalha)
        self.__contador_de_passes = 0
        self.mudar_turno()

    def mudar_turno(self):
        if (self.__tabuleiro_do_turno.codigo == self.t1.codigo):
            self.__tabuleiro_do_turno = self.t2
        else:
            self.__tabuleiro_do_turno = self.t1
