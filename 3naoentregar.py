#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/3naoentregar.c


def calcula(p1):
    p = []
    p.append(p1 + (p1 * (10/100)))
    p.append(p1 + (p1 * (15/100)))
    p.append(p1 + (p1 * (20/100)))
    return  p

def mostar(p):
    print("salario 1:{}\nsalario 2:{}\nsalario 3:{}".format(p[0],p[1],p[2]))
    
sal = float(input("digite seu salario"))
salarios = calcula(sal)
mostar(salarios)
