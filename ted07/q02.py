# Solicitando ao usuário um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Loop para gerar a tabuada de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
