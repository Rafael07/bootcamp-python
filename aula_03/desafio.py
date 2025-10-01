def calculo_bonus(nome, salario, porcentagem):
    kpi_bonus = 1000 + (salario * porcentagem)
    return (f"Olá {nome}, seu bonus foi de {kpi_bonus} reais")
    

def main():

    nome_valido = False
    salario_valido = False
    porcentagem_valida = False
   
    while not nome_valido:
        try:    
            nome = input("Digite seu nome: ")
            if len(nome) == 0:
                 raise ValueError("Erro: o nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                 raise ValueError("Erro: o nome deve conter apenas letras.")
            else:
                 nome_valido = True
        except ValueError as e:
             print(e)
            
    while not salario_valido:
            try:
                salario = float(input("Digite seu salario: "))
                if salario <= 0:
                    print("Erro: o salário não pode ser igual ou inferior a zero.")
                else:
                     salario_valido = True        
            except ValueError as e:
                print(e)
    
    while not porcentagem_valida:
            try:
                porcentagem = float(input("Digite sua porcentagem de bonus: "))
                if porcentagem <= 0:
                     print("Erro: a porcentagem não pode ser igual ou inferior a zero.") 
                else:
                     porcentagem_valida = True       
            except ValueError as e:
                 print(e)
            
    print(calculo_bonus(nome, salario, porcentagem))
            
main()