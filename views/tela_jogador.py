class TelaJogador():
    def tela_opcoes(self):
        print('Escolha uma opção:')
        print('\n')
        print('---------Jogador---------')
        print('1 - Incluir jogador')
        print('2 - Alterar jogador')
        print('3 - Excluir jogador')
        print('4 - Listar jogadores')
        print('5 - Opções de baralho')
        print('0 - Voltar')
        print('\n')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def mostra_jogador(self, dados_jogador):
        print("\n")
        print('NOME: ', dados_jogador["nome"])
        print('PARTIDAS JOGADAS: ', dados_jogador["partidas_jogadas"])
        print('VITÓRIAS: ', dados_jogador["vitorias"])
        print('DERROTAS: ', dados_jogador["derrotas"])
        print('PONTOS: ', dados_jogador["pontos"])
        print('\n')

    def seleciona_jogador(self):
        nome = str(input('Nome do jogador: '))
        return nome

    def pega_dados_jogador(self):
        nome = str(input('Nome: '))
        return {
            'nome': nome,
            'baralhos': [],
            'partidas_jogadas': 0,
            'vitorias': 0,
            'derrotas': 0,
            'pontos': 0
        }

    def tela_opcoes_baralho(self):
        print('\n')
        print('---------Baralho---------')
        print('1 - Listar baralhos')
        print('2 - Incluir baralho')
        print('3 - Alterar baralho')
        print('4 - Excluir baralho')
        print('5 - Adicionar carta ao baralho')
        print('6 - Remover carta do baralho')
        print('7 - Listar cartas do baralho')
        print('0 - Voltar')
        print('\n')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def seleciona_baralho(self):
        nome = str(input('Nome do baralho: '))
        return nome

    def mostra_baralho(self, dados_baralho):
        print('\n')
        print('---------Dados Baralho---------')
        print('NOME: ', dados_baralho["nome"])
        print('\n')

    def pega_dados_baralho(self):
        nome = str(input('Nome: '))

        return {
            'nome': nome,
            'cartas': []
        }

    def mostra_msg(self, msg):
        print('\n')
        print(msg)
        print('\n')
