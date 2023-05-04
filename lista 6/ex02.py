import random

def ordenadorTupla():
    numerosAleatorios = tuple(random.randint(0, 100) for _ in range(5))

    maiorValor = menorValor = numerosAleatorios[0]
    for num in numerosAleatorios:
        if num > maiorValor:
            maiorValor = num
        elif num < menorValor:
            menorValor = num


    print(f"Listagem dos números gerados: {numerosAleatorios}")
    print(f"Maior número: {maiorValor}")
    print(f"Menor número: {menorValor}")



#main
ordenadorTupla()