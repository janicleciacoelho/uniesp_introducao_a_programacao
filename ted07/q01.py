# Inicializando variáveis
notas = []
nota = 0

# Loop para entrada das notas
while True:
    # Solicitando ao usuário uma nota
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    
    # Condição de parada
    if nota == -1:
        break
    
    # Adicionando a nota à lista
    notas.append(nota)

# Verificando se há notas para calcular a média
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")