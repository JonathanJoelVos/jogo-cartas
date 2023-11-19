import PySimpleGUI as sg


class TelaCarta:
    def tela_opcoes(self):
        layout = [
            [sg.Text("Escolha uma opção:")],
            [sg.Radio("Incluir Carta", "OPCOES", key=1)],
            [sg.Radio("Listar Cartas", "OPCOES", key=2)],
            [sg.Radio("Excluir Carta", "OPCOES", key=3)],
            [sg.Radio("Alterar Carta", "OPCOES", key=4)],
            [sg.Radio("Voltar", "OPCOES", key=0, default=True)],
            [sg.Button("Submeter")]
        ]

        window = sg.Window("Jogo de Cartas", layout, resizable=True)

        opcao_selecionada = 0

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                opcao_selecionada = next((key for key, value in values.items() if value), None)

                break

        window.close()

        print(opcao_selecionada)
        return opcao_selecionada



