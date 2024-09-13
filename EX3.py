# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX3.c

listestagiarios = []
qtos = 0

for i in range(2):
    estagiarios = {}
    estagiarios['cod'] = input('QUAL O CODIGO DO ESTAGIARIO:')
    estagiarios['nome'] = input('QUAL O NOME DO ESTAGIARIO:')
    estagiarios['ano'] = input('QUAL O ANO DO ESTAGIARIO:')
    salarios = []
    total = 0
    for j in range(12): #ALretara depois
        salarios.append(input('Digite o mes o salario do mes {}:'.format(j)))
        total += float(salarios[j])
    estagiarios['salario'] = salarios
    estagiarios['salarioAnual'] = total
    qtos += 1
    listestagiarios.append(estagiarios)
    print("numere de Estagiario {}".format(qtos))
    
for i in listestagiarios:
    print('cod:{}'.format(i['cod']))
    print('nome:{}'.format(i['nome']))
    print('Ano:{}'.format(i['ano']))
    print('salario anual:{}'.format(i['salarioAnual']))
    print('------------------------------------\n')
    
    
