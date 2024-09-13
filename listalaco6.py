#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listalaco6.c

lanche = int(input('Digite o codigo do  lanche'))
bebida = int(input('Digite o codigo de bebida'))
ped = 0
total = 0

while lanche>0 or bebida > 0:
    ped +=1
    preco = 0
    if lanche == 100:
        preco+=1.20
        print("cachorro quente a 1.20")
    elif lanche == 101:
        preco +=1.30
        print("Bauru a 1.30")
    elif lanche == 102:
        preco += 1.50
        print("Hamburguer a 1.50")
    if bebida == 5:
        preco += 5
        print("coca a 5.0")
    elif bebida == 3:
        preco += 3
        print("agua a 3.0")
    print('valor total: {}'.format(preco))
    total += preco
    
    lanche = int(input('Digite o codigo do  lanche'))
    bebida = int(input('Digite o codigo de bebida'))
    
    
print('pedidos diferentes feitos {}'.format(ped))
print('pedidos totais feitos {}'.format(total))
    