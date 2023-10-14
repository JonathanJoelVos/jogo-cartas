class TelaCarta():
    def tela_opcoes(self):
        print('-------- OPÇÕES DE CARTA --------')
        print('1 - Incluir carta')
        print('2 - Listar cartas')
        print('3 - Excluir carta')
        print('4 - Alterar carta')
        print('0 - Voltar')
        print('----------------------------------')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def mostra_carta(self, dados_carta):
        print('CUSTO MANA:', dados_carta['custo_mana'])
        print('CÓDIGO:', dados_carta['codigo'])

    def mostra_monstro(self, dados_carta):
        self.mostra_carta(dados_carta)
        print('ATAQUE:', dados_carta['ataque'])
        print('VIDA:', dados_carta['vida'])
        print('ATRIBUTOS:', dados_carta['atributos'])
        print("\n")

    def mostra_feitico(self, dados_carta):
        self.mostra_carta(dados_carta)
        print('MODIFICAÇÃO:', dados_carta['modificacao'])
        print('ATRIBUTO MODIFICADO:', dados_carta['atributo_modificado'])
        print('VALOR:', dados_carta['valor'])
        print("\n")

    def seleciona_carta(self):
        codigo = str(input('Código da carta: '))
        return codigo

    def mostra_msg(self, msg):
        print(msg)

    def pega_dados_monstro(self):
        custo_mana = int(input('Custo de mana: '))
        codigo = str(input('Código: '))
        ataque = int(input('Ataque: '))
        vida = int(input('Vida: '))
        atributos = str(input('Atributos: '))
        return {
            'custo_mana': custo_mana,
            'codigo': codigo,
            'ataque': ataque,
            'vida': vida,
            'atributos': atributos,
            'tipo': 'Monstro'
        }

    def pega_dados_feitico(self):
        custo_mana = int(input('Custo de mana: '))
        codigo = str(input('Código: '))
        modificacao = str(input('Modificação: '))
        atributo_modificado = str(input('Atributo modificado: '))
        valor = int(input('Valor: '))
        return {
            'custo_mana': custo_mana,
            'codigo': codigo,
            'modificacao': modificacao,
            'atributo_modificado': atributo_modificado,
            'valor': valor,
            'tipo': 'Feitiço'
        }

    def pega_dados_carta(self):
        print('Escolha o tipo da carta:')
        print('1 - Mostro')
        print('2 - Feitiço')
        tipo = int(input('Tipo: '))
        if (tipo == 1):
            return self.pega_dados_monstro()
        else:
            return self.pega_dados_feitico()
