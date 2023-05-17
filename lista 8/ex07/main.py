from pulaSapo import PulaSapo

pulo, num_canos = map(int, input('Digite o tamodo do pulo e o numero de canos: ').split())

alturas_canos = list(map(int, input('Digite a altura dos canos: ').split()))

jogo = PulaSapo(pulo, alturas_canos)

resultado = jogo.verifica_vitoria(pulo, alturas_canos)

print(resultado)
