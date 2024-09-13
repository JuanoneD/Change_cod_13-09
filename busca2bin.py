#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/busca2bin.c

vet = []

for i in range(10):
    vet.append(int(input('Escreva o valor {}:'.format(i))))

proc = int(input('informe o valor a ser procurado:'))

first = 0
end = 9
find = False

while first<=end:
    mid = int((first+end)/2)
    if(proc<vet[mid]):
        end = mid+1
    elif(proc>vet[mid]):
        first = mid+1
    else:
        find = True
        break

if(find):
    print('foi encontrado')
else:
    print('não foi enconrado')