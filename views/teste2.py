from PySimpleGUI import PySimpleGUI as sg
sg.theme('Dark')

dados_turno = {
    'rodada': 10,
    'j1': 'leo',
    'j2': 'jonathan',
    'atacante': 'leo',
    'atacou': True,
    'turno': 'jonathan',
    'vida_j1': 20,
    'vida_j2': 15,
    'mana_j1': 4,
    'mana_j2': 8,
    'spellmana_j1': 2,
    'spellmana_j2': 3,
    'contador_de_passes': 1,
    'em_batalha': False,
    'dados_monstros': [[2, 'karthus', 10, 5, 'Sobrepujar', 'gragas',8,8,'gordo'],
                       [0], [1,'gragas',8,7,'obeso'], [0]]
}

monstros_j1 = dados_turno['dados_monstros'][0]
monstros_j1_batalha = dados_turno['dados_monstros'][1]
monstros_j2 = dados_turno['dados_monstros'][2]
monstros_j2_batalha = dados_turno['dados_monstros'][3]

def criar_layout_batalha_j2(dados_monstros, nome_jogador, atacante):

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
                                                          [[sg.Text('                               ')], [sg.Text('')],
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
                                                          [[sg.Text('                               ')], [sg.Text('')],
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
                                                          [[sg.Text('                               ')], [sg.Text('')],
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
                                                          [[sg.Text('                               ')], [sg.Text('')],
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
    layout_batalha_j2.append(sg.Text(f'Campo de batalha de {nome_jogador}',size=(30,1) ))

    return sg.Frame('', [layout_batalha_j2], background_color='#541616')

def criar_layout_de_opcoes( em_batalha, atacou, contador_passes, cor):
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
    return sg.Frame('Opções',layout_opcoes, background_color=cor)

def criar_layout_batalha_j1(dados_monstros, nome_jogador, atacante):
    defendendo = (atacante != nome_jogador)
    layout_batalha_j1 = []

    if dados_monstros[0] == 0:
        for i in range(3):
            layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                               [[sg.Text('                               ')], [sg.Text('')],
                                                [sg.Text('')], ]))

    if dados_monstros[0] >= 1 and (not defendendo):

        layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 1                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[1]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[2]}'),
                                                sg.Text(f'Vida: {dados_monstros[3]}')]
                                           ]))
    if dados_monstros[0] >= 2 and (not defendendo):
        layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 2                  ')],
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

    if dados_monstros[0] == 3: #pode ser defesa
        if defendendo:
            if dados_monstros[1] is None:  #[3, 'olaf', 8, 8, 'Sobrepujar', None, None]
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
                                                          [   [sg.Text('CARTA 3                  ')],
                                                              [sg.Text(f'Nome: {dados_monstros[3]}')],
                                                              [sg.Text(f'Atributos: {dados_monstros[6]}')],
                                                              [sg.Text(f'Ataque: {dados_monstros[4]}'),
                                                               sg.Text(f'Vida: {dados_monstros[5]}')]
                                                          ]))

                else:
                    layout_batalha_j1.append(sg.Frame("",
                                                      [   [sg.Text('CARTA 2                  ')],
                                                          [sg.Text(f'Nome: {dados_monstros[2]}')],
                                                          [sg.Text(f'Atributos: {dados_monstros[5]}')],
                                                          [sg.Text(f'Ataque: {dados_monstros[3]}'),
                                                           sg.Text(f'Vida: {dados_monstros[4]}')]
                                                      ]))
                    if dados_monstros[6] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [   [sg.Text('CARTA 3                  ')],
                                                              [sg.Text(f'Nome: {dados_monstros[6]}')],
                                                              [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                                              [sg.Text(f'Ataque: {dados_monstros[7]}'),
                                                               sg.Text(f'Vida: {dados_monstros[8]}')]
                                                          ]))
            else:
                layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 1                  ')],
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
                                                  [[sg.Text('                               ')], [sg.Text('')],
                                                   [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 3                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[6]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[9]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[7]}'), sg.Text(f'Vida: {dados_monstros[8]}')]
                                           ]))
                else:
                    layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 2                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[5]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[6]}'),
                                                sg.Text(f'Vida: {dados_monstros[7]}')]
                                           ]))
                    if dados_monstros[9] is None:
                        layout_batalha_j1.append(sg.Frame('ESPAÇO VAZIO',
                                                          [[sg.Text('                               ')], [sg.Text('')],
                                                           [sg.Text('')], ]))
                    else:
                        layout_batalha_j1.append(sg.Frame("",
                                                          [   [sg.Text('CARTA 3                  ')],
                                                              [sg.Text(f'Nome: {dados_monstros[9]}')],
                                                              [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                                              [sg.Text(f'Ataque: {dados_monstros[10]}'),
                                                               sg.Text(f'Vida: {dados_monstros[11]}')]
                                                          ]))
        else:
            layout_batalha_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 3                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[9]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[10]}'), sg.Text(f'Vida: {dados_monstros[11]}')]
                                           ]))

    layout_batalha_j1.append(sg.Text(f'Campo de batalha de {nome_jogador}',size=(30,1)))

    return [sg.Frame(f'{dados_turno["j1"].upper()}', [
            [sg.Text(f'Vida da Torre: {dados_turno["vida_j1"]}')],
            [sg.Text(f'Mana: {dados_turno["mana_j1"]}')],
            [sg.Text(f'Mana de Feitiço: {dados_turno["spellmana_j1"]}')]
        ], background_color='#284d78'), sg.Frame('', [layout_batalha_j1], background_color='#541616') ]

