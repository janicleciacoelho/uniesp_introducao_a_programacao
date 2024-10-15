# Função para converter um número decimal para binário
def decimal_para_binario(numero):
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario if binario != "" else "0"

# Solicitando ao usuário um número decimal
numero_decimal = int(input("Digite um número decimal: "))

# Convertendo o número para binário
binario = decimal_para_binario(numero_decimal)
print(f"O número {numero_decimal} em binário é: {binario}")
