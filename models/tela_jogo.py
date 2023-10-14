from errors.tipo_de_carta_errado import TipoDeCartaErrado
from errors.voltar import Voltar
from models.monstro import Monstro


class TelaJogo:
    def __init__(self):
        pass

    def mostra_msg(self, mensagem):
        print(mensagem)

    def opcoes_turno(self, em_batalha: bool):
        opcoes_validas = [0, 1, 2]
        print('Escolha uma opção:')
        print('Passar a vez: digite "0"')
        if not em_batalha:
            print('Jogar monstro: digite "1"')
            print('Iniciar ataque: digite "2"')
        else:
            print('Jogar feitiço: digite "1"')
            print('Realizar Bloqueio: digite "2"')
        opcao = int(input())
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
                print(f'Atributo: {carta.atributo}')
                print(f'Valor: {carta.valor}')
            print()

    def pega_posicao_carta_em_lista(self, lista_cartas):
        posicoes_disponiveis = len(lista_cartas)
        while True:
            try:
                posicao_carta_escolhida = input('Escolha a posição da carta ou tecle "v" para voltar'
                                                ' para a tela de opções: ')

                if posicao_carta_escolhida.lower() == 'v':
                    raise Voltar

                posicao_carta_escolhida = int(posicao_carta_escolhida)
                if posicao_carta_escolhida < 1 or posicao_carta_escolhida > posicoes_disponiveis:
                    raise ValueError
                break

            except ValueError:
                print('Escoha uma opção válida!')
                print()

            return posicao_carta_escolhida

    def pega_inteiro(self):
        return int(input())

    def pega_string(self):
        string = input()
        if string.lower() == 'v':
            raise Voltar
