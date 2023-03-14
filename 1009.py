funcionario = input()
salarioFixo = float(input())
vendas = float(input())

bonus = float(vendas * 0.15)

salarioFinal = salarioFixo + bonus
print('TOTAL = R$ {:.2f}'.format(salarioFinal))
