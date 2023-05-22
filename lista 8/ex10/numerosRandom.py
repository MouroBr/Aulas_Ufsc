import random


class NumerosRandom:
    def gerador_valores(self, start, end, size):
        return random.sample(range(start, end + 1), size)
