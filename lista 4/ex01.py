sexo = input("Digite o sexo (M/F): ").upper()

while sexo != "M" and sexo != "F":
    sexo = input("Sexo inválido. Digite novamente (M/F): ").upper()

print("Sexo digitado: ", sexo)
