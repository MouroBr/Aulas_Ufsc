def multiplicadorDeListas():

    quantidadeElementos = int(input('Digite o número total de elementos: '))
    listaX = []
    
    for i in range(quantidadeElementos):
        elementosDaListaX = float(input(f'Digite o elemento {i + 1}: '))
        listaX.append(elementosDaListaX)

    multiplicadorK = float(input('Digite o valor a ser multiplicado pela lista: '))
    resultado = [elem * multiplicadorK for elem in listaX]

    print('Lista resultante: ')
    print(resultado)


multiplicadorDeListas()