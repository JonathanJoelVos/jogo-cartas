import PySimpleGUI as sg


class TelaJogador():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Jogador ----------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir jogador', "RD1", key='1')],
            [sg.Radio('Alterar jogador', "RD1", key='2')],
            [sg.Radio('Excluir jogador', "RD1", key='3')],
            [sg.Radio('Listar jogadores', "RD1", key='4')],
            [sg.Radio('Opções de baralho', "RD1", key='5')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de jogador').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        print(values, 'values')
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def mostra_jogador(self, dados_layout):

        layout = [
            [sg.Table(values=dados_layout, headings=['Nome', 'Partidas',
                      'Vitórias', 'Derrotas', 'Pontos'],
                      auto_size_columns=True)],
            [sg.Button('Ok')]
        ]

        self.__window = sg.Window('Jogadores').Layout(layout)
        button, values = self.open()
        self.close()

        # string_info_jogador += "NOME: " + dados_jogador["nome"] + '\n'
        # string_info_jogador += "PARTIDAS JOGADAS: " +
        # str(dados_jogador["partidas_jogadas"]) + '\n'
        # string_info_jogador += "VITÓRIAS: " +
        # str(dados_jogador["vitorias"]) + '\n'
        # string_info_jogador += "DERROTAS: " +
        # str(dados_jogador["derrotas"]) + '\n'
        # string_info_jogador += "PONTOS: " +
        # str(dados_jogador["pontos"]) + '\n\n'

        # sg.Popup('-------- INFORMAÇÕES DO JOGADOR ----------',
        #          string_info_jogador)

        # sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_amigos)
        # print("\n")
        # print('NOME: ', dados_jogador["nome"])
        # print('PARTIDAS JOGADAS: ', dados_jogador["partidas_jogadas"])
        # print('VITÓRIAS: ', dados_jogador["vitorias"])
        # print('DERROTAS: ', dados_jogador["derrotas"])
        # print('PONTOS: ', dados_jogador["pontos"])
        # print('\n')

    def pega_nome_jogador(self):
        print('chamou2')
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- JOGADOR ----------',
                     font=("Helvica", 25))],
            [sg.Text('Digite o nome do jogador:',
                     font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona jogador').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def seleciona_jogador(self):
        print('chamou1')
        nome = self.pega_nome_jogador()
        return nome
        nome = str(input('Nome do jogador: '))
        return nome

    def pega_dados_jogador(self):
        nome = self.pega_nome_jogador()
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

    def mostra_ranking(self, dados_jogador, posicao):
        print('\n')
        print(f'----- Posiçao {posicao} ------')
        print('NOME: ', dados_jogador["nome"])
        print('PARTIDAS JOGADAS: ', dados_jogador["partidas_jogadas"])
        print('VITÓRIAS: ', dados_jogador["vitorias"])
        print('DERROTAS: ', dados_jogador["derrotas"])
        print('PONTOS: ', dados_jogador["pontos"])
        print('\n')

    def mostra_msg(self, msg):
        print('\n')
        print(msg)
        print('\n')
