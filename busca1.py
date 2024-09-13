#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/busca1.c

val =  []

for i in range(10):
    val.append(int(input('Informe o valor {}:'.format(i))))

proc =  int(input('valor a ser procurado: '))


achou=0
for i in val:
    if i == proc:
        achou+=1
        
print('numero foi achado {}'.format(achou))
