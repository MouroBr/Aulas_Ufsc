from plantacao import Plantacao


def main():
    linhas, colunas, M, N = map(int, input().split())

    plantacao = Plantacao(linhas, colunas)

    plantacao.exibir_plantacao()

    flores_colhidas = plantacao.colher(M, N)

    print("Número de flores colhidas:", flores_colhidas)


if __name__ == '__main__':
    main()
