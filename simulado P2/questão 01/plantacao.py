import random


class Plantacao:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.vasos = [[random.randint(0, 9) for _ in range(colunas)] for _ in range(linhas)]

    def colher(self, linha, coluna):
        linha -= 1
        coluna -= 1
        soma_linha = sum(self.vasos[linha])
        soma_coluna = sum(self.vasos[i][coluna] for i in range(len(self.vasos)))
        intersecao = self.vasos[linha][coluna]
        return soma_linha + soma_coluna - intersecao

    def exibir_plantacao(self):
        for linha in self.vasos:
            print(' '.join(str(v) for v in linha))
