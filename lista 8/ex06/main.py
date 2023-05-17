from mergulhadores import Mergulhadores

while True:
    try:
        numero_voluntario, voluntarios_retornados = map(int, input('Digite o numero de voluntarios e quantos retornaram: ').split())
        retornados = list(map(int, input('Digite o numero de identificação dos retornados: ').split()))

        mergulhadores = Mergulhadores(numero_voluntario, voluntarios_retornados)

        resultado = mergulhadores.identificador_mortos(retornados)

        print(' '.join(str(voluntario) for voluntario in resultado))

    except EOFError:
        break