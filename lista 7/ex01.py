while True:
    n = int(input())
    if n == 0:
        break

    suspeitos = list(map(int, input().split()))
    maisSuspeito = max(suspeitos)
    segundoMaisSuspeito = max(valor for valor in suspeitos if valor < maisSuspeito)
    indiceAssassino = suspeitos.index(segundoMaisSuspeito) + 1

    print(indiceAssassino)
