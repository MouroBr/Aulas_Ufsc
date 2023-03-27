from time import sleep
proceed = 'N'

while proceed == 'S':
    wage = float(input('Digite o salário: R$ '))
    discount = (wage * 0.11)
    if discount >= 320:
        print(f'Desconto: R$ 320.00')
        sleep(2)
        
    else:
        print(f'Desconto: R${discount}')
        sleep(2)
    proceed = str(input('Deseja continuar [S] ou [N]: ').upper)
    



print('Tenha um bom dia!!!')
