from errors.voltar import Voltar
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark')


class TelaJogo:
    def __init__(self):
        pass

    def opcoes_tela(self):
        layout = [
            [sg.Text('-------- JOGOS ----------',
                     font=("Helvica", 25), text_color='#f0ad8b')],
            [sg.Text("Escolha uma opção:", justification='center')],
            [sg.Radio("Iniciar Partida", "OPCOES", key='1')],
            [sg.Radio("Histórico de Partidas de um Jogador", "OPCOES", key='2')],
            [sg.Radio("Voltar", "OPCOES", key='0', default=True)],
            [sg.Button("Submeter", button_color=('white', 'green'),
                       size=(20, 1), pad=((10, 10), 3))]
        ]

        window = sg.Window("OPÇÕES DE JOGO", layout)

        opcao_selecionada = '0'

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                opcao_selecionada = next(
                    (key for key, value in values.items() if value), None)
                break

        window.close()

        return opcao_selecionada

    def mostra_msg(self, mensagem):
        layout = [[sg.Text(mensagem)],
                  [sg.Button("Continuar", button_color=('white', 'green'))]]
        window = sg.Window(mensagem, layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Continuar":
                break

        window.close()

    def mostra_dados_do_turno(self, dados_turno):

        largura_janela = 1100
        altura_janela = 650

        monstros_j1 = dados_turno['dados_monstros'][0]
        monstros_j1_batalha = dados_turno['dados_monstros'][1]
        monstros_j2 = dados_turno['dados_monstros'][2]
        monstros_j2_batalha = dados_turno['dados_monstros'][3]

        layout = [
            [sg.Frame('', [
                [
                    sg.Text(f'RODADA {dados_turno["rodada"]}', font=(
                        'Helvetica', 15), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('ATACANTE DA RODADA:', font=('Helvetica', 12)),
                    sg.Text(f'{dados_turno["atacante"].upper()}', font=(
                        'Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('CONTADOR DE PASSES:', font=('Helvetica', 12)),
                    sg.Text(f'{dados_turno["contador_de_passes"]}', font=(
                        'Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('EM BATALHA:', font=('Helvetica', 12)),
                    sg.Text(f'{str(dados_turno["em_batalha"]).upper()}', font=(
                        'Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('VEZ DE', font=('Helvetica', 13)),
                    sg.Text(f'{dados_turno["turno"].upper()}', font=(
                        'Helvetica', 12)),
                ],
            ])],
            [
                self.criar_layout_monstros_j1(monstros_j1, dados_turno["j1"], dados_turno["turno"],
                                              dados_turno["em_batalha"], dados_turno["atacou"],
                                              dados_turno["contador_de_passes"])
            ],
            [
                self.criar_layout_batalha_j1(monstros_j1_batalha, dados_turno["j1"],
                                             dados_turno["vida_j1"], dados_turno["mana_j1"],
                                             dados_turno["spellmana_j1"])
            ],
            [
                sg.Frame('', [[sg.Text('', size=(105, 1))]])
            ],
            [
                sg.Frame(f'{dados_turno["j2"].upper()}', [
                    [sg.Text(f'Vida da Torre: {dados_turno["vida_j2"]}')],
                    [sg.Text(f'Mana: {dados_turno["mana_j2"]}')],
                    [sg.Text(
                        f'Mana de Feitiço: {dados_turno["spellmana_j2"]}')]
                ], background_color='#275245'),
                self.criar_layout_batalha_j2(
                    monstros_j2_batalha, dados_turno["j2"])

            ],
            [
                self.criar_layout_monstros_j2(monstros_j2, dados_turno["j2"], dados_turno["turno"],
                                              dados_turno["em_batalha"], dados_turno["atacou"],
                                              dados_turno["contador_de_passes"])
            ]
        ]

        window = sg.Window('Tabuleiro', layout, size=(
            largura_janela, altura_janela))

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                return ('GAME OVER', window)

            elif event == "Confirmar":
                opcao_selecionada = next(
                    (key for key, value in values.items() if value), None)
                break

        if opcao_selecionada is not None:
            opcao_selecionada = (int(opcao_selecionada))

        return (opcao_selecionada, window)

    def criar_layout_monstros_j1(self, dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou,
                                 contador_de_passes):
        layout_monstros_j1 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_monstros_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')], ]))

        if dados_monstros[0] >= 1:
            layout_monstros_j1.append(sg.Frame("",
                                               [[sg.Text('CARTA 1                  ')],
                                                [sg.Text(
                                                    f'Nome: {dados_monstros[1]}')],
                                                [sg.Text(
                                                    f'Atributos: {dados_monstros[4]}')],
                                                [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                 sg.Text(f'Vida: {dados_monstros[3]}')]
                                                ]))
        if dados_monstros[0] >= 2:
            layout_monstros_j1.append(sg.Frame("",
                                               [[sg.Text('CARTA 2                  ')],
                                                [sg.Text(
                                                    f'Nome: {dados_monstros[5]}')],
                                                [sg.Text(
                                                    f'Atributos: {dados_monstros[8]}')],
                                                [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                 sg.Text(f'Vida: {dados_monstros[7]}')]
                                                ]))
        if dados_monstros[0] == 1:
            for i in range(2):
                layout_monstros_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')], ]))

        if dados_monstros[0] == 2:
            layout_monstros_j1.append(sg.Frame('ESPAÇO VAZIO',
                                               [[sg.Text('                               ')], [sg.Text('')],
                                                [sg.Text('')], ]))

        if dados_monstros[0] == 3:
            layout_monstros_j1.append(sg.Frame("",
                                               [[sg.Text('CARTA 3                  ')],
                                                [sg.Text(
                                                    f'Nome: {dados_monstros[9]}')],
                                                [sg.Text(
                                                    f'Atributos: {dados_monstros[12]}')],
                                                [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                 sg.Text(f'Vida: {dados_monstros[11]}')]
                                                ]))
        if jogador_turno == nome_jogador:
            layout_inicial = self.criar_layout_de_opcoes(
                em_batalha, atacou, contador_de_passes, '#284d78')
        else:
            layout_inicial = sg.Text('', size=(15, 1))
        layout_monstros_j1.append(
            sg.Text(f'Monstros de {nome_jogador} no tabuleiro', size=(30, 1)))
        return [layout_inicial, sg.Frame('', [layout_monstros_j1], background_color='#284d78')]

    def criar_layout_batalha_j1(self, dados_monstros, nome_jogador, vida_j1, mana_j1, spellmana_j1):
        layout_batalha_j1 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] == 1:

            if dados_monstros[1] is None:
                for i in range(3):
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
            else:
                layout_batalha_j1.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                for i in range(2):
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))

        if dados_monstros[0] == 2:
            if dados_monstros[1] is None:
                layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))
                if dados_monstros[2] is not None:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[2]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[5]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                        sg.Text(f'Vida: {dados_monstros[4]}')]
                                                       ]))

                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))

                else:
                    for i in range(2):
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
            else:
                layout_batalha_j1.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                if dados_monstros[5] is not None:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[5]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[8]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                        sg.Text(f'Vida: {dados_monstros[7]}')]
                                                       ]))
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                else:
                    for i in range(2):
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))

        if dados_monstros[0] == 3:
            if dados_monstros[1] is None:
                layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))
                if dados_monstros[2] is None:
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[3] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[3]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[6]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[4]}'),
                                                            sg.Text(f'Vida: {dados_monstros[5]}')]
                                                           ]))

                else:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[2]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[5]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                        sg.Text(f'Vida: {dados_monstros[4]}')]
                                                       ]))
                    if dados_monstros[6] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[6]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[9]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                            sg.Text(f'Vida: {dados_monstros[8]}')]
                                                           ]))
            else:
                layout_batalha_j1.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                if dados_monstros[5] is None:
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[6] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[6]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[9]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                            sg.Text(f'Vida: {dados_monstros[8]}')]
                                                           ]))
                else:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[5]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[8]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                        sg.Text(f'Vida: {dados_monstros[7]}')]
                                                       ]))
                    if dados_monstros[9] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[9]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[12]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                            sg.Text(f'Vida: {dados_monstros[11]}')]
                                                           ]))

        layout_batalha_j1.append(
            sg.Text(f'Campo de batalha de {nome_jogador}', size=(30, 1)))

        return [sg.Frame(f'{nome_jogador.upper()}', [
            [sg.Text(f'Vida da Torre: {vida_j1}')],
            [sg.Text(f'Mana: {mana_j1}')],
            [sg.Text(f'Mana de Feitiço: {spellmana_j1}')]
        ], background_color='#284d78'), sg.Frame('', [layout_batalha_j1], background_color='#541616')]

    def criar_layout_monstros_j2(self, dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou,
                                 contador_de_passes):
        layout_monstros_j2 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_monstros_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')], ]))

        if dados_monstros[0] >= 1:
            layout_monstros_j2.append(sg.Frame("",
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       'CARTA 1                  ')]
                                               ]))
        if dados_monstros[0] >= 2:
            layout_monstros_j2.append(sg.Frame("",
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                    sg.Text(f'Vida: {dados_monstros[7]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[8]}')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[5]}')],
                                                   [sg.Text(
                                                       'CARTA 2                  ')]
                                               ]))
        if dados_monstros[0] == 1:
            for i in range(2):
                layout_monstros_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')]]))

        if dados_monstros[0] == 2:
            layout_monstros_j2.append(sg.Frame('ESPAÇO VAZIO',
                                               [[sg.Text('                               ')], [sg.Text('')],
                                                [sg.Text('')]]))

        if dados_monstros[0] == 3:
            layout_monstros_j2.append(sg.Frame("",
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                    sg.Text(f'Vida: {dados_monstros[11]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[12]}')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[9]}')],
                                                   [sg.Text(
                                                       'CARTA 3                  ')]
                                               ]))

        if jogador_turno == nome_jogador:
            layout_inicial = self.criar_layout_de_opcoes(
                em_batalha, atacou, contador_de_passes, '#275245')
        else:
            layout_inicial = sg.Text('', size=(15, 1))
        layout_monstros_j2.append(
            sg.Text(f'Monstros de {nome_jogador} no tabuleiro', size=(30, 1)))
        return [layout_inicial, sg.Frame('', [layout_monstros_j2], background_color='#275245')]

    def criar_layout_batalha_j2(self, dados_monstros, nome_jogador):

        layout_batalha_j2 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] == 1:

            if dados_monstros[1] is None:
                for i in range(3):
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
            else:
                layout_batalha_j2.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                for i in range(2):
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))

        if dados_monstros[0] == 2:
            if dados_monstros[1] is None:
                layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))
                if dados_monstros[2] is not None:
                    layout_batalha_j2.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[2]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[5]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                        sg.Text(f'Vida: {dados_monstros[4]}')]
                                                       ]))

                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))

                else:
                    for i in range(2):
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
            else:
                layout_batalha_j2.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                if dados_monstros[5] is not None:
                    layout_batalha_j2.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[5]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[8]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                        sg.Text(f'Vida: {dados_monstros[7]}')]
                                                       ]))
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                else:
                    for i in range(2):
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))

        if dados_monstros[0] == 3:
            if dados_monstros[1] is None:
                layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))
                if dados_monstros[2] is None:
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[3] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[3]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[6]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[4]}'),
                                                            sg.Text(f'Vida: {dados_monstros[5]}')]
                                                           ]))

                else:
                    layout_batalha_j2.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[2]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[5]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                        sg.Text(f'Vida: {dados_monstros[4]}')]
                                                       ]))
                    if dados_monstros[6] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[6]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[9]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                            sg.Text(f'Vida: {dados_monstros[8]}')]
                                                           ]))
            else:
                layout_batalha_j2.append(sg.Frame("",
                                                  [[sg.Text('CARTA 1                  ')],
                                                   [sg.Text(
                                                       f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text(
                                                       f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')]
                                                   ]))
                if dados_monstros[5] is None:
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[6] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[6]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[9]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                            sg.Text(f'Vida: {dados_monstros[8]}')]
                                                           ]))
                else:
                    layout_batalha_j2.append(sg.Frame("",
                                                      [[sg.Text('CARTA 2                  ')],
                                                       [sg.Text(
                                                           f'Nome: {dados_monstros[5]}')],
                                                       [sg.Text(
                                                           f'Atributos: {dados_monstros[8]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                        sg.Text(f'Vida: {dados_monstros[7]}')]
                                                       ]))
                    if dados_monstros[9] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [[sg.Text('CARTA 3                  ')],
                                                           [sg.Text(
                                                               f'Nome: {dados_monstros[9]}')],
                                                           [sg.Text(
                                                               f'Atributos: {dados_monstros[12]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                            sg.Text(f'Vida: {dados_monstros[11]}')]
                                                           ]))
        layout_batalha_j2.append(
            sg.Text(f'Campo de batalha de {nome_jogador}', size=(30, 1)))

        return sg.Frame('', [layout_batalha_j2], background_color='#541616')

    def criar_layout_de_opcoes(self, em_batalha, atacou, contador_passes, cor):
        passar = 'Passar a vez'
        if not em_batalha:
            string_jogar = 'Jogar monstro'
            string_movimento = 'Iniciar ataque'
            if atacou:
                string_movimento = 'Já atacou na rodada!'
            if contador_passes == 1:
                passar = 'Finalizar rodada'
        else:
            string_jogar = 'Jogar feitiço'
            string_movimento = 'Bloquear'
            if contador_passes == 1:
                passar = 'Realizar batalha'

        linha_movimento = sg.Radio(f'{string_movimento}', "RD1", key='2')
        if atacou and (not em_batalha):
            linha_movimento = sg.Text('Já atacou na rodada!')

        layout_opcoes = [
            [sg.Radio('Desistir', "RD1", key='-1')],
            [sg.Radio(f'{passar}', "RD1", key='0')],
            [sg.Radio(f'{string_jogar}', "RD1", key='1')],
            [linha_movimento],
            [sg.Button("Confirmar", button_color=('white', 'green'))]
        ]
        return sg.Frame('Opções', layout_opcoes, background_color=cor)

    def fechar_janela(self, janela):
        janela.close()

    def pega_posicao_carta_em_lista(self, posicoes_disponiveis, janela_turno):
        layout = [
            [sg.Text('Escolha a POSIÇÃO da carta'),
             sg.InputText(key='posicao')],
            [sg.Button('OK', button_color=('white', 'green')),
             sg.Button('Cancelar', button_color=('white', 'red'))]
        ]

        janela = sg.Window('Pegar posição da Carta', layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                janela.close()
                return None

            if evento == 'OK':
                if all(valores.values()):
                    try:
                        valores['posicao'] = int(valores['posicao'])
                    except ValueError:
                        sg.popup_error('Posição inválida!')
                        janela.close()
                        janela_turno.close()
                        raise Voltar
                    if (int(valores['posicao']) > posicoes_disponiveis) or (int(valores['posicao']) < 1):
                        sg.popup_error('Posição inválida!')
                        janela.close()
                        janela_turno.close()
                        raise Voltar
                    janela.close()

                    return int(valores['posicao'])

                else:
                    sg.popup_error('Escolha a posição ou cancele')

    def tela_tabuleiro_cheio(self, dados_monstro,
                             janela_turno):
        layout = [
            [sg.Text(
                'O Tabuleiro está cheio. Avance para substituir um monstro ou cancele para voltar')],
            [sg.Button('Avançar', button_color=('white', 'green')),
             sg.Button('Cancelar', button_color=('white', 'red'))]
        ]

        janela = sg.Window('Substituir monstro?', layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                janela.close()
                janela_turno.close()
                raise Voltar

            if evento == 'Avançar':
                janela.close()

                layout = [
                    [sg.Text('MONSTRO SELECIONADO:')],
                    [sg.Frame('', [[sg.Text(f'Nome: {dados_monstro["nome"]}')],
                                   [sg.Text(
                                       f'Atributo: {dados_monstro["atributo"]}')],
                                   [sg.Text(f'Ataque: {dados_monstro["ataque"]}'),
                                    sg.Text(f'Vida: {dados_monstro["vida"]}')]
                                   ]
                              )],
                    [sg.Button('Continuar', button_color=('white', 'green'))]

                ]

                janela = sg.Window('Monstro selecionado', layout)

                while True:
                    evento, valores = janela.read()

                    if evento in (sg.WIN_CLOSED, 'Continuar'):
                        janela.close()
                        break

                return janela

    def tela_confirmar_ataque(self, janela_turno):
        layout = [
            [sg.Button('Adicionar mais monstros para a batalha',
                       button_color=('white', 'orange'))],
            [sg.Button('Confirmar ataque ✅', button_color=('white', 'green'))],
            [sg.Button("Cancelar ataque ❌", button_color=('white', 'red'))]
        ]

        window = sg.Window("OPÇÕES DE ATAQUE", layout)

        cancelou = False

        while True:
            event, values = window.read()

            if event in [sg.WIN_CLOSED, "Cancelar ataque ❌"]:
                cancelou = True
                window.close()
                janela_turno.close()
                return ('0', cancelou)
            if event == 'Confirmar ataque ✅':
                window.close()
                return ('1', cancelou)

            if event == 'Adicionar mais monstros para a batalha':
                window.close()
                return ('2', cancelou)

    def tela_escolhe_tabuleiro_feitico(self, janela_turno):
        layout = [
            [sg.Text('Escolha o tabuleiro em que o feitiço será aplicado')],
            [sg.Button('Tabuleiro Aliado', button_color=('white', 'green'))],
            [sg.Button("Tabuleiro Inimigo", button_color=('white', 'red'))],
            [sg.Button("Cancelar ❌", button_color=('white', 'orange'))]
        ]

        window = sg.Window("Escolha de Tabuleiro", layout)

        while True:
            event, values = window.read()

            if event in [sg.WIN_CLOSED, "Cancelar ❌"]:
                window.close()
                janela_turno.close()
                return
            if event == 'Tabuleiro Aliado':
                window.close()
                return ('a')

            if event == 'Tabuleiro Inimigo':
                window.close()
                return ('i')

    def mostra_dados_jogos(self, dados_jogos):

        selecionado = dados_jogos[-1]
        data_jogos = []
        for i in range(0, (len(dados_jogos) - 1), 8):
            data_jogo = dados_jogos[i:i + 8]
            data_jogos.append(data_jogo)

        jogos = []
        for data_jogo in data_jogos:
            jogo = {
                "codigo": data_jogo[0],
                "j1": data_jogo[1],
                "j2": data_jogo[2],
                "b1": data_jogo[3],
                "b2": data_jogo[4],
                "vencedor": data_jogo[5],
                "perdedor": data_jogo[6],
                "empate": data_jogo[7]
            }
            jogos.append(jogo)

        col_layout = [[sg.Text(f"Histórico de {selecionado}",
                               font=("Helvica", 18))]]
        for i, jogo in enumerate(jogos):
            if jogo["empate"]:
                jogo_frame = sg.Frame(f"Jogo {i + 1}", self.criar_layout_jogo(**jogo), key=f"-FRAME-{jogo['codigo']}-",
                                      background_color='#494d4a')
            elif jogo["vencedor"] == selecionado:
                jogo_frame = sg.Frame(f"Jogo {i + 1}", self.criar_layout_jogo(**jogo), key=f"-FRAME-{jogo['codigo']}-",
                                      background_color='#168247')

            else:
                jogo_frame = sg.Frame(f"Jogo {i + 1}", self.criar_layout_jogo(**jogo), key=f"-FRAME-{jogo['codigo']}-",
                                      background_color='#611728')
            col_layout.append([jogo_frame])

        layout = [
            [sg.Column(col_layout, scrollable=True,
                       vertical_scroll_only=True, size=(800, 500))],
            [sg.Button("Fechar", button_color=('white', 'red'))]
        ]

        window = sg.Window("Partidas:", layout, finalize=True)

        while True:
            event, _ = window.read()

            if event in (sg.WIN_CLOSED, "Fechar"):
                break

        window.close()

    def criar_layout_jogo(self, codigo, j1, j2, b1, b2, vencedor, perdedor, empate):
        if not empate:
            return [
                [sg.Text(f"Código do jogo: {codigo}")],
                [sg.Text(f"Jogador 1 (azul): {j1}")],
                [sg.Text(f"Baralho do jogador 1: {b1}")],
                [sg.Text(f"Jogador 2 (verde): {j2}")],
                [sg.Text(f"Baralho do jogador 2: {b2}")],
                [sg.Text(f"Vencedor: {vencedor}")],
                [sg.Text(f"Perdedor: {perdedor}")]
            ]
        else:
            return [
                [sg.Text(f"Código do jogo: {codigo}")],
                [sg.Text(f"Jogador 1 (azul): {j1}")],
                [sg.Text(f"Baralho do jogador 1: {b1}")],
                [sg.Text(f"Jogador 2 (verde): {j2}")],
                [sg.Text(f"Baralho do jogador 2: {b2}")],
                [sg.Text("Jogo empatado!")],
            ]
