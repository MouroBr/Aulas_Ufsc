numero = int(input("Digite um número: "))

divisores = []

for divisor in range(2, numero):
    if numero % divisor == 0:
        divisores.append(divisor)

if len(divisores) == 0:
    print(numero, "é um número primo!")
else:
    print(numero, "não é um número primo.")
    print("Ele é divisível por:", divisores)
