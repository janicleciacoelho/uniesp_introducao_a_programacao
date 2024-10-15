import random

# Solicitando ao usuário o número de lançamentos
lancamentos = int(input("Digite o número de lançamentos do dado: "))

# Loop para realizar os lançamentos
for i in range(lancamentos):
    resultado = random.randint(1, 6)
    print(f"Lançamento {i + 1}: {resultado}")
