a, b, c = input().split()

pi = 3.14159
a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) / 2
circulo = pi * c**2
trapezio = c * (a + b) / 2
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
