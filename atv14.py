import random

numero_secreto = random.randint(1, 20)  
print("Tente adivinhar o número que estou pensando — entre 1 e 20!")

palpite = None  
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Errado! Tente um número maior.")
    elif palpite > numero_secreto:
        print("Errado! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")