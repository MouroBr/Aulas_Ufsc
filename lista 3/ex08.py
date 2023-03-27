valor01  = int(input("Digite o primeiro número: "))
valor02 = int(input("Digite o segundo número: "))
soma = 0

if valor01 <= valor02:
  for i in range(valor01, valor02+1):
    print(i)
    soma += i
else:
  for i in range(valor02,valor01+1):
    print(i)
    soma += i

print("A soma dos números no intervalo é:", soma)
