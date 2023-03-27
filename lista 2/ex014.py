tempoJogo = input().split()
tempoInicial, tempoFinal = tempoJogo

tempoInicial= int(tempoJogo[0])
tempoFinal = int(tempoJogo[1])

if tempoInicial < tempoFinal:
    t = tempoFinal - tempoInicial
else:
    t = (24 - tempoInicial) + tempoFinal
print(f'O JOGO DUROU {t} HORA(S)')