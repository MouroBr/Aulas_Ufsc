def verificadorNumeroRepitidos():
    numeros = []
    repetidos = False
    
    numeroElementosLista = int(input('Digite o número de elementos na lista: '))

    for i in range(numeroElementosLista):
        numero = int(input('Digite um número inteiro: '))
        if numero in numeros:
            repetidos = True
        numeros.append(numero)

    if repetidos: 
        print('Existem nùmeros repetidos na lista.')
    else:
        print('Não existem numeros repetidos na lista.')



verificadorNumeroRepitidos()