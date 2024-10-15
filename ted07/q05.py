# Solicitando ao usuário o valor de N
n = int(input("Quantos números da sequência de Fibonacci você deseja ver? "))

# Inicializando os primeiros valores da sequência
fibonacci = [0, 1]

# Gerando a sequência de Fibonacci
for i in range(2, n):
    proximo_numero = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo_numero)

# Exibindo a sequência de Fibonacci até N números
print(f"Os primeiros {n} números da sequência de Fibonacci são:")
print(fibonacci[:n])
