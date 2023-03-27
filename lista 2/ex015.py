x = input().split()
horaInicial, minutoInicial, horaFinal, minutoFinal = x

horaInicial = int(x[0])
minutoInicial = int(x[1])
horaFinal = int(x[2])
minutoFinal = int(x[3])

if horaInicial < horaFinal:
    h = horaFinal - horaInicial
    if minutoInicial < minutoFinal:
        m = minutoFinal - minutoInicial
    if minutoInicial > minutoFinal:
        h = h - 1
        m = (60 - minutoInicial) + minutoFinal
    if minutoInicial == minutoFinal:
        m = 0
if horaInicial > horaFinal:
    h = (24 - horaInicial) + horaFinal
    if minutoInicial < minutoFinal:
        m = minutoFinal - minutoInicial
    if minutoInicial > minutoFinal:
        h = h - 1
        m = (60 - minutoInicial) + minutoFinal
    if minutoInicial == minutoFinal:
        m = 0
if horaInicial == horaFinal:
    if minutoInicial < minutoFinal:
        m = minutoFinal - minutoInicial
        h = 0
    if minutoInicial > minutoFinal:
        m = (60 - minutoInicial) + minutoFinal
        h = 23
    if minutoInicial == minutoFinal:
        h = 24
        m = 0
    
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')