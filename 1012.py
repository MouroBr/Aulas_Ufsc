Pi = 3.14159

a, b, c = [float(x) for x in input().split(' ')]

areaTriangulo = (a * c) / 2
areaCirculo = Pi * c ** 2
areaTrapezio = (a + b) / 2 * c
areaQuadrado = b ** 2
areaRetangulo = a * b

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO  : {areaCirculo:.3f}")
print(f"TRAPEZIO : {areaTrapezio:.3f}")
print(f"QUADRADO : {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")


