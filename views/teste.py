import PySimpleGUI as sg

# Layout da janela com um frame e um texto ao lado
layout = [
    [
        sg.Frame(
            layout=[
                [sg.Button('Botão 1')],
                [sg.Button('Botão 2')],
                [sg.Button('Botão 3')],
            ],
            title='Frame',
            relief=sg.RELIEF_SUNKEN,
            tooltip='Este é um tooltip para o frame',
        ),
        sg.Text('Texto ao Lado do Frame')
    ],
    [sg.Button('Sair')]
]

# Criação da janela
window = sg.Window('Exemplo de Frame com Texto', layout)

# Loop de eventos
while True:
    event, values = window.read()

    # Tratamento de eventos
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

# Fechamento da janela
window.close()
