n = int(input("Digite um número inteiro: "))

if n <= 1:
    print(f"{n} não é primo")
else:
    é_primo = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            é_primo = False
            break
        divisor += 1

    if é_primo:
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")