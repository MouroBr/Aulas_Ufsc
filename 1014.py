distanciaTotal = int(input())
consumoTotal = float(input())

consumoMédio = float(distanciaTotal / consumoTotal)
print('{:.3f} km/l'.format(consumoMédio))