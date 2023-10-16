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

    def mostrar_tabuleiros(self, dados_tabuleiro):
        print('-----------------------------------------------------------------')
        print(f'{dados_tabuleiro["jogador_1"]} - VIDA DA TORRE: {dados_tabuleiro["vida_torre_t1"]}')
        print()
        print('MONSTROS NO TABULEIRO: ', end='')
        posicao = 0
        for monstro in dados_tabuleiro['monstros_tabuleiro_1']:
            posicao += 1
            atributos = [atributo.efeito for atributo in monstro.atributos]

            if atributos:
                atributos_str = ", ".join(atributos)
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
            else:
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: || '

            print(mensagem, end=' ')
            print()

        print()
        print('\nMONSTROS EM BATALHA: ', end='')
        posicao = 0
        for monstro in dados_tabuleiro['monstros_em_batalha_1']:
            posicao += 1
            if monstro is not None:
                atributos = [atributo.efeito for atributo in monstro.atributos]

                if atributos:
                    atributos_str = ", ".join(atributos)
                else:
                    atributos_str = "||"

                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
                print(mensagem, end=' ')
        print('\n-----------------------------------------------------------------')
        print('-----------------------------------------------------------------')
        print('MONSTROS EM BATALHA: ', end='')
        posicao = 0
        for monstro in dados_tabuleiro['monstros_em_batalha_2']:
            posicao += 1
            if monstro is not None:
                atributos = [atributo.efeito for atributo in monstro.atributos]

                if atributos:
                    atributos_str = ", ".join(atributos)
                else:
                    atributos_str = "||"

                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
                print(mensagem, end=' ')
        print('\n')
        print('MONSTROS NO TABULEIRO: ', end='')
        posicao = 0
        for monstro in dados_tabuleiro['monstros_tabuleiro_2']:
            posicao += 1
            atributos = [atributo.efeito for atributo in monstro.atributos]

            if atributos:
                atributos_str = ", ".join(atributos)
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
            else:
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: || '

            print(mensagem, end=' ')
            print()
        print()
        print(f'{dados_tabuleiro["jogador_2"]} - VIDA DA TORRE:{dados_tabuleiro["vida_torre_t2"]} ')
        print('\n-----------------------------------------------------------------')


    def mostrar_dados_jogador_rodada(self, dados_jogador):
        print('\n---')
        print(f'JOGADOR: {dados_jogador["nome"]}')
        print(f'VIDA DA TORRE: {dados_jogador["vida_torre"]}')
        print(f'MANA: {dados_jogador["mana"]}')
        print(f'MANA DE FEITICO:{dados_jogador["spellmana"]}')
        print('MONSTROS NO TABULEIRO: ', end='')
        posicao = 0
        for monstro in dados_jogador['monstros_tabuleiro']:
            posicao += 1
            atributos = [atributo.efeito for atributo in monstro.atributos]

            if atributos:
                atributos_str = ", ".join(atributos)
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
            else:
                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: || '

            print(mensagem, end=' ')

        print('\nMONSTROS EM BATALHA: ', end='')
        posicao = 0
        #for monstro in dados_jogador['monstros_em_batalha']:
            #posicao += 1
            #if (monstro is not None):
                #print(
                    #f'{monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida}', end=' || ')

        for monstro in dados_jogador['monstros_em_batalha']:
            posicao += 1
            if monstro is not None:
                atributos = [atributo.efeito for atributo in monstro.atributos]

                if atributos:
                    atributos_str = ", ".join(atributos)
                else:
                    atributos_str = "||"

                mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
                print(mensagem, end=' ')

    def mostra_dados_da_rodada(self, dados_rodada):
        print('\n')
        print(
            '---------------------------------------------------------'
            f'RODADA {dados_rodada["rodada"]}--------------------------'
            '-------------------------------')
        print(f'VEZ DO(A) JOGADOR(A): {dados_rodada["tabuleiro_turno"]}')
        print(
            f'ATACANTE DA RODADA: {dados_rodada["atacante_rodada"].jogador.nome}')
        print(f'ATAQUE JÁ REALIZADO: {dados_rodada["ataque_realizado"]}')
        print(f'Está acontecendo uma batalha? {dados_rodada["em_batalha"]}')
        print(f'Contador de passes: {dados_rodada["contador_de_passes"]}')
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

    def opcoes_turno(self, em_batalha: bool, nome_jogador):
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

        if not em_batalha:
            if opcao == 0:
                print(f'{nome_jogador} passou a vez!')
            elif opcao == 1:
                print(f'{nome_jogador} escolheu JOGAR MONSTRO')
            elif opcao == 2:
                print(f'{nome_jogador} escolheu INICIAR ATAQUE')
        else:
            if opcao == 0:
                print(f'{nome_jogador} passou a vez!')
            elif opcao == 1:
                print(f'{nome_jogador} escolheu JOGAR FEITIÇO')
            else:
                print(f'{nome_jogador} escolheu REALIZAR BLOQUEIO')

        return opcao

    def mostra_dados_em_lista_de_cartas(self, lista_cartas):
        posicao = 0
        for carta in lista_cartas:
            if carta is not None:
                posicao += 1
                print(f'POSIÇÃO: {posicao}: ')
                if isinstance(carta, Monstro):
                    print('TIPO: Monstro')
                    print(f'CUSTO MANA: {carta.custo_mana}')
                    print(f'CÓDIGO: {carta.codigo}')
                    print(f'NOME: {carta.nome}')
                    print(f'ATAQUE: {carta.ataque}')
                    print(f'VIDA: {carta.vida}')
                    if carta.atributos:
                        print('ATRIBUTOS:', end=' ')
                        for atributo in carta.atributos:
                            print(atributo.efeito, end=' ')
                        print('', end='\n')
                else:
                    print('TIPO: Feitiço')
                    print(f'CUSTO MANA: {carta.custo_mana}')
                    print(f'CÓDIGO: {carta.codigo}')
                    print(f'NOME: {carta.nome}')
                    print(f'MODIFICAÇÃO: {carta.modificacao}')
                    print(f'ATRIBUTO: {carta.atributo_modificado}')
                    print(f'VALOR: {carta.valor}')
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

    def tela_escolhe_tabuleiro_feitico(self):
        print()
        print('O feitiço será aplicado em um monstro aliado ou um inimigo?')

        print('Digite "a" para aliado, "i" para inimigo ou "v" para voltar para'
                                    ' a tela de opções')
        string = input()
        while string != 'a' and string != 'i':
            if string.lower() == 'v':
                raise Voltar
            print('Escolha uma opção válida')
            print('Digite "a" para aliado, "i" para inimigo ou "v" para voltar para'
                  ' a tela de opções')
            string = input()

        return string.lower()

    def tela_tabuleiro_cheio(self, dados_tabuleiro):
        print('Tabuleiro cheio. Digite "v" para voltar para a tela de opções ou '
              'outra tecla para escolher um monstro aliado para ser'
              ' eliminado.')

        string = input()
        if string.lower() == 'v':
            raise Voltar

        self.mostrar_tabuleiros(dados_tabuleiro)
        print('Selecione um monstro aliado para ser substituído pela carta escolhida:')

    def pega_string(self):
        string = input()
        if string.lower() == 'v':
            raise Voltar
        return string
