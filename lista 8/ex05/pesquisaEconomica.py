class PesquisaEconomica:
    def __init__(self, numeroParticipantes, opinioes):
        self.numeroParticipantes = numeroParticipantes
        self.opinioes = opinioes

    def verifica_resultado(self):
        satisfatorio = self.opinioes.count('0')
        insatisfatorio  = self.opinioes.count('1')

        if satisfatorio > insatisfatorio:
            return 'Y'
        else:
            return 'N'
