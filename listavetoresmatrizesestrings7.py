#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listavetoresmatrizesestrings7.c

var = []
par = []
impar = []

for i in range(10):
    var.append(int(input('escreva o valor {}:'.format(i))))

for i in var:
    if i&1 == 0:
        par.append(i)
    else:
        impar.append(i)

print("numeros pares:")
print(par)
print("Numeros impares")
print(impar)