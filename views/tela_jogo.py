from errors.voltar import Voltar
from models.monstro import Monstro


class TelaJogo:
    def __init__(self):
        pass

    def mostra_msg(self, mensagem):
        print(mensagem)

    def mostra_dados_jogo(self, jogo):
        print(f'Codigo do jogo: {jogo.codigo}')
        print()
        print('Jogadores:')
        for tabuleiro in jogo.tabuleiros:
            print(
                f'{tabuleiro.jogador.nome}. Baralho utilizado: {tabuleiro.baralho.nome}')
        print()
        if jogo.empate:
            print('Jogo empatado.')
        else:
            print(f'Vencedor: {jogo.vencedor.nome}')
            print(f'Perdedor: {jogo.perdedor.nome}')

    def mostrar_dados_jogador_rodada(self, dados_jogador):
        print('\n---')
        print(f'JOGADOR: {dados_jogador["nome"]}')
        print(f'VIDA DA TORRE: {dados_jogador["vida_torre"]}')
        print(f'MANA: {dados_jogador["mana"]}')
        print(f'MANA DE FEITICO:{dados_jogador["spellmana"]}')
        print('MONSTROS NO TABULEIRO: ', end='')
        for monstro in dados_jogador['monstros_tabuleiro']:
            print(
                f'{monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida}', end=' || ')
        print('\nMONSTROS EM BATALHA: ', end='')
        for monstro in dados_jogador['monstros_em_batalha']:
            if (monstro is not None):
                print(
                    f'{monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida}', end=' || ')

    def mostra_dados_da_rodada(self, dados_rodada):
        print('\n')
        print(
            '---------------------------------------------------------'
            f'RODADA {dados_rodada["rodada"]}--------------------------'
            '-------------------------------')
        print(
            f'ATACANTE DA RODADA: {dados_rodada["atacante_rodada"].jogador.nome}')
        print("\n")

    def mostra_dados_do_turno(self, dados_turno):
        print("\n")
        print('-----------------------')
        print(f'VEZ DO JOGADOR: {dados_turno["jogador_atual"]}')
        print(f'MANA: {dados_turno["mana"]}')
        print(f'MANA DE FEITICO:{dados_turno["spellmana"]}')
        print('-----------------------')

    def opcoes_tela(self):
        print('\n')
        print('-------- OPÇÕES DE JOGO --------')
        valores = [0, 1, 2]
        while True:
            print('1 - Iniciar partida')
            print('2 - Histórico de partidas jogadas')
            print('0 - Voltar')
            try:
                opcao = int(input('Escolha a opção: '))
                if opcao not in valores:
                    raise ValueError
                break
            except ValueError:
                print('Digite uma opção válida!')
        return opcao

    def opcoes_turno(self, em_batalha: bool):
        print('\n')
        print('-------- OPÇÕES --------')
        opcoes_validas = [0, 1, 2, -1]
        print('DESISTIR: -1')
        print('PASSAR A VEZ: 0')
        if not em_batalha:
            print('JOGAR MONSTRO: 1')
            print('INICIAR ATAQUE: 2')
        else:
            print('JOGAR FEITICO: 1')
            print('REALIZAR BLOQUEIO: 2')
        print('\n')
        opcao = int(input('Escolha uma opção:'))

        if opcao not in opcoes_validas:
            raise ValueError

        return opcao

    def mostra_dados_em_lista_de_cartas(self, lista_cartas):
        posicao = 0
        for carta in lista_cartas:
            posicao += 1
            print(f'Carta {posicao}: ')
            print(carta.codigo)
            print(carta.custo_mana)
            if isinstance(carta, Monstro):
                print('Tipo: Monstro')
                print(f'Ataque: {carta.ataque}')
                print(f'Vida: {carta.vida}')
                if carta.atributos:
                    print('Atributos:', end=' ')
                    for atributo in carta.atributos:
                        print(atributo.efeito, end=' ')
                    print('', end='\n')
            else:
                print('Tipo: Feitiço')
                print(f'Modificação: {carta.modificacao}')
                print(f'Atributo: {carta.atributo_modificado}')
                print(f'Valor: {carta.valor}')
            print()

    def pega_posicao_carta_em_lista(self, posicoes_disponiveis):
        while True:
            try:
                posicao_carta_escolhida = int(input('Escolha a posição da carta ou tecle "-1" para voltar'
                                                    ' para a tela de opções: '))

                if posicao_carta_escolhida == -1:
                    raise Voltar
                if posicao_carta_escolhida < 1 or posicao_carta_escolhida > \
                        posicoes_disponiveis:
                    raise ValueError

                return posicao_carta_escolhida

            except ValueError:
                print('Escoha uma opção válida!')
                print()

    def pega_inteiro(self):
        return int(input())

    def pega_string(self):
        string = input()
        if string.lower() == 'v':
            raise Voltar
        return string
