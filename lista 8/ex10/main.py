from megasenaPalpites import MegasenaPalpites


quantidade_jogos = int(input('Digite a quantidade de jogos: '))
if quantidade_jogos == 0:
    print("Nenhum jogo será sorteado. O programa será encerrado.")


megasena = MegasenaPalpites(quantidade_jogos)

megasena.mostrar_palpites()