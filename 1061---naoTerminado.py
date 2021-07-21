dia1 = int((input().split())[1])
hora1, minuto1, segundo1 = map(int, input().split(':'))

dia2 = int((input().split())[1])
hora2, minuto2, segundo2 = map(int, input().split(':'))


W = dia2 - dia1
X = hora2 - hora1
Y = minuto2 - minuto1
Z = segundo2 - segundo1

    
if X < 0:
    X = X + 24
    W = W - 1

if Y < 0:
    Y = Z + Z
    X = X -1

if Z < 0:
    Z = 60 + Z
    Y = Y - 1

if Z <= 0:
    W = 0

print(f'{W} dia(s)')
print(f'{X} hora(s)')
print(f'{Y} minuto(s)')
print(f'{Z} segundo(s)')
    
