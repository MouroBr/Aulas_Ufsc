from random import randint
from time import sleep

secretNumber = randint(0, 10)
print('-=-' * 20)
print('escolhendo numero...')
print('-=-' * 20)

player = int(input('Escolha um numero entre 0 e 10: '))
print('Processando...')
sleep(2)

conter = 0

while secretNumber != player:
    print('Você Errou, tente novamente:')
    sleep(1)
    player = int(input('Escolha um numero entre 0 e 10: '))
    conter += 1

print('Parabéns! Você acertou! O número secreto é: {}\nVocê fez {} tentativas'. format(secretNumber, conter))
