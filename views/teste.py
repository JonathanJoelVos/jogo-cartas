import PySimpleGUI as sg

# Defina o layout do frame interno
inner_frame_layout = [
    [sg.Text('Informações destacadas', justification='center')],
    [sg.Text('Detalhe 1')],
    [sg.Text('Detalhe 2')],
    [sg.Frame('Detalhe Destacado', [[sg.Text('Detalhe 1 Destacado')]]), sg.Frame("CARTA 2",
                                      [
                                          [sg.Text(f'Nome: leo')],
                                          [sg.Text(f'Atributos: voar')],
                                          [sg.Text(f'Ataque: 5'),
                                           sg.Text(f'Vida: 10')]
                                      ])]  # Novo Frame para destacar Detalhe 1
]

# Crie o frame interno
inner_frame = sg.Frame('Destaque', inner_frame_layout)

# Defina o layout geral
layout = [
    [sg.Text('Conteúdo fora do frame interno')],
    [inner_frame],
    [sg.Button('OK')]
]

# Crie a janela
window = sg.Window('Exemplo de Destaque com Frame Interno', layout)

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'OK':
        break

# Feche a janela
window.close()
