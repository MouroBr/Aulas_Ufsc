while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if m > n:
        m, n = n, m
    soma = sum(range(m, n+1))
    sequencia = ' '.join(str(i) for i in range(m, n+1))
    print(f'{sequencia} Sum={soma}')