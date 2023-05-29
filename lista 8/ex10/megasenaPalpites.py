from numerosRandom import NumerosRandom


class MegasenaPalpites:
    def __init__(self, quantidade_jogos):
        self.quantidade_jogos = quantidade_jogos
        self.palpites = []
        self.__gerar_palpites()

    def __gerar_palpites(self):
        numeros_random = NumerosRandom()
        for _ in range(self.quantidade_jogos):
            numeros = numeros_random.gerador_valores(1, 60, 6)
            self.palpites.append(numeros)

    def mostrar_palpites(self):
        for i, numeros in enumerate(self.palpites):
            print(f"Jogo {i + 1}: {numeros}")
