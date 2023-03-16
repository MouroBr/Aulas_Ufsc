dias = int(input())

totalAnos = dias // 365
saldo = dias % 365

totalMes = saldo // 30
saldoDias = saldo % 30

print('{} Ano(s)'.format(totalAnos))
print('{} Mês(s)'.format(totalMes))
print('{} Dia(s)'.format(saldoDias))