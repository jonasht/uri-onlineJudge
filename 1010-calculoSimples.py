c1, n1, p1 = input().split()
c2, n2, p2 = input().split()

c1 = int(c1)
c2 = int(c2)
n1 = int(n1)
n2 = int(n2)
p1 = float(p1)
p2 = float(p2)

print(f'VALOR A PAGAR: R$ {((n1 * p1) + (n2 * p2)):.2f}')
