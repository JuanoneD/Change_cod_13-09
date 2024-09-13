# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX1.c

valor_hora = 10.00
valor_extra = 15.00


horasnormais = float(input('Numero de horas normais trabalhadas do ano:'))
horasextras = float(input('Numero de horas extras trabalhadas do ano:'))

horanorm = horasnormais * valor_hora
horaextr = horasextras * valor_extra
total = horanorm + horaextr

poup = total * 0.08

print('valor de hora normais:{}'.format(horanorm))
print('valor de hora extras:{}'.format(horaextr))
print('total dde ganho do ano:{}'.format(total))
print('total dde poupança:{}'.format(poup))