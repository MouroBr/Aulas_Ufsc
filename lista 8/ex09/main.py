from numeroPerfeito import NumeroPerfeito

while True:
    quantidade_valores = int(input('Digite o total de valores: '))
    if quantidade_valores == 0:
        break

    for _ in range(quantidade_valores):
        valor_para_teste = int(input('Digite o valor a ser verificado: '))

        resultado = NumeroPerfeito.verificador(valor_para_teste)

        print(resultado)
