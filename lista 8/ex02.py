import random

ordem = int(input("Digite a ordem da matriz: "))
linha = int(input("Digite a linha da matriz que deseja calcular (0 a {}): ".format(ordem - 1)))
operacao = input("Digite 'S' para soma ou 'M' para média: ")

matriz = [[random.randint(1, 9) for _ in range(ordem)] for _ in range(ordem)]

print("Matriz original:")
for linha_matriz in matriz:
    print(linha_matriz)

linha_verde = matriz[linha][1:ordem - 1]
soma = sum(linha_verde)
media = soma / (ordem - 2)


for j in range(ordem):
    if j == 0 or j == ordem - 1:
        continue
    matriz[linha][j] = media


print("Matriz modificada:")
for linha_matriz in matriz:
    print(linha_matriz)


if operacao == 'S':
    print("Soma da área verde na linha {}: {:.1f}".format(linha, soma))
else:
    print("Média da área verde na linha {}: {:.1f}".format(linha, media))
