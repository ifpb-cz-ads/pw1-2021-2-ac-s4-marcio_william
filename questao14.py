quilometragemPercorrida = float(input("Digite a quilometragem percorrida: "))
quantidadeDias = int(input("Digite a quantidade de dias alugadis: "))
preco = (quilometragemPercorrida*0.15) + (quantidadeDias*60)

print(f"O preço a ser pago pelo aluguel é de R${preco}")