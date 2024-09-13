imoveis = []


for i in range(3):
    dados = {}
    dados['numcad'] = int(input("numero de cadastro:"))
    dados['valorIPTU'] = float(input("Valor do IPTU:"))
    dados['mesesatrasado'] = int(input("Meses atrasados:"))
    dados['valorMulta'] = 50.00 *  dados['mesesatrasado']
    imoveis.append(dados)
    
for i in imoveis:
    print('cadastro {} valor IPTU {} Meses em atraso {} Multas {}'.format(i['numcad'],i['valorIPTU'],i['mesesatrasado'],i['valorMulta']))
    
print("numeros de imoveis calculados {}".format(len(imoveis)))

    