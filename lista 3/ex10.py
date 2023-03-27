notas = {}

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    notas[nome] = nota

media = sum(notas.values()) / len(notas)
print("Média das notas:", media)


alunoMaiorMedia = max(notas, key=notas.get)
print("Aluno com a maior média:", alunoMaiorMedia)


if notas[alunoMaiorMedia] >= 5.75:
    conceito = "Aprovado"
elif notas[alunoMaiorMedia] >= 2.75:
    conceito = "Em Recuperação"
else:
    conceito = "Reprovado"

print("Conceito do aluno com a maior nota:", conceito)
