nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
porcentagem = float(input("Digite sua porcentagem de bonus: "))

kpi_bonus = 1000 + (salario * porcentagem)

print(f"Olá {nome}, seu bonus foi de {kpi_bonus} reais")