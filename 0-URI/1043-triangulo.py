
valores = list(map(float, input().split()))

if (valores[0]+valores[1] > valores[2] and
    valores[1]+valores[2] > valores[0] and
    valores[2]+valores[0] > valores[1]):
    
    print(f'Perimetro = {(sum(valores)):.1f}')
else:
    print(f'Area = {((valores[0]+valores[1]) * valores[2]*.5):.1f}')
