A, B, C = [float(x) for x in input().split()]

if A == 0 and (B)**2 < (4 * A * C):
    print('Impossivel calcular')

else:
    print(f'R1 = {((-B) + ((B)**2 - 4 * A * C)**0.5) / (2 * A):.5}')
    print(f'R2 = {((-B) - ((B)**2 - 4 * A * C)**0.5) / (2 * A):.5}')