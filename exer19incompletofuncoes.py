def ideal_homem(alt):
    return (72.7*alt) - 58

def ideal_mulher(alt):
    return (62.1*alt) - 44.7

sexo = input("Informe seu sexo(M ou F)")
altura = float(input("informe sua altura"))

if sexo == 'M':
    print('peso ideal é ',ideal_homem(altura))
else:
    print('peso ideal é ',ideal_mulher(altura))