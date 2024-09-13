# https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_01.c


for i in range(11):
    cod=input('Qual seu codigo')
    horasn = float(input('Horas normais'))
    horase = float(input('Horas extras'))
    print('calculo funcionario {}'.format(i))
    res_bruto = horasn * 12 + horase * 15.50
    res_liquido = res_bruto - (res_bruto * 0.1)
    print('funcionario {} trabalhou horas normais e {} horas extras'.format(cod,horasn,horase))
    print('ira receber {} de salario bruto e {} de salario liquido'.format(res_bruto,res_liquido))