def criar_layout_monstros_j1(dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou, contador_de_passes):
    layout_monstros_j1 = []

    if dados_monstros[0] == 0:
        for i in range(3):
            layout_monstros_j1.append(sg.Frame('ESPAÇO VAZIO', [[sg.Text('                               ')],[sg.Text('')],[sg.Text('')],]))

    if dados_monstros[0] >= 1:
        layout_monstros_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 1                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[1]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[4]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[2]}'), sg.Text(f'Vida: {dados_monstros[3]}')]
                                           ]))
    if dados_monstros[0] >= 2:
        layout_monstros_j1.append(sg.Frame("",
                                           [   [sg.Text('CARTA 2                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[5]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[8]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[6]}'), sg.Text(f'Vida: {dados_monstros[7]}')]
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
                                           [   [sg.Text('CARTA 3                  ')],
                                               [sg.Text(f'Nome: {dados_monstros[9]}')],
                                               [sg.Text(f'Atributos: {dados_monstros[12]}')],
                                               [sg.Text(f'Ataque: {dados_monstros[10]}'), sg.Text(f'Vida: {dados_monstros[11]}')]
                                           ]))
    if jogador_turno == nome_jogador:
        layout_inicial = criar_layout_de_opcoes(em_batalha, atacou, contador_de_passes, '#284d78' )
    else:
        layout_inicial = sg.Text('',size=(15,1))
    layout_monstros_j1.append(sg.Text(f'Monstros de {nome_jogador} no tabuleiro',size=(30,1)))
    return [layout_inicial, sg.Frame('', [layout_monstros_j1], background_color='#284d78')]

def criar_layout_monstros_j2(dados_monstros, nome_jogador, jogador_turno, em_batalha, atacou, contador_de_passes):
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
        layout_inicial = criar_layout_de_opcoes(em_batalha, atacou, contador_de_passes, '#275245')
    else:
        layout_inicial = sg.Text('',size=(15,1))
    layout_monstros_j2.append(sg.Text(f'Monstros de {nome_jogador} no tabuleiro',size=(30, 1)))
    return [layout_inicial, sg.Frame('', [layout_monstros_j2], background_color='#275245')]



# Mantendo a largura e altura da janela
largura_janela = 1100
altura_janela = 650

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
        criar_layout_monstros_j1(monstros_j1, dados_turno["j1"], dados_turno["turno"], dados_turno["em_batalha"],dados_turno["atacou"], dados_turno["contador_de_passes"])
    ],
    [
        criar_layout_batalha_j1(monstros_j1_batalha, dados_turno["j1"], dados_turno["atacante"])
    ],
    [
        sg.Frame('',[[sg.Text('',size=(105,1))]])
    ],
    [
        sg.Frame(f'{dados_turno["j2"].upper()}', [
            [sg.Text(f'Vida da Torre: {dados_turno["vida_j2"]}')],
            [sg.Text(f'Mana: {dados_turno["mana_j2"]}')],
            [sg.Text(f'Mana de Feitiço: {dados_turno["spellmana_j2"]}')]
        ],background_color= '#275245'), criar_layout_batalha_j2(monstros_j2_batalha, dados_turno["j2"], dados_turno["atacante"])

    ],
    [
        criar_layout_monstros_j2(monstros_j2, dados_turno["j2"],dados_turno["turno"], dados_turno["em_batalha"],dados_turno["atacou"], dados_turno["contador_de_passes"])
    ]
]

window = sg.Window('Teste', layout, size=(largura_janela, altura_janela))

opcao_selecionada = None

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Confirmar":
        opcao_selecionada = next((key for key, value in values.items() if value), None)
        break

print(opcao_selecionada) #será um return

window.close()
