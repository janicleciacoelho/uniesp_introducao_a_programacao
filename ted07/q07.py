# Função para calcular o fatorial de um número
def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Solicitando ao usuário um número
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Calculando o fatorial
if numero < 0:
    print("Não existe fatorial de número negativo.")
else:
    print(f"O fatorial de {numero} é {fatorial(numero)}.")
