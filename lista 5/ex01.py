def sistemasNotasAlunos():
    numeroAlunos = int(input("Digite o número de alunos: "))
    alunos = []

    for i in range(numeroAlunos):
        nome = input(f'Digite o nome do aluno {i + 1}: ')
        notas = []
        for j in range(3):
            nota = float(input(f'Digite a nota {j + 1} do aluno {i + 1}: '))
            notas.append(nota)
        alunos.append((nome, notas))
    
    for i, aluno in enumerate(alunos):
        nome = aluno[0]
        notas = aluno[1]
        media = sum(notas)/3
        maiorNota = max(notas)
        menorNota = min(notas)
        diferenca = maiorNota - menorNota
        print(f"Aluno {i+1}: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Maior nota: {maiorNota}")
        print(f"Menor nota: {menorNota}")
        print(f"Diferença entre a maior e a menor nota: {diferenca:.2f}")



sistemasNotasAlunos()