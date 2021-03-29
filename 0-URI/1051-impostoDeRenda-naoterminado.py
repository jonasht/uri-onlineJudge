def t(valor):
    if valor < 2000.00:
        print('Insento')
    else:
        if valor < 3000:
            resposta = valor * 0.08
        elif valor < 4500:
            resposta = valor * 0.18
        elif valor > 4500:
            resposta = valor * 0.28
        print(f'R$ {resposta:.2f}')

#valor = float(input())
#t(valor)
print()
t(3002)
t(1701.12)
t(4520.00)
print(28/100)
print((.08*3002.00))