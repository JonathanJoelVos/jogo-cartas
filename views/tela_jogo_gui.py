from errors.voltar import Voltar
from PySimpleGUI import PySimpleGUI as sg


class TelaJogo:
    def __init__(self):
        pass


    def opcoes_tela(self):
        layout = [
            [sg.Text("Escolha uma opção:", justification='center')],
            [sg.Radio("Iniciar Partida", "OPCOES", key='1')],
            [sg.Radio("Histórico de Partidas de um Jogador", "OPCOES", key='2')],
            [sg.Radio("Voltar", "OPCOES", key='0', default=True)],
            [sg.Button("Submeter", size=(20, 1), pad=((10, 10), 3))]
        ]


        window = sg.Window("OPÇÕES DE JOGO", layout)

        opcao_selecionada = '0'

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                opcao_selecionada = next((key for key, value in values.items() if value), None)
                break

        window.close()

        return opcao_selecionada

    def mostra_msg(self, mensagem):
        layout = [[sg.Text(mensagem)],
                  [sg.Button('Continuar')]]
        window = sg.Window(mensagem, layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Continuar":
                break

        window.close()

    def mostra_dados_do_turno(self, dados_turno):

        layout = [[sg.Text(f'RODADA {dados_turno['rodada']}',  size=(20, 1), font=('Helvetica', 20))],
                  [sg.Text(f'ATACANTE DA RODADA: {dados_turno['atacante']}'), sg.Text(f'CONTADOR DE PASSES: {dados_turno['contador_de_passes']}'), sg.Text(f'EM BATALHA: {dados_turno['em_batalha']}')],
                  [sg.Text(f'VEZ DE {dados_turno['turno']}')]
                  [sg.Column([
                      [sg.Text(f'JOGADOR: {dados_turno['j1']}')],
                      [sg.Text(f'VIDA DA TORRE: {dados_turno['vida_j1']}')],
                      [sg.Text(f'MANA: {dados_turno['mana_j1']}')],
                      [sg.Text(f'MANA DE FEITIÇO: {dados_turno['spellmana_j1']}')]
                  ]), #talvez adicionar size
                  [sg.Column([

                  ])]
                  ]
                  ]

