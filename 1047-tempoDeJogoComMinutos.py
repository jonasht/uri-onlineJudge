def t(hora1, minuto1, horaFim, minutoFim): 
    
    EmMinutos = 24 * 60 - (hora1 * 60 + minuto1)
    EmMinutos += horaFim * 60 + minutoFim
    
    horas = EmMinutos / 60
    minutos = EmMinutos % 60

    if horas >= 24 and minutos >= 1:
        horas %= 24
    print(f'O JOGO DUROU {int(horas)} HORA(S) E {int(minutos)} MINUTO(S)')

    
h1, m1, h2, m2 = map(int, input().split())
t(h1, m1, h2, m2)