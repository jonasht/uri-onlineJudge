
# colocando os preços errados 
notebook = '137,00'
mochila = '3738,00'

# mostrandos os preços errados na tela 
print(f'preços antigos: notebook:{notebook} mochila:{mochila} ')


# consertando os preços que o correto
guardar = notebook
notebook = mochila
mochila = guardar 

# mostrando os preços atualizados
print(f'preços atualizados: notebook:{notebook} mochila:{mochila}')
