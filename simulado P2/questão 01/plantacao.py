import random


class Plantacao:
    def __int__(self, L, C):
        self.linhas = L
        self.colunas = C
        self.vasos = [[random.randint(0, 10) for _ in range(C)] for _ in range(L)]

    def colher(self, linha, coluna):
        return self.vasos[linha - 1][coluna - 1]

    def exibir_plantacao(self):
        for linha in self.vasos:
            print(' '.join(str(v) for v in linha))
