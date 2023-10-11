from copy import deepcopy
class Tabuleiro:
    def __init__(self, codigo: str, jogador, baralho):
    
        self.__codigo = codigo
        self.__jogador = jogador
        self.__vida_torre = 20
        self.__baralho = deepcopy(baralho)
        self.__cartas_na_mao = []
        self.__monstros = []
        self.__mana_atual = 1
        self.__mana_total = 1
        self.__spellmana = 0
        self.__monstros_em_batalha = []
    
    
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo
        
    @property
    def jogador(self):
        return self.__jogador
    @jogador.setter
    def jogador(self,jogador):
        self.__jogador = jogador
        
    @property
    def vida_torre(self):
        return self.__vida_torre
    @vida_torre.setter
    def vida_torre(self,vida_torre):
        self.__vida_torre = vida_torre
    
    @property
    def baralho(self):
        return self.__baralho
    @baralho.setter
    def baralho(self,baralho):
        self.__baralho = baralho
    
    @property
    def cartas_na_mao(self):
        return self.__cartas_na_mao
    def comprar_carta(self):
        self.__cartas_na_mao.append(self.__baralho.pop(0))
            
    @property
    def monstros(self):
        return self.__monstros
    
    def jogar_monstro(self,monstro):    
        self.__monstros.append(monstro)
        self.__cartas_na_mao.remove(monstro)
    
    def jogar_feitico(self,feitico,tabuleiro_aplicado,posicao_em_batalha):
        if tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1] == None:
            raise AlvoInvalido
        self.__cartas_na_mao.remove(feitico)
        if feitico.modificacao == 'aumentar':
            if feitico.atributo == 'ataque':                
                tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1].ataque += feitico.valor #ver se pode ser dessa forma o setter
            else:
                tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1].vida += feitico.valor
        else:
            if feitico.atributo == 'ataque':                
                tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1].ataque -= feitico.valor #ver se pode ser dessa forma o setter
            else:
                tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1].vida -= feitico.valor
                if tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1].vida <= 0:
                    tabuleiro_aplicado.monstros.remove(tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1])
                    tabuleiro_aplicado.monstros_em_batalha[posicao_em_batalha-1] = None
        
        

    def eliminar_monstro(self,monstro):
        self.__monstros.remove(monstro)
        
    @property
    def mana_atual(self):
        return self.__mana_atual
    @mana_atual.setter
    def mana_atual(self,quantidade):
        self.__mana_atual = quantidade
    
    @property
    def mana_total(self):
        return self.__mana_total
    @mana_total.setter
    def mana_total(self,quantidade):
        self.__mana_total = quantidade
    
    @property
    def spellmana(self):
        return self.__spellmana
    @spellmana.setter
    def spellmana(self,quantidade):
        self.__spellmana = quantidade
    
    @property
    def monstros_em_batalha(self):
        return self.__monstros_em_batalha
    @monstros_em_batalha.setter
    def monstros_em_batalha(self,monstros):
        self.__monstros_em_batalha = monstros
        
    def atacar(self, monstros):
        self.__monstros_em_batalha.append(monstros)
        for monstro in monstros:
            self.__monstros.remove(monstro)
    def definir_bloqueador(self,posicao): #o controlador vai ver se a posição pode ser passada ou nao (se ja tem monstro ou maior q 6)
        if posicao == 0:
            self.__monstros_em_batalha.append(None)
        else:
            self.__monstros_em_batalha.append(self.__monstros[posicao-1])
            self.__monstros.remove(self.__monstros[posicao-1])
        
            return self.__monstros[posicao-1]

    
    
    
        
            
    
        