from aluno import Aluno
from boletim import Boletim


def main():
    boletim = Boletim()
    continuar = True

    while continuar:
        nome = input("Digite o nome do aluno: ")
        aluno = Aluno(nome)

        nota1 = float(input("Digite a primeira nota: "))
        aluno.adicionar_nota(nota1)
        nota2 = float(input("Digite a segunda nota: "))
        aluno.adicionar_nota(nota2)
        nota3 = float(input("Digite a terceira nota: "))
        aluno.adicionar_nota(nota3)

        boletim.adicionar_aluno(aluno)

        opcao = input("Deseja adicionar outro aluno? (s/n): ")
        if opcao.lower() != "s":
            continuar = False

    print("\nBoletim:")
    boletim.exibir_boletim()

    consultar = input("Deseja consultar as notas de algum aluno? (s/n): ")
    while consultar.lower() == "s":
        nome_consulta = input("Digite o nome do aluno: ")
        notas
