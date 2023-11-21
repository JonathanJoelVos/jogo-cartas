import PySimpleGUI as sg


class TelaCarta:
    def __int__(self):
        self.__window 
    def tela_opcoes(self):
        layout = [
            [sg.Text("Escolha uma opção:", justification='center')],
            [sg.Radio("Incluir Carta", "OPCOES", key=1)],
            [sg.Radio("Listar Cartas", "OPCOES", key=2)],
            [sg.Radio("Excluir Carta", "OPCOES", key=3)],
            [sg.Radio("Alterar Carta", "OPCOES", key=4)],
            [sg.Radio("Voltar", "OPCOES", key=0, default=True)],
            [sg.Button("Submeter", size=(20, 1), pad=((10, 10), 3))]
        ]

        # Centralizando o conteúdo usando sg.Column
        column_layout = [
            [sg.Column(layout, element_justification='center')]
        ]

        window = sg.Window("Opções de Cartas", column_layout, resizable=True, finalize=True)
        window.maximize()

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
            [sg.Button('Submeter')]
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
                  [sg.Button('Voltar')]]
        window = sg.Window(mensagem, layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "Voltar":
                break

        window.close()

    def pega_dados_iniciais_carta(self):
        layout = [[sg.Text('Escolha o tipo da carta para ser incluída:', justification='center')],
                  [sg.Radio("Monstro", "OPCOES", key=1)],
                  [sg.Radio("Feitiço", "OPCOES", key=2)],
                  [sg.Button("Submeter", size=(20, 1), pad=((10, 10), 3))]
                  ]

        window = sg.Window("Tipo da carta", layout)
        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Submeter":
                tipo = next((key for key, value in values.items() if value), None)
                break

        window.close()

        if tipo == 1:
            return self.pega_dados_monstro()
        else:
            return self.pega_dados_feitico()

    def pega_dados_carta(self):
        # Defina o layout da janela
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Custo de Mana:'), sg.InputText(key='custo_mana')],
            [sg.Text('Código:'), sg.InputText(key='codigo')],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]

        # Crie a janela
        janela = sg.Window('Pegar Dados da Carta', layout)

        while True:
            # Leia os eventos e valores da janela
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                # Feche a janela se o usuário fechar ou clicar em Cancelar
                janela.close()
                return None

            if evento == 'OK':
                # Verifique se todos os campos foram preenchidos
                if all(valores.values()):
                    # Se todos os campos estão preenchidos, retorne os dados
                    janela.close()
                    return {
                        'nome': valores['nome'],
                        'custo_mana': int(valores['custo_mana']),
                        'codigo': valores['codigo']
                    }
                else:
                    # Se algum campo estiver vazio, exiba uma mensagem de erro
                    sg.popup_error('Todos os campos devem ser preenchidos.')

    def pega_dados_monstro(self):
        # Obtenha os dados da carta usando a função anterior
        dados_carta = self.pega_dados_carta()

        # Adicione campos específicos para monstros
        layout = [
            [sg.Text('Ataque:'), sg.InputText(key='ataque')],
            [sg.Text('Vida:'), sg.InputText(key='vida')],
            [sg.Text('Atributos:')],
            [sg.Radio('Voar', 'atributos', key='voar'), sg.Radio('Sobrepujar', 'atributos', key='sobrepujar', default=True), sg.Radio('Nenhum', 'atributos', key='nenhum')],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]

        # Crie a janela
        janela = sg.Window('Pegar Dados do Monstro', layout)

        while True:
            # Leia os eventos e valores da janela
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                # Feche a janela se o usuário fechar ou clicar em Cancelar
                janela.close()
                return None

            if evento == 'OK':
                # Verifique se todos os campos necessários foram preenchidos
                if valores['ataque'] and valores['vida'] and (valores['voar'] or valores['sobrepujar'] or valores['nenhum']):
                    # Determine o valor de 'atributos' com base nos botões de rádio
                    atributos = 'voar' if valores['voar'] else 'sobrepujar' if valores['sobrepujar'] else ''

                    # Adicione os campos específicos para monstros aos dados da carta
                    dados_monstro = {
                        'nome': dados_carta['nome'],
                        'custo_mana': dados_carta['custo_mana'],
                        'codigo': dados_carta['codigo'],
                        'ataque': int(valores['ataque']),
                        'vida': int(valores['vida']),
                        'atributos': atributos,
                        'tipo': 'Monstro'
                    }
                    janela.close()
                    return dados_monstro
                else:
                    # Se algum campo estiver vazio, exiba uma mensagem de erro
                    sg.popup_error('Todos os campos necessários devem ser preenchidos.')


    def pega_dados_feitico(self):
        # Obtenha os dados da carta usando a função anterior
        dados_carta = self.pega_dados_carta()

        # Adicione campos específicos para feitiços
        layout = [
            [sg.Text('Modificação:')],
            [sg.Radio('Aumentar', 'modificacao', key='aumentar'), sg.Radio('Diminuir', 'modificacao', key='diminuir', default=True)],
            [sg.Text('Atributo modificado:')],
            [sg.Radio('Ataque', 'atributo_modificado', key='ataque'), sg.Radio('Vida', 'atributo_modificado', key='vida')],
            [sg.Text('Valor:'), sg.InputText(key='valor')],
            [sg.Button('OK'), sg.Button('Cancelar')],
        ]

        # Crie a janela
        janela = sg.Window('Pegar Dados do Feitiço', layout)

        while True:
            # Leia os eventos e valores da janela
            evento, valores = janela.read()

            if evento in (sg.WIN_CLOSED, 'Cancelar'):
                # Feche a janela se o usuário fechar ou clicar em Cancelar
                janela.close()
                return None

            if evento == 'OK':
                # Verifique se todos os campos foram preenchidos
                if (valores['aumentar'] or valores['diminuir']) and (valores['ataque'] or valores['vida']) and valores['valor']:
                    # Determine o valor de 'modificacao' com base nos botões de rádio
                    modificacao = 'aumentar' if valores['aumentar'] else 'diminuir'

                    # Determine o valor de 'atributo_modificado' com base nos botões de rádio
                    atributo_modificado = 'ataque' if valores['ataque'] else 'vida'

                    # Adicione os campos específicos para feitiços aos dados da carta
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
                    # Se algum campo estiver vazio, exiba uma mensagem de erro
                    sg.popup_error('Todos os campos necessários devem ser preenchidos.')

    def mostra_carta(self, dados_layout):
        if dados_layout[-1] == 'monstro':
            layout = [
                [sg.Table(values=dados_layout, headings=['Nome', 'Codigo',
                          'Custo', 'Ataque', 'Vida', 'Atributos', 'Tipo'],
                          auto_size_columns=True)],
                [sg.Button('Ok')]
            ]
        else:
            layout = [
                [sg.Table(values=dados_layout, headings=['Nome', 'Codigo',
                                                         'Custo', 'Modificaçao', 'Atributo Modificado', 'Quantidade', 'Tipo'],
                          auto_size_columns=True)],
                [sg.Button('Ok')]
            ]

        self.__window = sg.Window('Jogadores').Layout(layout)
        button, values = self.open()
        self.close()