entrada = list(map(int, input().split()))
total = 0

if entrada[1] == 1:
    total += 4.00 * entrada[1]
        
if entrada[0] == 2:
    total += 4.50 * entrada[1]
    
if entrada[0] == 3:
    total += 5.00 * entrada[1]
    
if entrada[0] == 4:
    total += 2.00 * entrada[1]
if entrada[0] == 5: 
    total += 1.50 * entrada[1]
    
print(f'Total: R$ {total:.2f}')
