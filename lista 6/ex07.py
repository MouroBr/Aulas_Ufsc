numeroCelulasTabuleiro = int(input())

tabuleiro = []

for i in range(numeroCelulasTabuleiro):
    linha = list(map(int, input().split()))
    tabuleiro.append(linha)

for i in range(numeroCelulasTabuleiro):
    numeroMinas = 0

    # verifica própria célula
    numeroMinas += tabuleiro[i][0]

    #verifica à esquerda
    if i > 0:
        numeroMinas += tabuleiro[i - 1][0]

    #verifica à direita
    if i > 0:
        numeroMinas += tabuleiro[i + 1][0]



    print(numeroMinas)