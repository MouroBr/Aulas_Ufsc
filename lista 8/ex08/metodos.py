def verifica_alternativa_correta(tons_cinza):
    marcador = 0
    for tons_cinza in tons_cinza:
        if tons_cinza <= 127:
            marcador += 1

        if marcador == 1:
            return chr(65 + tons_cinza.index(max(tons_cinza)))

        else:
            return '*'