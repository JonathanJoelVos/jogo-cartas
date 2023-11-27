import PySimpleGUI as sg


class TelaJogador():
    def __init__(self):
        self.__window = None
        self.init_opcoes_jogador()

    def init_opcoes_jogador(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Jogador ----------', font=("Helvica", 25), text_color='#f0ad8b')],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('Incluir jogador', "RD1", key='1')],
            [sg.Radio('Alterar jogador', "RD1", key='2')],
            [sg.Radio('Excluir jogador', "RD1", key='3')],
            [sg.Radio('Listar jogadores', "RD1", key='4')],
            [sg.Radio('Opções de baralho', "RD1", key='5')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')),
             sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Sistema de jogador').Layout(layout)

    def init_opcoes_baralho(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Baralhos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('Listar baralhos', "RD1", key='1')],
            [sg.Radio('Incluir baralho', "RD1", key='2')],
            [sg.Radio('Alterar baralho', "RD1", key='3')],
            [sg.Radio('Excluir baralho', "RD1", key='4')],
            [sg.Radio('Adicionar carta ao baralho', "RD1", key='5')],
            [sg.Radio('Remover carta do baralho', "RD1", key='6')],
            [sg.Radio('Listar cartas do baralho', "RD1", key='7')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar', button_color=('white', 'green')),
             sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Baralhos').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_opcoes_jogador()
        button, values = self.open()
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
            [sg.Button('Ok', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('Jogadores').Layout(layout)
        button, values = self.open()
        self.close()

    def pega_nome_jogador(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Digite o nome do jogador:',
                     font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar', button_color=('white', 'green')),
             sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Seleciona jogador').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def seleciona_jogador(self):
        nome = self.pega_nome_jogador()
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
        self.init_opcoes_baralho()
        button, values = self.open()
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
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def pega_nome_baralho(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Digite o nome do baralho:',
                     font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar', button_color=('white', 'green')),
             sg.Cancel('Cancelar', button_color=('white', 'green'))]
        ]
        self.__window = sg.Window('Seleciona baralho').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome

    def seleciona_baralho(self):
        nome = self.pega_nome_baralho()
        return nome

    def mostra_baralho(self, dados_baralho):
        layout = [
            [sg.Table(values=dados_baralho, headings=['Baralhos'],
                      auto_size_columns=True)],
            [sg.Button('Ok', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('Cartas').Layout(layout)
        button, values = self.open()
        self.close()

    def pega_dados_baralho(self):
        nome = self.pega_nome_baralho()

        return {
            'nome': nome,
            'cartas': []
        }

    def mostra_ranking(self, dados_jogador):
        layout = [
            [sg.Table(values=dados_jogador, headings=['Nome', 'Partidas',
                      'Vitórias', 'Derrotas', 'Pontos', 'Posição'],
                      auto_size_columns=True)],
            [sg.Button('Ok', button_color=('white', 'green'))]
        ]

        self.__window = sg.Window('Ranking').Layout(layout)
        button, values = self.open()
        self.close()

    def mostra_msg(self, msg):
        sg.popup("", msg)
