from aluno import Aluno


class Boletim:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_boletim(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}")
            print(f"Média: {aluno.calcular_media()}")
            print()

    def consultar_notas(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno.consultar_notas()
        return None
