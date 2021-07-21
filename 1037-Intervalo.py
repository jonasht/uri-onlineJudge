
entrada = float(input())


if entrada < 0 or entrada > 100:
    mostrar = 'Fora de intervalo'
    
elif entrada <= 25.00:
    mostrar = 'Intervalo [0,25]'

elif entrada <= 50.0:
    mostrar = 'Intervalo (25,50]'
    
elif entrada <=75.0:
    mostrar = 'Intervalo (50,75]'

elif entrada <= 100.0:
    mostrar = 'Intervalo (75,100]'

print(mostrar)
