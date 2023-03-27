numerosPares = 0
numerosImpares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1

print(f"Quantidade de números pares: {numerosPares}")
print(f"Quantidade de números ímpares: {numerosImpares}")