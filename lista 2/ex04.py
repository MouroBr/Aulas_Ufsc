nota01, nota02, nota03 = [float(x) for x in input().split(' ')]

media = (nota01 + nota02 + nota03) / 3

if media <= 5:
    print('Reprovado')

elif media >= 5 and media < 7:
    print('Em recuperação')

else:
    print('Aprovado')