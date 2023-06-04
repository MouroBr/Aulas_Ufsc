from participante import Participante


class AmigoSecreto:
    def __init__(self):
        self.participantes = []

    def adicionar_participante(self, participante):
        self.participantes.append(participante)

    def consultar_presente(self, nome, presente):
        for participante in self.participantes:
            if participante.nome == nome:
                return participante.verifica_presente(presente)
        return "Nome não encontrado"
