def calculaVencedorSalto():

    while True:
        nomeDoAtleta = input("Digite o nome do atleta (ou 'O' para sair): ")
        if nomeDoAtleta == "O":
            break

        saltos = []
        for i in range(1, 6):
            salto = float(input(f"Digite a distância do {i}º salto: "))
            saltos.append(salto)

        melhorSalto = max(saltos)
        piorSalto = min(saltos)
        saltos.remove(melhorSalto)
        saltos.remove(piorSalto)
        mediaSaltos = sum(saltos) / len(saltos)

        print(f"Atleta: {nomeDoAtleta}")
        for i, salto in enumerate(saltos):
            print(f"Salto {i + 1}: {salto} m")
        print(f"Melhor salto: {melhorSalto} m")
        print(f"Pior salto: {piorSalto} m")
        print(f"Média dos demais saltos: {mediaSaltos:.1f} m")
        print(f"Resultado final:")
        print(f"{nomeDoAtleta}: {mediaSaltos:.1f} m\n")



calculaVencedorSalto()