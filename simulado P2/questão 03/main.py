from lista_numeros import ListaNumeros


def main():
    n = int(input())

    numeros = list(map(int, input().split()))

    lista = ListaNumeros(numeros)

    print(lista.quantidade_multiplos())


if __name__ == "__main__":
    main()
