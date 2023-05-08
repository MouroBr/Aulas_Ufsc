n = int(input())
seq = list(map(int, input().split()))

lista = [0] * n

for i in seq:
    lista[i - 1] = 1

for i in range(n):
    if lista[i] == 0:
        print(i + 1)
        break
