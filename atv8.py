produto = 1

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número inteiro: "))
    produto *= num  

print("Produto de todos os números:", produto)
