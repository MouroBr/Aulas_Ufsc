from folhaResposta import FolhaResposta

while True:
    num_questoes = int(input('Digite o numero de questôes: '))
    if num_questoes == 0:
        break

    respostas = []

    for _ in range(num_questoes):
        tons_cinza = list(map(int, input('Digite os tons de cinza').split()))
        respostas.append(tons_cinza)

    folha_resposta = FolhaResposta(num_questoes, respostas)

    folha_resposta.processar()