salario = float(input())

if salario <= 2000.00:
    print('Isento')
    
elif 2000.00 < salario <= 3000.00:
    salariotaxado = salario - 2000.00
    taxaImposto = float(salariotaxado * 0.08)
    print(f'R$ {taxaImposto:.2f}')

elif 3000.00 < salario <= 4500.00:
    taxa01 =float(1000 * 0.08)
    taxa02 = float((salario - 3000.00) * 0.18)
    taxaImposto = taxa01 + taxa02
    print(f'R$ {taxaImposto:.2f}')

else:
    taxa01 = 1000 * 0.08
    taxa02 = 1500.00 * 0.18
    taxa03 = (salario -4500.00) * 0.28
    taxaImposto = taxa01 + taxa02 + taxa03
    print(f'R$ {taxaImposto:.2f}')
