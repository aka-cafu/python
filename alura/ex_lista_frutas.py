frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Melao']

fruta_pedida = input('Qual a fruta deseja consultar? ')
fruta_pedida = fruta_pedida.strip()



if (fruta_pedida in frutas):
    fileira = frutas.index(fruta_pedida)
    print('Sim, temos a fruta. Ela esta na fileira {}.'.format(fileira))
else:
    print('Nao temos a fruta.')