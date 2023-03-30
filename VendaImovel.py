valor_imovel = float (input("Digite o valor de venda: "))

corretor = valor_imovel *0.06
taxa_municipal = valor_imovel *0.01
vl_vendedor = valor_imovel - corretor - taxa_municipal
print ("Valor recebido pelo o vendedor: {vl_vendedor}")
