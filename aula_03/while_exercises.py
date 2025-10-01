### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# entrada = ''
# while entrada != 'sair':
#     entrada = input("Digite uma palavra: ").lower()

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = int(input("Insira um número de 1 a 10: "))

# while numero not in range(1,11):
#     print("Número fora do intervalo!")
#     numero = int(input("Insira novamente um número de 1 a 10: "))
# print("Numero válido!")
    
### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# last_page = 13
# page = 1

# while True:
#     print(f"Página {page} da API...")
#     page += 1
#     if page > last_page:
#         print("Não há mais páginas na API!")
#         break
        
### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     tentativa += 1
#     print("Tentando reconectar ao serviço...")
    
# print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [1,2,3,4,5,'parar',6,8,9]
indice = 0

while indice <= len(lista):
    if lista[indice] == 'parar':
        print("Processo encerrado...")
        break
    print(f"Processando item {lista[indice]}")
    indice += 1
        