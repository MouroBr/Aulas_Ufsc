class Participante:
    def __init__(self, nome, presentes):
        self.nome = nome
        self.presentes = presentes

    def verifica_presente(self, presente):
        if presente in self.presentes:
            return "Seu amigo secreto vai adorar"
        else:
            return "Tente Novamente!"
