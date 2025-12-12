while True:
    print("=== MENU ===")
    print("(1) Somar dois números")
    print("(2) Subtrair dois números")
    print("(3) Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}\n")

    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}\n")

    elif opcao == "3":
        print("Saindo... Até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.\n")