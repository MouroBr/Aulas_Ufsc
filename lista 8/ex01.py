pessoas = []
continuar = True

while continuar:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    pessoa = [nome, idade, peso]
    pessoas.append(pessoa)

    resposta = input("Deseja continuar cadastrando? (S/N) ")
    if resposta.upper() == "N":
        continuar = False


print(f"Quantidade de pessoas cadastradas: {len(pessoas)}")


maior_peso = max(pessoas, key=lambda pessoa: pessoa[2])[2]
pessoas_mais_pesadas = [pessoa for pessoa in pessoas if pessoa[2] == maior_peso]
print(f"Pessoa(s) mais pesada(s) (peso: {maior_peso} kg):")
for pessoa in pessoas_mais_pesadas:
    print(f"{pessoa[0]} - idade: {pessoa[1]}")


menor_peso = min(pessoas, key=lambda pessoa: pessoa[2])[2]
pessoas_mais_leves = [pessoa for pessoa in pessoas if pessoa[2] == menor_peso]
print(f"Pessoa(s) mais leve(s) (peso: {menor_peso} kg):")
for pessoa in pessoas_mais_leves:
    print(f"{pessoa[0]} - idade: {pessoa[1]}")


pessoas_acima_20_anos = [pessoa for pessoa in pessoas if pessoa[1] > 20]
print(f"Número de pessoas acima de 20 anos: {len(pessoas_acima_20_anos)}")
for pessoa in pessoas_acima_20_anos:
    print(f"{pessoa[0]} - idade: {pessoa[1]}")
