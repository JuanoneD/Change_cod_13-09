matriz2 = []
soma = 0
valor = 1

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(valor)
        valor *=2
        soma += linha[j]
    matriz2.append(linha)
    
for i in matriz2:
    print(i)
    
print('soma das matrizes{}'.format(soma))