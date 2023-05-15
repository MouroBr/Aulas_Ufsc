while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    matriz = []
    for i in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Verificar a restrição 2
    problemas_resolvidos = set()
    for j in range(m):
        alguem_resolveu = False
        for i in range(n):
            if matriz[i][j] == 1:
                alguem_resolveu = True
        if not alguem_resolveu:
            break
        problemas_resolvidos.add(j)

    # Verificar a restrição 1
    todos_problemas = set(range(m))
    for i in range(n):
        problemas_pessoa_i = set([j for j in range(m) if matriz[i][j] == 1])
        if len(problemas_pessoa_i) == m:
            break
        todos_problemas -= problemas_pessoa_i

    # Verificar a restrição 3
    todos_resolvidos = False
    for i in range(n):
        if set([j for j in range(m) if matriz[i][j] == 1]) == todos_problemas:
            todos_resolvidos = True
            break

    # Verificar a restrição 4
    todos_resolveram = True
    for i in range(n):
        if sum(matriz[i]) == 0:
            todos_resolveram = False
            break

    # Imprimir o resultado
    count = int(not todos_resolvidos) + int(len(problemas_resolvidos) == m) + int(not todos_problemas) + int(todos_resolveram)
    print(count)
