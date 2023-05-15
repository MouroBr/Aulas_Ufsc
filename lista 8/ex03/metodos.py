import random


class Metodos:
    def cria_Matriz_Random(ordem):
        matriz = []
        for i in range(ordem):
            linha = []
            for j in range(ordem):
                linha.append(random.randint(0, 9))
            matriz.append(linha)
        return matriz

    def cria_Matriz_Manual(ordem):
        matriz = []
        for i in range(ordem):
            linha = []
            for j in range(ordem):
                linha.append(int(input(f"Digite o valor da posição ({i+1},{j+1}): ")))
            matriz.append(linha)
        return matriz

    def calcular_media_abaixo_diagonal(matriz):
        soma = 0
        count = 0
        n = len(matriz)
        for i in range(n):
            for j in range(i):
                soma += matriz[i][j]
                count += 1
        if count == 0:
            return 0
        else:
            return soma / count

    def soma_abaixo_diagonal(matriz):
        soma = 0
        for i in range(len(matriz)):
            for j in range(i):
                soma += matriz[i][j]
        return soma
