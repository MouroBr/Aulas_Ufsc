class PulaSapo:
    def __init__(self, pulo, alturas_canos):
        self.pulo = pulo
        self.alturas_canos = alturas_canos

    def verifica_vitoria(self):
        for i in range(len(self.alturas_canos) - 1):
            diferenca_altura = abs(self.alturas_canos[i] - self.alturas_canos[i + 1])
            if diferenca_altura > self.pulo:
                return "GAME OVER"
            return "YOU WIN"

