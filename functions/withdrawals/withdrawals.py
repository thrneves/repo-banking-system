limit = 500
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

def withdrawals(*, account: dict) -> dict:
    global number_of_withdrawals
    
    try:
        value = float(input("Informe o valor do saque: "))
    except ValueError as err:
        print("Saque precisa ser numérico!\nError: ", err)
        return account

    if value <= 0: 
        print("Operação falhou! Valor de saque precisa ser maior que 0.")
        return account

    exceeded_balance = value > account["balance"]
    exceeded_limit = value > limit
    exceeded_withdrawals = number_of_withdrawals >= WITHDRAWAL_LIMIT

    if exceeded_balance:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
        print("Operação falhou! O valor do saque excede o limite.")

    elif exceeded_withdrawals:
        print("Operação falhou! Número máximo de saques excedido.")

    else:
        account["balance"] -= value
        account["extract"] += f"Saque: R$ {value:.2f}\n"
        number_of_withdrawals += 1

    return account
