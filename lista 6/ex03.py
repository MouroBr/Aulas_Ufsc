numeroCasos = int(input("Digite o núumero de camisetas a sortear: "))

for i in range(numeroCasos):
    quantidadeAlunos, numeroSecreto = map(int, input().split())
    alunos = list(map(int, input().split()))

    ganhador = 1
    diferencaGanhador = abs(numeroSecreto - alunos[0])

    for j in range(1, quantidadeAlunos):
        diferencaAtual = abs(numeroSecreto - alunos[j])

        if alunos[j] == numeroSecreto:
            ganhador = j + 1
            break

        elif diferencaAtual < diferencaGanhador:
            ganhador = j + 1
            diferencaGanhador = diferencaAtual


print(ganhador)
