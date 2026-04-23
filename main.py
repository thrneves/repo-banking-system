menu = """

[d] Depositar
[s] Sacar
[e] extract
[q] Sair

=> """

balance = 0
limit = 500
extract = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:

    user_input = input(menu)

    if user_input == "d":
        value = float(input("Informe o value do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"

        else:
            print("Operação falhou! O value informado é inválido.")

    elif user_input == "s":
        value = float(input("Informe o value do saque: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operação falhou! Você não tem balance suficiente.")

        elif exceeded_limit:
            print("Operação falhou! O value do saque excede o limit.")

        elif exceeded_withdrawals:
            print("Operação falhou! Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            extract += f"Saque: R$ {value:.2f}\n"
            number_of_withdrawals += 1

        else:
            print("Operação falhou! O value informado é inválido.")

    elif user_input == "e":
        print("\n================ extract ================")
        print("Não foram realizadas movimentações." if not extract else extract)
        print(f"\nbalance: R$ {balance:.2f}")
        print("==========================================")

    elif user_input == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
