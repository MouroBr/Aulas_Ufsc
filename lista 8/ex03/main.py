from metodos import Metodos

ordem = int(input("Digite o tamanho da matriz: "))

print("Digite 1 para criar uma matriz aleatória ou 2 para criar uma matriz manualmente:")
opcao = int(input())

if opcao == 1:
    matriz = Metodos.cria_Matriz_Random(ordem)
elif opcao == 2:
    matriz = Metodos.cria_Matriz_Manual(ordem)
else:
    print("Opção inválida")

if opcao == 1 or opcao == 2:
    print("Matriz gerada:")
    for linha in matriz:
        print(linha)

    media_abaixo_diagonal = Metodos.calcular_media_abaixo_diagonal(matriz)
    print(f"Média abaixo da diagonal principal: {media_abaixo_diagonal}")

    soma_abaixo_diagonal = Metodos.soma_abaixo_diagonal(matriz)
    print(f"Soma dos valores abaixo da diagonal principal: {soma_abaixo_diagonal}")