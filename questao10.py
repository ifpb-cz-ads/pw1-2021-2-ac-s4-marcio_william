salario = float(input("Digite o valor do salario: "))
aumento = float(input("Digite a porcentagem do aumento: "))

salarioAumentado = salario * (1+ aumento/100)
print(f"O salario aumentado é de: R$ {salarioAumentado}")