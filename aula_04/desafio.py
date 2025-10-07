def calcular_bonus(dicionario: dict) -> str:
    kpi_bonus: float = 1000 + (dicionario['salario'] * dicionario['porcentagem'])
    return f"Olá {dicionario['nome']}, seu bonus foi de {kpi_bonus:.2f} reais"
    
def validar_nome() -> str:
    nome_valido: bool = False
    while not nome_valido:
        try:    
            nome: str = input("Digite seu nome: ")
            if len(nome) == 0:
                raise ValueError("Erro: o nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("Erro: o nome deve conter apenas letras.")
            else:
                nome_valido = True
        except ValueError as e:
            print(e)
    return nome

def validar_salario() -> str:
    salario_valido: bool = False
    while not salario_valido:
        try:
            salario: float = float(input("Digite seu salario: "))
            if salario <= 0:
                print("Erro: o salário não pode ser igual ou inferior a zero.")
            else:
                salario_valido = True        
        except ValueError as e:
            print(e)
    return salario

def validar_porcentagem() -> float:
    porcentagem_valida: bool = False
    while not porcentagem_valida:
        try:
            porcentagem: float = float(input("Digite sua porcentagem de bonus: "))
            if porcentagem <= 0:
                print("Erro: a porcentagem não pode ser igual ou inferior a zero.") 
            else:
                porcentagem_valida = True       
        except ValueError as e:
            print(e)
    return porcentagem     

def main():
    dados = {
        'nome': validar_nome(),
        'salario': validar_salario(),
        'porcentagem': validar_porcentagem()
    }
    print(calcular_bonus(dados))

if __name__ == "__main__":            
    main()