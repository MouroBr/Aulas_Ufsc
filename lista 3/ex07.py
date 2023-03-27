numeroPessoas = int(input("Digite o número de pessoas: "))

idades = []
for i in range(numeroPessoas):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    idades.append(idade)

mediaIdades = sum(idades) / numeroPessoas

if mediaIdades <= 25:
    print("A turma é jovem.")
elif mediaIdades <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")
