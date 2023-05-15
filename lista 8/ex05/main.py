from pesquisaEconomica import PesquisaEconomica

numeroParticipante = int(input('Digite o numero de participantes: '))
opinioes = input('Digite a opinião dos participantes: ').split()

pesquisa = PesquisaEconomica(numeroParticipante, opinioes)

resultado = pesquisa.verifica_resultado()

print(resultado)
