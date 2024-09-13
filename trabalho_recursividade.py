#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/trabalho_recursividade.c

def produto(x,y):
    if y ==1:
        return x
    else:
        return x + produto(x,y-1)
    
    

multiplicando = int(input("informe o multiplicando:"))
multiplicador = int(input("Informe o multiplicador"))

print(' o produto é {}'.format(produto(multiplicando,multiplicador)))



