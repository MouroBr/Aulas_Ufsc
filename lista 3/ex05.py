numero = int(input("Digite um número inteiro: "))


for i in range(2, numero):
    if numero % i == 0:
        print(numero, "não é um número primo")
        break
else:
    print(numero, "é um número primo")
