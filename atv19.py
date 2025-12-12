a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# Definindo início e fim no sentido correto
inicio = min(a, b)
fim = max(a, b)

print(f"Números ímpares entre {inicio} e {fim}:")

for n in range(inicio, fim + 1):
    if n % 2 != 0:
        print(n)