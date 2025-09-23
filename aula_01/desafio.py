def calculo_bonus(nome, salario, porcentagem):
    kpi_bonus = 1000 + (salario * porcentagem)
    return (f"Olá {nome}, seu bonus foi de {kpi_bonus} reais")

def main():
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salario: "))
    porcentagem = float(input("Digite sua porcentagem de bonus: "))

    print(calculo_bonus(nome, salario, porcentagem))

main()