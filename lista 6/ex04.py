entrada = input("")
plug_X = list(map(int, entrada.split()))
entrada = input("")
plug_Y = list(map(int, entrada.split()))


compativel = True
for i in range(5):
    if plug_X[i] == plug_Y[i]:
        compativel = False
        break


if compativel:
    print(("Y"))
else:
    print("N")