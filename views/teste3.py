import PySimpleGUI as sg

monstros_j1 = [0]

# Função para criar o layout de uma carta
def criar_layout_carta(nome, ataque, vida, atributo):
    return [
        [sg.Text(f"Nome: {nome}")],
        [sg.Text(f"Atributo: {atributo}")],
        [sg.Text(f"Ataque: {ataque}   Vida: {vida}")]
    ]

# Crie o layout da janela com as colunas e retângulos para cada carta
layout = [[]]

# Verifica se há monstros na lista antes de iterar
if monstros_j1[0] > 0:
    # Itera sobre os dados dos monstros do jogador 1
    for i in range(1, len(monstros_j1), 4):
        nome = monstros_j1[i]
        ataque = monstros_j1[i + 1]
        vida = monstros_j1[i + 2]
        atributo = monstros_j1[i + 3]

        frame = sg.Frame(f"Monstro {i // 4 + 1}", criar_layout_carta(nome, ataque, vida, atributo), key=f"-FRAME-{nome}-")
        layout[0].append(frame)

# Cria a janela e exibe
window = sg.Window("Exemplo de Monstros", layout, finalize=True)
event, values = window.read()
window.close()
