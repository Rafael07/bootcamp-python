def calculo_bonus(nome, salario, porcentagem):
    kpi_bonus = 1000 + (salario * porcentagem)
    return (f"Olá {nome}, seu bonus foi de {kpi_bonus} reais")

def main():
    try:    
        nome = input("Digite seu nome: ")
        if not nome.replace(" ", "").isalpha():
            raise ValueError("NOME_INVALIDO")
        
        salario = input("Digite seu salario: ")
        porcentagem = input("Digite sua porcentagem de bonus: ")

        try:
            salario = float(salario)
            porcentagem = float(porcentagem)
        except ValueError:
            raise ValueError("NUMERO_INVALIDO")
        
        print(calculo_bonus(nome, salario, porcentagem))

    except ValueError as e:
        error_code = str(e)
        if error_code == "NOME_INVALIDO":
            print("Erro: o nome informado deve conter apenas letras.")
        elif error_code == "NUMERO_INVALIDO":
            print("Erro: apenas números são aceitos.")
        else:
            print(f"Erro inesperado: {e}")

main()