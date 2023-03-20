somaNota = 0

for i in range(1, 4):

    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))
    mensalidade = float(input("Digite a mensalidade: "))
    somaNota = somaNota + nota

    if (i == 1):
        melhorNome = nome
        melhorNota = nota
        melhorMensalidade = mensalidade

    else:
        if (nota > melhorNota):
            melhorNome = nome
            melhorNota = nota
            melhorMensalidade = mensalidade

print('Nome do aluno com maior nota:',melhorNome)
print('Mensalidade: ', melhorMensalidade)
print(f'Nova mensalidade, com desconto de 30%: {melhorMensalidade * 0.7}')
print(f'Média da turma: {somaNota / i:.2f}')