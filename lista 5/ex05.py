def trocavaloresPosicaoListaX():
    listaX = list(range(20))

    for i in range(len(listaX) // 2):
        listaX[i], listaX[-i - 1] = listaX[-i - 1], listaX[i]

    print(listaX)



trocavaloresPosicaoListaX()
