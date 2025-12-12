soma = 0
contador = 0

while True:
    idade = int(input("Digite uma idade (0 para encerrar): "))
    if idade == 0:
        break
    soma += idade
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média das idades digitadas é: {media:.2f}")
else:
    print("Nenhuma idade válida foi informada.")
