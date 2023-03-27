wage = float(input())
if wage <= 400.00:
    newWage = wage * 1.15
    readjustment = newWage - wage
    percentage = 15
if 400.01 <= wage <= 800.00:
    newWage = wage * 1.12
    readjustment = newWage - wage
    percentage = 12
if 800.01 <= wage <= 1200.00:
    newWage = wage * 1.10
    readjustment = newWage - wage
    percentage = 10
if 1200.01 <= wage <= 2000.00:
    newWage = wage * 1.07
    readjustment = newWage - wage
    percentage = 7
if  wage> 2000.00:
    newWage = wage * 1.04
    readjustment = newWage - wage
    percentage = 4
print('Novo salario: {:.2f}'.format(newWage))
print('Reajuste ganho: {:.2f}'.format(readjustment))
print('Em percentual: {} %'.format(percentage))