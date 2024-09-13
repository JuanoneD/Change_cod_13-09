nome = input("escreva seu nome")
preco = float(input("escreva o preco da gasolina"))
pagamento = float(input("informe o valor de pagamento"))

print('{} vai abastecer {} litros de gasolina'.format(nome,pagamento/preco))