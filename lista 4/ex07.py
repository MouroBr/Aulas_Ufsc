alcool = gasolina = diesel = 0

codigo = int(input())

while codigo != 4:

    if codigo in [1, 2, 3]:
        
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        else:
            diesel += 1
    
    codigo = int(input())

print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')