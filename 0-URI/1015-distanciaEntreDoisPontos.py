from math import sqrt
p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
distancia = sqrt((p2[0] - p1[0])**2 + (p2[1]-p1[1])**2)
print(f'{distancia:.4f}')