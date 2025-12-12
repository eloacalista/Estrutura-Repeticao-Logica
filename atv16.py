cont_positivos = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num > 0:
        cont_positivos += 1

print("Você digitou", cont_positivos, "números positivos.")