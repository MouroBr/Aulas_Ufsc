while True:

    wage = float(input('Digite o salário: R$ '))
    

    if wage * 0.11 <= 320:
        discount = wage * 0.11
        percentDiscount = 11
    
        
    else:
        discount = 320
        percentDiscount = 320 / wage * 100

    print(f'Desconto previdenciário: R$ {discount:.2f}\nPercentual de desconto: {percentDiscount}%')


    proceed = str(input('Deseja continuar [S] ou [N]: ')).upper()
    if proceed == 'N':
        break

   



