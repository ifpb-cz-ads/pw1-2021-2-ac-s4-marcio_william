dia = int(input("Digite o dia: "))
hora = int(input("Digite a hora: "))
minutos = int(input("Digite o minuto: "))
segundos = int(input("Digite o segundo: "))

hora = hora + dia*24
minutos = minutos + hora*60
segundos = segundos + minutos*60

print(f"segundos total: {segundos}")