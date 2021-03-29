def t(valor):
    if valor < 2000.00:
        print('Isento')
    else:
        
        if valor <= 3000:
            resposta = (valor - 2000) * 0.08
        elif valor <= 4500:
            # 2000 / 2 = 1000
            resposta = (valor - 3000) * 0.18 + (1000 * 0.08)
        elif valor > 4500:
            # 3000 / 2 = 1500
            resposta = (valor-4500) * 0.28 +(1500 * 0.18) + (1000 * 0.08)

        print(f'R$ {resposta:.2f}')
        
t(float(input()))

#t(3002.00)
#t(1701.12)
#t(4520.00)

