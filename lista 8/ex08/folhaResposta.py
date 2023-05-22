from metodos import verifica_alternativa_correta
class FolhaResposta:
    def __init__(self, num_questoes, respostas):
        self.num_questoes = num_questoes
        self.respostas = respostas

    def processar(self):
        for i in range(self.num_questoes):
            alternativa_correta = verifica_alternativa_correta(self.respostas[i])
            print(alternativa_correta)
