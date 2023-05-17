class Mergulhadores:
    def __init__(self, numero_voluntario, voluntarios_retornados):
        self.numero_voluntario = numero_voluntario
        self.voluntarios_retornados = voluntarios_retornados

    def identificador_mortos(self, retornados):
        todos = set(range(1, self.numero_voluntario + 1))
        retornados = set(retornados)
        mortos = todos - retornados

        if mortos:
            return sorted(mortos)
        else:
            return '*'
