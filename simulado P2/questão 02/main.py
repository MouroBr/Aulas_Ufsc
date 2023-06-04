from amigo_secreto import AmigoSecreto


class Main:
    def __init__(self):
        self.amigo_secreto = AmigoSecreto()

    def executar_programa(self):
        while True:
            x = int(input("Digite o número de participantes: "))
            for _ in range(x):
                nome = input("Digite o nome do participante: ")
                presentes = []
                for _ in range(3):
                    presente = input("Digite uma sugestão de presente: ")
                    presentes.append(presente)
                participante = Participante(nome, presentes)
                self.amigo_secreto.adicionar_participante(participante)

            nome_consulta = input("Digite o nome da consulta: ")
            presente_consulta = input("Digite o presente da consulta: ")
            resultado = self.amigo_secreto.consultar_presente(nome_consulta, presente_consulta)
            print(resultado)

            continuar = input("Deseja fazer outra consulta? (S/N) ")
            if continuar.lower() != "s":
                break


if __name__ == "__main__":
    programa = Main()
    programa.executar_programa()
