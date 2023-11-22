from errors.voltar import Voltar
from PySimpleGUI import PySimpleGUI as sg


class TelaJogo:
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

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
                opcao_selecionada = next(
                    (key for key, value in values.items() if value), None)
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

    def mostra_dados_da_rodada(self, dados_rodada):
        string_dados_rodada = ""
        string_dados_rodada = string_dados_rodada + \
            "VEZ DO(A) JOGADOR(A): " + \
            dados_rodada["tabuleiro_turno"] + '\n'
        string_dados_rodada = string_dados_rodada + "ATACANTE DA RODADA: " + \
            str(dados_rodada["atacante_rodada"].jogador.nome) + '\n'
        string_dados_rodada = string_dados_rodada + "ATAQUE JÁ REALIZADO: " + \
            str(dados_rodada["ataque_realizado"]) + '\n'
        string_dados_rodada = string_dados_rodada + "Está acontecendo uma batalha?" + \
            str(dados_rodada["em_batalha"]) + '\n'
        string_dados_rodada = string_dados_rodada + "Contador de passes:" + \
            str(dados_rodada["contador_de_passes"]) + '\n'

        sg.Popup('--------- '
                 f'RODADA {dados_rodada["rodada"]} ---------',
                 string_dados_rodada)

    def mostrar_dados_jogador_rodada(self, dados_jogador):
        string_dados_jogador = ""
        string_dados_jogador = string_dados_jogador + \
            "JOGADOR: " + \
            dados_jogador["nome"] + '\n'
        string_dados_jogador = string_dados_jogador + "VIDA DA TORRE: " + \
            str(dados_jogador["vida_torre"]) + '\n'
        string_dados_jogador = string_dados_jogador + "MANA: " + \
            str(dados_jogador["mana"]) + '\n'
        string_dados_jogador = string_dados_jogador + "MANA DE FEITICO: " + \
            str(dados_jogador["spellmana"]) + '\n'

        sg.Popup('--------- '
                 f'Jogador {dados_jogador["nome"]} ---------',
                 string_dados_jogador)
        # print('MONSTROS NO TABULEIRO: ', end='')
        # posicao = 0
        # for monstro in dados_jogador['monstros_tabuleiro']:
        #     posicao += 1
        #     atributos = [atributo.efeito for atributo in monstro.atributos]

        #     if len(atributos[0]) > 0:
        #         atributos_str = ", ".join(atributos[0])
        #         mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
        #     else:
        #         mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: || '

        #     print(mensagem, end=' ')

        # print('\nMONSTROS EM BATALHA: ', end='')
        # posicao = 0
        # # for monstro in dados_jogador['monstros_em_batalha']:
        # # posicao += 1
        # # if (monstro is not None):
        # # print(
        # # f'{monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida}', end=' || ')

        # for monstro in dados_jogador['monstros_em_batalha']:
        #     posicao += 1
        #     if monstro is not None:
        #         atributos = [atributo.efeito for atributo in monstro.atributos]

        #         if atributos[0]:
        #             atributos_str = ", ".join(atributos[0])
        #         else:
        #             atributos_str = "||"

        #         mensagem = f'||POS: {posicao} - {monstro.nome} - ATK: {monstro.ataque} - VIDA: {monstro.vida} - ATR: {atributos_str} || '
        #         print(mensagem, end=' ')

    def mostra_dados_do_turno(self, dados_turno):
        string_dados_turno = ""
        string_dados_turno = string_dados_turno + \
            "VEZ DO JOGADOR: " + \
            dados_turno["jogador_atual"] + '\n'
        string_dados_turno = string_dados_turno + "MANA: " + \
            str(dados_turno["mana"]) + '\n'
        string_dados_turno = string_dados_turno + "MANA DE FEITICO: " + \
            str(dados_turno["spellmana"]) + '\n'

        sg.Popup('--------- TURNO ---------',
                 string_dados_turno)

    def init_opcoes_turno(self, em_batalha: bool, nome_jogador):
        string_jogar = ""
        string_movimento = ""
        if not em_batalha:
            string_jogar = 'JOGAR MONSTRO'
            string_movimento = 'INICIAR ATAQUE'
        else:
            string_jogar = 'JOGAR FEITICO'
            string_movimento = 'REALIZAR BLOQUEIO'
        layout = [
            [sg.Text('-------- OPÇÕES --------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção:', font=("Helvica", 15))],
            [sg.Radio('DESISTIR', "RD1", key='-1')],
            [sg.Radio('PASSAR A VEZ', "RD1", key='0')],
            [sg.Radio(f'{string_jogar}', "RD1", key='1')],
            [sg.Radio(f'{string_movimento}', "RD1", key='2')],
            [sg.Button('Confirmar')]
        ]

        self.__window = sg.Window('Sistemas').Layout(layout)

    def opcoes_turno(self, em_batalha: bool, nome_jogador):
        self.init_opcoes_turno(em_batalha, nome_jogador)
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['-1']:
            opcao = -1
        if values['0']:
            opcao = 0
        self.close()
        return opcao
