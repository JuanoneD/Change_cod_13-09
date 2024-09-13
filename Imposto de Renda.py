#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/Imposto%20de%20Renda.c


cod = int(input("Escreva o cod de funcionario"))

while(cod != 0):
    somaINSS = 0
    somaIR = 0
    dep = int(input("Escreva o numero de dependentes"))

    for i in range(10):
        sal = float(input('Digite o salario do mes {}:'.format(i+1)))
        if sal<1399.12:
            valorINSS = sal * 0.08
        elif sal<=2331.88:
            valorINSS = sal * 0.09
        elif sal<=4663.75:
            valorINSS = sal * 0.11
        else:
            valorINSS = 513.01
        somaINSS += valorINSS
        salLiqudo = sal - valorINSS
        
        salIR = salLiqudo - (dep * 189.59)
        if salIR <= 1903.98:
            ValorIR = 0
        elif salIR <= 2826.65:
            valorIR = ((salIR * 0.075) - 142.80)
        elif salIR <= 3751.05:
            valorIR = ((salIR * 0.15) - 354.80)
        elif salIR <= 4664.68:
            valorIR = ((salIR * 0.225) - 636.13)
        else:
            valorIR = ((salIR * 0.275) - 869.36)
        somaIR += ValorIR
        
        salLiqudo -= valorIR
        print("Salario liquido {}".format(salLiqudo))
        print("Valor INSS {}".format(valorINSS))
        print("Valor IR {}".format(valorIR))
          
    print("Funcionario {}".format(cod))
    print("Valor anual do INSS {}".format(somaINSS))
    print("Valor anual do IR {}".format(somaIR))
    cod = int(input("Escreva o cod de funcionario"))
                
        
    