cedulas = float(input())

print('NOTAS:')

print(f'{int(cedulas/100)} nota(s) de R$ 100.00')
cedulas = cedulas % 100

print(f'{int(cedulas/50)} nota(s) de R$ 50.00')
cedulas = cedulas % 50


print(f'{int(cedulas/20)} nota(s) de R$ 20.00')
cedulas = cedulas%20

print(f'{int(cedulas/10)} nota(s) de R$ 10.00')
cedulas = cedulas%10

print(f'{int(cedulas/5)} nota(s) de R$ 5.00')
cedulas = cedulas%5


print(f'{int(cedulas/2)} nota(s) de R$ 2.00')
cedulas = cedulas%2

print('MOEDAS:')
print(f'{int(cedulas/1)} moeda(s) de R$ 1.00')
cedulas = cedulas%1

cedulas = int(str(cedulas)[2:4])

print(f'{int(cedulas/50)} moeda(s) de R$ 0.50')
cedulas = cedulas % 50

print(f'{int(cedulas/25)} moeda(s) de R$ 0.25')
cedulas = cedulas%25

print(f'{int(cedulas/10)} moeda(s) de R$ 0.10')
cedulas = cedulas%10

print(f'{int(cedulas/5)} moeda(s) de R$ 0.05')
cedulas = cedulas%5

print(f'{int(cedulas/1)} moeda(s) de R$ 0.01')

