valorCasa = float(input())
salario = float(input())
numeroDeAnos = int(input())

numeroDeMeses = numeroDeAnos * 12

valorDaPrestação = valorCasa / numeroDeMeses

if valorDaPrestação < salario * 0.3:
    print('Aprovado, valor da prestação R$ {:.2f}'.format(valorDaPrestação))

else:
    print('Não aprovado, parcela maior que 30% do salário')
