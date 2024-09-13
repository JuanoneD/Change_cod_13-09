#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_02.c

n1 = int(input('digite primeiro numero'))
n2 = int(input('digite segundo numero'))

print('a soma dos numeros é {}'.format(n1+n2))
print('a mult dos numeros é {}'.format(n1*n2))
resp =  (n1+n2)%2 == 0 and 'P' or 'I'
print(resp)


