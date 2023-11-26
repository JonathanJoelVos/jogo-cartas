from errors.voltar import Voltar
from PySimpleGUI import PySimpleGUI as sg


sg.theme('Dark')


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

        largura_janela = 1100
        altura_janela = 650

        monstros_j1 = dados_turno['dados_monstros'][0]
        monstros_j1_batalha = dados_turno['dados_monstros'][1]
        monstros_j2 = dados_turno['dados_monstros'][2]
        monstros_j2_batalha = dados_turno['dados_monstros'][3]

        # Adicionando sg.Frame para cada jogador
        layout = [
            [sg.Frame('', [
                [
                    sg.Text(f'RODADA {dados_turno["rodada"]}', font=('Helvetica', 15), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('ATACANTE DA RODADA:', font=('Helvetica', 12)),
                    sg.Text(f'{dados_turno["atacante"].upper()}', font=('Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('CONTADOR DE PASSES:', font=('Helvetica', 12)),
                    sg.Text(f'{dados_turno["contador_de_passes"]}', font=('Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('EM BATALHA:', font=('Helvetica', 12)),
                    sg.Text(f'{str(dados_turno["em_batalha"]).upper()}', font=('Helvetica', 12), pad=(0, 0)),
                    sg.VerticalSeparator(),
                    sg.Text('VEZ DE', font=('Helvetica', 13)),
                    sg.Text(f'{dados_turno["turno"].upper()}', font=('Helvetica', 12)),
                ],
            ])],
            [
                self.criar_layout_monstros_j1(monstros_j1, dados_turno["j1"], dados_turno["turno"],
                                         dados_turno["em_batalha"], dados_turno["atacou"],
                                         dados_turno["contador_de_passes"])
            ],
            [
                self.criar_layout_batalha_j1(monstros_j1_batalha, dados_turno["j1"], dados_turno["atacante"], dados_turno["vida_j1"], dados_turno["mana_j1"], dados_turno["spellmana_j1"])
            ],
            [
                sg.Frame('', [[sg.Text('', size=(105, 1))]])
            ],
            [
                sg.Frame(f'{dados_turno["j2"].upper()}', [
                    [sg.Text(f'Vida da Torre: {dados_turno["vida_j2"]}')],
                    [sg.Text(f'Mana: {dados_turno["mana_j2"]}')],
                    [sg.Text(f'Mana de Feitiço: {dados_turno["spellmana_j2"]}')]
                ], background_color='#275245'),
                self.criar_layout_batalha_j2(monstros_j2_batalha, dados_turno["j2"], dados_turno["atacante"])

            ],
            [
                self.criar_layout_monstros_j2(monstros_j2, dados_turno["j2"], dados_turno["turno"],
                                         dados_turno["em_batalha"], dados_turno["atacou"],
                                         dados_turno["contador_de_passes"])
            ]
        ]

        window = sg.Window('Tabuleiro', layout, size=(largura_janela, altura_janela))

        opcao_selecionada = None

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                return ('GAME OVER', window)

            elif event == "Confirmar":
                opcao_selecionada = next((key for key, value in values.items() if value), None)
                break

        if opcao_selecionada is not None:
            opcao_selecionada = (int(opcao_selecionada))

        return (opcao_selecionada, window)  # será um return

    def criar_layout_monstros_j1(self, dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou, contador_de_passes):
        layout_monstros_j1 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_monstros_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')], ]))

        if dados_monstros[0] >= 1:
            layout_monstros_j1.append(sg.Frame("",
                                               [[sg.Text('CARTA 1                  ')],
                                                [sg.Text(f'Nome: {dados_monstros[1]}')],
                                                [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                                [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                 sg.Text(f'Vida: {dados_monstros[3]}')]
                                                ]))
        if dados_monstros[0] >= 2:
            layout_monstros_j1.append(sg.Frame("",
                                               [[sg.Text('CARTA 2                  ')],
                                                [sg.Text(f'Nome: {dados_monstros[5]}')],
                                                [sg.Text(f'Atributos: {dados_monstros[8]}')],
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
                                                [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                 sg.Text(f'Vida: {dados_monstros[11]}')]
                                                ]))
        if jogador_turno == nome_jogador:
            layout_inicial = self.criar_layout_de_opcoes(em_batalha, atacou, contador_de_passes, '#284d78')
        else:
            layout_inicial = sg.Text('', size=(15, 1))
        layout_monstros_j1.append(sg.Text(f'Monstros de {nome_jogador} no tabuleiro', size=(30, 1)))
        return [layout_inicial, sg.Frame('', [layout_monstros_j1], background_color='#284d78')]

    def criar_layout_batalha_j1(self, dados_monstros, nome_jogador, atacante, vida_j1, mana_j1, spellmana_j1):
        defendendo = (atacante != nome_jogador)
        layout_batalha_j1 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] >= 1 and (not defendendo):
            layout_batalha_j1.append(sg.Frame("",
                                              [[sg.Text('CARTA 1                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[1]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                sg.Text(f'Vida: {dados_monstros[3]}')]
                                               ]))
        if dados_monstros[0] >= 2 and (not defendendo):
            layout_batalha_j1.append(sg.Frame("",
                                              [[sg.Text('CARTA 2                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[5]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                sg.Text(f'Vida: {dados_monstros[7]}')]
                                               ]))
        if dados_monstros[0] == 1:
            for i in range(2):
                layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] == 2:
            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                              [[sg.Text('                               ')], [sg.Text('')],
                                               [sg.Text('')], ]))

        if dados_monstros[0] == 3:  # pode ser defesa
            if defendendo:
                if dados_monstros[1] is None:  # [3, 'olaf', 8, 8, 'Sobrepujar', None, None]
                    layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[2] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                        if dados_monstros[3] is None:
                            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j1.append(sg.Frame("",
                                                              [[sg.Text('CARTA 3                  ')],
                                                               [sg.Text(f'Nome: {dados_monstros[3]}')],
                                                               [sg.Text(f'Atributos: {dados_monstros[6]}')],
                                                               [sg.Text(f'Ataque: {dados_monstros[4]}'),
                                                                sg.Text(f'Vida: {dados_monstros[5]}')]
                                                               ]))

                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 2                  ')],
                                                           [sg.Text(f'Nome: {dados_monstros[2]}')],
                                                           [sg.Text(f'Atributos: {dados_monstros[5]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                            sg.Text(f'Vida: {dados_monstros[4]}')]
                                                           ]))
                        if dados_monstros[6] is None:
                            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j1.append(sg.Frame("",
                                                              [[sg.Text('CARTA 3                  ')],
                                                               [sg.Text(f'Nome: {dados_monstros[6]}')],
                                                               [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                                               [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                                sg.Text(f'Vida: {dados_monstros[8]}')]
                                                               ]))
                else:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [[sg.Text('CARTA 1                  ')],
                                                       [sg.Text(f'Nome: {dados_monstros[1]}')],
                                                       [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                                       [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                        sg.Text(f'Vida: {dados_monstros[3]}')]
                                                       ]))
                    if dados_monstros[5] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                        if dados_monstros[6] is None:
                            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j1.append(sg.Frame("",
                                                              [[sg.Text('CARTA 3                  ')],
                                                               [sg.Text(f'Nome: {dados_monstros[6]}')],
                                                               [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                                               [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                                sg.Text(f'Vida: {dados_monstros[8]}')]
                                                               ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [[sg.Text('CARTA 2                  ')],
                                                           [sg.Text(f'Nome: {dados_monstros[5]}')],
                                                           [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                                           [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                            sg.Text(f'Vida: {dados_monstros[7]}')]
                                                           ]))
                        if dados_monstros[9] is None:
                            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j1.append(sg.Frame("",
                                                              [[sg.Text('CARTA 3                  ')],
                                                               [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                               [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                               [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                                sg.Text(f'Vida: {dados_monstros[11]}')]
                                                               ]))
            else:
                layout_batalha_j1.append(sg.Frame("",
                                                  [[sg.Text('CARTA 3                  ')],
                                                   [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                   [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                   [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                    sg.Text(f'Vida: {dados_monstros[11]}')]
                                                   ]))

        layout_batalha_j1.append(sg.Text(f'Campo de batalha de {nome_jogador}', size=(30, 1)))

        return [sg.Frame(f'{nome_jogador.upper()}', [
            [sg.Text(f'Vida da Torre: {vida_j1}')],
            [sg.Text(f'Mana: {mana_j1}')],
            [sg.Text(f'Mana de Feitiço: {spellmana_j1}')]
        ], background_color='#284d78'), sg.Frame('', [layout_batalha_j1], background_color='#541616')]

    def criar_layout_monstros_j2(self, dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou, contador_de_passes):
        layout_monstros_j2 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_monstros_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                   [[sg.Text('                               ')], [sg.Text('')],
                                                    [sg.Text('')], ]))

        if dados_monstros[0] >= 1:
            layout_monstros_j2.append(sg.Frame("",  # Removido o título do frame
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                    sg.Text(f'Vida: {dados_monstros[3]}')],
                                                   [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                                   [sg.Text(f'Nome: {dados_monstros[1]}')],
                                                   [sg.Text('CARTA 1                  ')]  # Adicionada uma última linha
                                               ]))
        if dados_monstros[0] >= 2:
            layout_monstros_j2.append(sg.Frame("",  # Removido o título do frame
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                    sg.Text(f'Vida: {dados_monstros[7]}')],
                                                   [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                                   [sg.Text(f'Nome: {dados_monstros[5]}')],
                                                   [sg.Text('CARTA 2                  ')]  # Adicionada uma última linha
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
            layout_monstros_j2.append(sg.Frame("",  # Removido o título do frame
                                               [
                                                   [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                    sg.Text(f'Vida: {dados_monstros[11]}')],
                                                   [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                   [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                   [sg.Text('CARTA 3                  ')]  # Adicionada uma última linha
                                               ]))

        if jogador_turno == nome_jogador:
            layout_inicial = self.criar_layout_de_opcoes(em_batalha, atacou, contador_de_passes, '#275245')
        else:
            layout_inicial = sg.Text('', size=(15, 1))
        layout_monstros_j2.append(sg.Text(f'Monstros de {nome_jogador} no tabuleiro', size=(30, 1)))
        return [layout_inicial, sg.Frame('', [layout_monstros_j2], background_color='#275245')]

    def criar_layout_batalha_j2(self, dados_monstros, nome_jogador, atacante):

        defendendo = (atacante != nome_jogador)

        layout_batalha_j2 = []

        if dados_monstros[0] == 0:
            for i in range(3):
                layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] >= 1 and (not defendendo):
            layout_batalha_j2.append(sg.Frame("",
                                              [
                                                  [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                   sg.Text(f'Vida: {dados_monstros[3]}')],
                                                  [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                                  [sg.Text(f'Nome: {dados_monstros[1]}')],
                                                  [sg.Text('CARTA 1                  ')]
                                              ]))
        if dados_monstros[0] >= 2 and (not defendendo):
            layout_batalha_j2.append(sg.Frame("",
                                              [
                                                  [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                   sg.Text(f'Vida: {dados_monstros[7]}')],
                                                  [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                                  [sg.Text(f'Nome: {dados_monstros[5]}')],
                                                  [sg.Text('CARTA 2                  ')]
                                              ]))
        if dados_monstros[0] == 1:
            for i in range(2):
                layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))

        if dados_monstros[0] == 2:
            layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                              [[sg.Text('                               ')], [sg.Text('')],
                                               [sg.Text('')], ]))

        if dados_monstros[0] == 3:  # pode ser defesa
            if defendendo:
                if dados_monstros[1] is None:  # [3, 'olaf', 8, 8, 'Sobrepujar', None, None]
                    layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                      [[sg.Text('                               ')], [sg.Text('')],
                                                       [sg.Text('')], ]))
                    if dados_monstros[2] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                        if dados_monstros[3] is None:
                            layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j2.append(sg.Frame("",
                                                              [
                                                                  [sg.Text(f'Ataque: {dados_monstros[4]}'),
                                                                   sg.Text(f'Vida: {dados_monstros[5]}')],
                                                                  [sg.Text(f'Atributos: {dados_monstros[6]}')],
                                                                  [sg.Text(f'Nome: {dados_monstros[3]}')],
                                                                  [sg.Text('CARTA 3                  ')]
                                                              ]))

                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [
                                                              [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                               sg.Text(f'Vida: {dados_monstros[4]}')],
                                                              [sg.Text(f'Atributos: {dados_monstros[5]}')],
                                                              [sg.Text(f'Nome: {dados_monstros[2]}')],
                                                              [sg.Text('CARTA 2                  ')]
                                                          ]))
                        if dados_monstros[6] is None:
                            layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j2.append(sg.Frame("",
                                                              [
                                                                  [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                                   sg.Text(f'Vida: {dados_monstros[8]}')],
                                                                  [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                                                  [sg.Text(f'Nome: {dados_monstros[6]}')],
                                                                  [sg.Text('CARTA 3                  ')]
                                                              ]))
                else:
                    layout_batalha_j2.append(sg.Frame("",  # [3, 'olaf', 8, 8, 'Sobrepujar', None, None]
                                                      [
                                                          [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                           sg.Text(f'Vida: {dados_monstros[3]}')],
                                                          [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                                          [sg.Text(f'Nome: {dados_monstros[1]}')],
                                                          [sg.Text('CARTA 1                  ')]
                                                      ]))
                    if dados_monstros[5] is None:
                        layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                        if dados_monstros[6] is None:
                            layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j2.append(sg.Frame("",
                                                              [
                                                                  [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                                   sg.Text(f'Vida: {dados_monstros[8]}')],
                                                                  [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                                                  [sg.Text(f'Nome: {dados_monstros[6]}')],
                                                                  [sg.Text('CARTA 3                  ')]
                                                              ]))
                    else:
                        layout_batalha_j2.append(sg.Frame("",
                                                          [
                                                              [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                               sg.Text(f'Vida: {dados_monstros[7]}')],
                                                              [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                                              [sg.Text(f'Nome: {dados_monstros[5]}')],
                                                              [sg.Text('CARTA 2                  ')]
                                                          ]))
                        if dados_monstros[9] is None:
                            layout_batalha_j2.append(sg.Frame('ESPAÇO VAZIO',
                                                              [[sg.Text('                               ')],
                                                               [sg.Text('')],
                                                               [sg.Text('')], ]))
                        else:
                            layout_batalha_j2.append(sg.Frame("",
                                                              [
                                                                  [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                                   sg.Text(f'Vida: {dados_monstros[11]}')],
                                                                  [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                                  [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                                  [sg.Text('CARTA 3                  ')]
                                                              ]))
            else:
                layout_batalha_j2.append(sg.Frame("",
                                                  [
                                                      [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                       sg.Text(f'Vida: {dados_monstros[11]}')],
                                                      [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                      [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                      [sg.Text('CARTA 3                  ')]
                                                  ]))
        layout_batalha_j2.append(sg.Text(f'Campo de batalha de {nome_jogador}', size=(30, 1)))

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
            linha_movimento = sg.Text(f'Já atacou na rodada!')

        layout_opcoes = [
            [sg.Radio('Desistir', "RD1", key='-1')],
            [sg.Radio(f'{passar}', "RD1", key='0')],
            [sg.Radio(f'{string_jogar}', "RD1", key='1')],
            [linha_movimento],
            [sg.Button('Confirmar')]
        ]
        return sg.Frame('Opções', layout_opcoes, background_color=cor)

    def fechar_janela(self, janela):
        janela.close()

    def pega_posicao_carta_em_lista(self, posicoes_disponiveis, janela_turno):
        layout = [
            [sg.Text('Escolha a POSIÇÃO da carta'), sg.InputText(key='posicao')],
            [sg.Button('OK'), sg.Button('Cancelar')]
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

    def tela_tabuleiro_cheio(self, dados_monstro, janela_turno): #exclui a carta certa, joga tudo pra esquerda e inclui
        layout = [
            [sg.Text('O Tabuleiro está cheio. Avance para substituir um monstro ou cancele para voltar')],
            [sg.Button('Avançar'), sg.Button('Cancelar')]
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
                    [sg.Frame('',[[sg.Text(f'Nome: {dados_monstro["nome"]}')],
                                 [sg.Text(f'Atributo: {dados_monstro["atributo"]}')],
                                 [sg.Text(f'Ataque: {dados_monstro["ataque"]}'),sg.Text(f'Vida: {dados_monstro["vida"]}')]
                                 ]
                             )],
                    [sg.Button('Continuar')]

                ]

                janela = sg.Window('Monstro selecionado',layout)

                while True:
                    evento, valores = janela.read()

                    if evento in (sg.WIN_CLOSED, 'Continuar'):
                        janela.close()
                        break

                return janela

    def tela_confirmar_ataque(self, janela_turno):
        layout = [
            [sg.Button('Adicionar mais monstros para a batalha')],
            [sg.Button('Confirmar ataque ✅')],
            [sg.Button("Cancelar ataque ❌")]
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

    def tela_de_bloqueio(self, janela_turno):
        pass