import PySimpleGUI as sg


class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Sistemas ----------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('Acessar jogadores', "RD1", key='1')],
            [sg.Radio('Opções de jogo', "RD1", key='2')],
            [sg.Radio('Ranking de jogadores', "RD1", key='3')],
            [sg.Radio('Opções de cartas', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistemas').Layout(layout)

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

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
