entrada = input().split()
Cv, Ce, Cs, Fv, Fe, Fs = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3]), int(entrada[4]), int(entrada[5])

pontosCormengo = 3*Cv + Ce
pontosFlaminthians = 3*Fv + Fe

if pontosCormengo > pontosFlaminthians:
    print('C')
elif pontosFlaminthians > pontosCormengo:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')
