quantidadeVAlores = int(input("Digite a quantidade de números a serem lidos: "))

soma = 0
maiorValor = float('-inf') 
menorValor = float('inf') 

for i in range(quantidadeVAlores):
    numeros = int(input("Digite um número inteiro: "))
    soma += numeros
    if numeros > maiorValor:
        maiorValor = numeros
    if numeros < menorValor:
        menorValor = numeros

media = soma / quantidadeVAlores

print("Média: %.2f" % media)
print("Maior valor: %d" % maiorValor)
print("Menor valor: %d" % menorValor)
