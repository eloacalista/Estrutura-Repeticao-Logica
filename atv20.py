
contador = 0
soma = 0
maior = None
menor = None
pares =0
while True:
    num = float(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    contador += 1
    soma += num
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
    if num % 2 == 0:
        pares += 1
if contador > 0:
    media = soma / contador
    print("\n--- RESULTADOS ---")
    print(f"Quantidade de números digitados: {contador}")
    print(f"Média dos números: {media}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade de números pares: {pares}")
else:
    print("Nenhum número válido foi digitado.")
