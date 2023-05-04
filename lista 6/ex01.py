def localizaValoresNaTupla():
    valoresTupla = tuple(int(input(f"Digite o {i + 1}º valor: ")) for i in range(5))

    encontaQuantidadeValor9 = valoresTupla.count(9)

    localizaPosicaoValorTres = None
    for i, v in enumerate(valoresTupla):
        if v == 3:
            localizaPosicaoValorTres = i
            break

    localizaValoresPares = [v for v in valoresTupla if v % 2 == 0]

    print(f"O número 9 apareceu {encontaQuantidadeValor9} vezes na tupla.")
    if localizaPosicaoValorTres is not None:
        print(f"O primeiro valor 3 foi digitado na posição {localizaPosicaoValorTres}.")
    else:
        print("Não foi digitado nenhum valor 3 na tupla.")
    print(f"Os números pares digitados foram: {localizaValoresPares}.")


# main
localizaValoresNaTupla()
