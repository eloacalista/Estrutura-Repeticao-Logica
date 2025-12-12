soma = 0

while True:
    n = int(input("Digite um número inteiro (negativo para terminar): "))
    if n < 0:
        break
    soma += n

print("Soma dos números positivos digitados:", soma)