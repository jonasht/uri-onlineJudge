
def t(salario):
    if salario <= 400:
        novoSalario = salario*1.15
        reajusteGanho = salario*0.15
        emPercentual = 15
        
    elif salario <= 800:
        novoSalario = salario*1.12
        reajusteGanho = salario*0.12
        emPercentual = 12
        
    elif salario <= 1200:

        novoSalario = salario*1.11
        reajusteGanho = salario*0.1
        emPercentual = 10
        
    elif salario <= 2000:
        novoSalario = salario*1.07
        reajusteGanho = salario*0.07
        emPercentual = 7
    elif salario > 2000:
        novoSalario = salario*1.04
        reajusteGanho = salario*0.04
        emPercentual = 4
    print(f'Novo salario: {novoSalario:.2f}')
    print(f'Reajuste ganho: {reajusteGanho:.2f}')
    print(f'Em percentual: {emPercentual} %')

salario = float(input())
t(salario)