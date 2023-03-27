numero = int(input("Digite um número inteiro entre 1 e 10: "))

if numero >= 1 and numero <= 10:
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"- {numero} x {i} = {resultado}")
else:
    print("Número inválido. Por favor, digite um número inteiro entre 1 e 10.")
