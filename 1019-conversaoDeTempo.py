tempoSegundos = int(input())

horas = int(tempoSegundos/60/60)
minutos = int(tempoSegundos/60 - horas*60)
segundos = int(tempoSegundos - (horas*60*60 + minutos*60))

print(f'{horas}:{minutos}:{segundos}')