class ListaNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def quantidade_multiplos(self):

        contador_2 = 0
        contador_3 = 0
        contador_4 = 0
        contador_5 = 0

        for numero in self.numeros:

            if numero % 2 == 0:
                contador_2 += 1

            if numero % 3 == 0:
                contador_3 += 1

            if numero % 4 == 0:
                contador_4 += 1

            if numero % 5 == 0:
                contador_5 += 1

        return f"{contador_2} múltiplo(s) de 2\n{contador_3} múltiplo(s) de 3\n{contador_4} múltiplo(s) de 4\n{contador_5} múltiplo(s) de 5"
