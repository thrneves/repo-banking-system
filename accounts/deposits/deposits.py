from decorator import log

@log
def deposits(account: dict, /) -> dict:
    try:
        value = float(input("Informe o valor do depósito: "))
    except ValueError as err:
        print("Depósito precisa ser numérico!\nError: ", err)
        return account

    if value > 0:
        account["balance"] += value
        account["extract"] += f"Depósito: R$ {value:.2f}\n"
        account["transactions"].append({"type": "deposit", "value": value})

    else:
        print("Operação falhou! O valor informado é inválido.")

    return account
