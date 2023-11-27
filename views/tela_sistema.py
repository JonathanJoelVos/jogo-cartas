import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Magia Medieval: Confronto dos Reinos', font=("Helvica", 25), text_color='#f0ad8b')],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('Acessar jogadores', "RD1", key='1', default=True)],
            [sg.Radio('Opções de jogo', "RD1", key='2')],
            [sg.Radio('Ranking de jogadores', "RD1", key='3')],
            [sg.Radio('Opções de cartas', "RD1", key='4')],
            [sg.Button('Confirmar', button_color=('white', 'green')),
             sg.Cancel('Sair do Jogo', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Jogo').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4

        if button in (None, 'Sair do Jogo'):
            opcao = 0
        self.close()
        return opcao
