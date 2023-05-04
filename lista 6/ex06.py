valorInicial= int(input("Digite o valor inicial: "))

n = [0] * 10

n[0] = valorInicial

for i in range(1, 10):
    n[i] = 2 * n[i - 1]


for i in range(1, 10):
    print(f"N[{i}] = {n[i]}")