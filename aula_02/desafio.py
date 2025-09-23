def calculo_bonus(nome, salario, porcentagem):
    kpi_bonus = 1000 + (salario * porcentagem)
    return (f"Olá {nome}, seu bonus foi de {kpi_bonus} reais")

def main():
    try:    
        nome = input("Digite seu nome: ")
        if not nome.isalpha():
            raise ValueError("alpha")
        
        salario = input("Digite seu salario: ")
        porcentagem = input("Digite sua porcentagem de bonus: ")

        try:
            salario = float(salario)
            porcentagem = float(porcentagem)
        except TypeError:
            raise ("numeros")
        
        print(calculo_bonus(nome, salario, porcentagem))

    except ValueError as e:
        if "alpha" in str(e):
            print("Nome aceita apenas letras.")
    except TypeError as e:
        if "numeros" in str(e):
            print("Apenas numeros.")

main()