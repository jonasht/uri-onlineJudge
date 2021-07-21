tempo = list(map(int, input().split()))
resultado = (24 - tempo[0]) + tempo[1]
if resultado > 24:
    resultado = resultado - 24
print(f'O JOGO DUROU {resultado} HORA(S)')