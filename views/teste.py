import PySimpleGUI as sg

# Função para criar o layout de uma carta
def criar_layout_carta(nome, mana, ataque, vida, imagem_path):
    return [
        [sg.Text(f"Nome: {nome}")],
        [sg.Text(f"Mana: {mana}")],
        [sg.Text(f"Ataque: {ataque}")],
        [sg.Text(f"Vida: {vida}")]
    ]

# Defina os atributos das cartas (substitua esses valores pelos atributos reais das suas cartas)
cartas = [
    {"nome": f"Carta {i+1}", "mana": i+2, "ataque": i+3, "vida": i+1, "imagem_path": "path_para_imagem.png"} for i in range(20)
]

# Organize as cartas em duas fileiras
num_cartas_por_linha = 10
linhas = [cartas[i:i+num_cartas_por_linha] for i in range(0, len(cartas), num_cartas_por_linha)]

# Crie o layout da janela com as linhas e retângulos para cada carta
layout = [
    [
        sg.Column([
            [
                sg.Frame(f"Carta {j + 1 + i*num_cartas_por_linha}", criar_layout_carta(**carta), key=f"-FRAME-{carta['nome']}-") for j, carta in enumerate(linha)
            ]
        ]) for i, linha in enumerate(linhas)
    ],
    [sg.Button("Fechar")]
]

# Crie a janela
window = sg.Window("Cartas do Jogo", layout, finalize=True)

# Loop de eventos
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Fechar"):
        break

# Feche a janela
window.close()
