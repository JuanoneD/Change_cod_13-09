#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/vetordeestruturaulapratica.c

candidatos = []

for i in range(3):
    candato={}
    candato['codigo'] = int(input("Escreva o codigo do candidato"))
    candato['salario'] = float(input("Escreva o salario do candidato"))
    candato['email'] = input("Escreva o email do candidato")
    candidatos.append(candato)
    
for i in candidatos:
    print(i)
    