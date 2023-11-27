import PySimpleGUI as sg
from errors.voltar import Voltar


class TelaCarta:
    def __int__(self):
        pass

    def tela_opcoes(self):
        layout = [
            [sg.Text('-------- CARTAS ----------', font=("Helvica", 25), text_color='#f0ad8b')],
            [sg.Text("Escolha uma opção:", justification='center')],
            [sg.Radio("Incluir Carta", "OPCOES", key=1)],
            [sg.Radio("Listar Cartas", "OPCOES", key=2)],
            [sg.Radio("Excluir Carta", "OPCOES", key=3)],
            [sg.Radio("Alterar Carta", "OPCOES", key=4)],
            [sg.Radio("Voltar", "OPCOES", key=0, default=True)],
            [sg.Button("Submeter", size=(20, 1), pad=((10, 10), 3), button_color=('white', 'green'))]
        ]

        window = sg.Window("Opções de Cartas", layout)

        opcao_selecionada = 0

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                opcao_selecionada = next((key for key, value in values.items() if value), None)
                break

        window.close()

        return opcao_selecionada

    def seleciona_carta(self):
        layout = [
            [sg.Text("Selecione o código da carta:"), sg.Input(key='codigo')],
            [sg.Button('Submeter', button_color=('white', 'green'))]
        ]
        window = sg.Window('Selecionar carta', layout)

        while True:
            eventos, valores = window.read()
            if eventos == sg.WIN_CLOSED:
                retornar = None
                break

            if eventos == 'Submeter':
                retornar = valores['codigo']
                break
        window.close()
        return retornar

    def mostra_msg(self, mensagem):
        layout = [[sg.Text(mensagem)],
                  [sg.Button('Continuar', button_color=('white', 'green'))]]
        window = sg.Window(mensagem, layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Continuar":
                break

        window.close()

    def pega_dados_iniciais_carta(self):
        layout = [[sg.Text('Escolha o tipo da carta para ser incluída:', justification='center')],
                  [sg.Radio("Monstro", "OPCOES", key=1)],
                  [sg.Radio("Feitiço", "OPCOES", key=2)],
                  [sg.Button("Submeter", button_color=('white', 'green'), size=(20, 1), pad=((10, 10), 3))]
                  ]

        tipo = 'voltar'
        window = sg.Window("Tipo da carta", layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                tipo = next((key for key, value in values.items() if value), None)
                break

        window.close()

        if tipo == 'voltar':
            return None
        elif tipo == 1:
            return self.pega_dados_monstro()
        else:
            return self.pega_dados_feitico()

    def pega_dados_carta(self):
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Custo de Mana:'), sg.InputText(key='custo_mana')],
            [sg.Text('Código:'), sg.InputText(key='codigo')],
            [sg.Button('OK', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))],
        ]

        janela = sg.Window('Pegar Dados da Carta', layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                janela.close()
                return None

            if evento == 'OK':
                if all(valores.values()):
                    janela.close()
                    return {
                        'nome': valores['nome'],
                        'custo_mana': int(valores['custo_mana']),
                        'codigo': valores['codigo']
                    }
                else:
                    sg.popup_error('Todos os campos devem ser preenchidos.')

    def pega_dados_monstro(self):
        dados_carta = self.pega_dados_carta()
        if dados_carta is None:
            raise Voltar()

        layout = [
            [sg.Text('Ataque:'), sg.InputText(key='ataque')],
            [sg.Text('Vida:'), sg.InputText(key='vida')],
            [sg.Text('Atributos:')],
            [sg.Radio('Voar', 'atributos', key='Voar'),
             sg.Radio('Sobrepujar', 'atributos', key='Sobrepujar', default=True),
             sg.Radio('Nenhum', 'atributos', key='nenhum')],
            [sg.Button('OK', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))],
        ]

        janela = sg.Window('Pegar Dados do Monstro', layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                janela.close()
                return None

            if evento == 'OK':
                if valores['ataque'] and valores['vida'] and (valores['Voar'] or valores['Sobrepujar'] or
                                                              valores['nenhum']):
                    atributos = 'Voar' if valores['Voar'] else 'Sobrepujar' if valores['Sobrepujar'] else ''

                    dados_monstro = {
                        'nome': dados_carta['nome'],
                        'custo_mana': dados_carta['custo_mana'],
                        'codigo': dados_carta['codigo'],
                        'ataque': int(valores['ataque']),
                        'vida': int(valores['vida']),
                        'atributos': [atributos],
                        'tipo': 'Monstro'
                    }
                    janela.close()
                    return dados_monstro
                else:
                    sg.popup_error('Todos os campos necessários devem ser preenchidos.')

    def pega_dados_feitico(self):
        dados_carta = self.pega_dados_carta()
        if dados_carta is None:
            raise Voltar()

        layout = [
            [sg.Text('Modificação:')],
            [sg.Radio('Aumentar', 'modificacao', key='aumentar'),
             sg.Radio('Diminuir', 'modificacao', key='diminuir', default=True)],
            [sg.Text('Atributo modificado:')],
            [sg.Radio('Ataque', 'atributo_modificado', key='ataque'), sg.Radio('Vida', 'atributo_modificado',
                                                                               key='vida')],
            [sg.Text('Valor:'), sg.InputText(key='valor')],
            [sg.Button('OK', button_color=('white', 'green')), sg.Button('Cancelar', button_color=('white', 'red'))],
        ]

        janela = sg.Window('Pegar Dados do Feitiço', layout)

        while True:
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                janela.close()
                return None

            if evento == 'OK':
                if ((valores['aumentar'] or valores['diminuir']) and
                        (valores['ataque'] or valores['vida']) and valores['valor']):
                    modificacao = 'aumentar' if valores['aumentar'] else 'diminuir'

                    atributo_modificado = 'ataque' if valores['ataque'] else 'vida'

                    dados_feitico = {
                        'nome': dados_carta['nome'],
                        'custo_mana': dados_carta['custo_mana'],
                        'codigo': dados_carta['codigo'],
                        'modificacao': modificacao,
                        'atributo_modificado': atributo_modificado,
                        'valor': int(valores['valor']),
                        'tipo': 'Feitiço'
                    }
                    janela.close()
                    return dados_feitico
                else:
                    sg.popup_error('Todos os campos necessários devem ser preenchidos.')

    def mostra_carta(self, dados_cartas):

        data_cartas = []
        for i in range(0, len(dados_cartas), 7):
            data_carta = dados_cartas[i:i + 7]
            data_cartas.append(data_carta)

        cartas = []
        for data_carta in data_cartas:
            carta = {
                "tipo": data_carta[0],
                "nome": data_carta[1],
                "codigo": data_carta[2],
                "mana": data_carta[3],
                "at1": data_carta[4],
                "at2": data_carta[5],
                "at3": data_carta[6],
            }
            cartas.append(carta)

        col_layout = []
        for i, carta in enumerate(cartas):
            if carta["tipo"] == 'Monstro':
                carta_frame = sg.Frame(f"Carta {i + 1}", self.criar_layout_carta(**carta),
                                       key=f"-FRAME-{carta['nome']}-", background_color='#d6996d')
            else:
                carta_frame = sg.Frame(f"Carta {i + 1}", self.criar_layout_carta(**carta),
                                       key=f"-FRAME-{carta['nome']}-", background_color='#4e47d1')

            col_layout.append([carta_frame])

        layout = [
            [sg.Column(col_layout, scrollable=True, vertical_scroll_only=True, size=(300, 800))],
            [sg.Button("Fechar", button_color=('white', 'red'))]
        ]

        window = sg.Window("Cartas:", layout, finalize=True)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, "Fechar"):
                break

        window.close()

    def criar_layout_carta(self, nome, codigo, mana, at1, at2, at3, tipo):
        if tipo == 'Monstro':
            return [
                [sg.Text(f"Tipo: {tipo} 👿")],
                [sg.Text(f"Nome: {nome}")],
                [sg.Text(f"Código: {codigo}")],
                [sg.Text(f"Mana: {mana}")],
                [sg.Text(f"Ataque: {at1}")],
                [sg.Text(f"Vida: {at2}")],
                [sg.Text(f"Atributos: {at3}")]
                ]
        else:
            return [
                [sg.Text(f"Tipo: {tipo} 🧪")],
                [sg.Text(f"Nome: {nome}")],
                [sg.Text(f"Código: {codigo}")],
                [sg.Text(f"Mana: {mana}")],
                [sg.Text(f"Modificação: {at1}")],
                [sg.Text(f"Atributo modificado: {at2}")],
                [sg.Text(f"Valor: {at3}")]
            ]
