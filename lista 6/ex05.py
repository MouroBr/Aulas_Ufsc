def substituiVetorNegativo():
    tamanhoVetorX = int(input())

    x = []

    for i in range(tamanhoVetorX):
        valor = int(input(f"Entre com o valor do X[{i}] : "))
        if valor <= 0:
            x.append(1)
        else:
            x.append(valor)

    for i in range(tamanhoVetorX):
        print(f"X[{i}] = {x[i]}")


# main
substituiVetorNegativo()
