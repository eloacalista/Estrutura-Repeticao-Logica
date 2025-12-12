pares = 0
impares = 0

for i in range(1, 11):
    num = int(input(f"Digite o {i} número inteiro: "))
    if num % 2 == 0:
        pares += num
    else:
        impares += num

print("Soma dos números pares:", pares)
print("Soma dos números ímpares:", impares)