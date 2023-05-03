def maiorMenorValorTupla():
    valores = []
    for i in range(10):
        valor = int(input(f'Informe o {i + 1}º valor: '))
        valores.append(valor)

    tupla = tuple(valores)
    posicaoDoMaior = tupla.index(max(tupla))
    posicaoDoMenor = tupla.index(min(tupla))

    print('Posição do maior elemento: ', posicaoDoMaior)
    print('Posição do menor elemento: ', posicaoDoMenor)


maiorMenorValorTupla()