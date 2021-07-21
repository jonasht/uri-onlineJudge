from math import sqrt

a, b, c = map(float, input().split())

delta = (b**2) - (4*a*c)
if delta < 0 or a == False:
    print("Impossivel calcular")
else:
    print(f'R1 = {(-b+sqrt(delta))/(2*a):.5f}')
    print(f'R2 = {(-b-sqrt(delta))/(2*a):.5f}')