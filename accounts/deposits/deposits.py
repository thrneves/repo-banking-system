from decorator import log
from datetime import datetime

@log
def deposits(account: dict, /) -> dict:
    try:
        value = float(input("Informe o valor do depósito: "))
    except ValueError as err:
        print("Depósito precisa ser numérico!\nError: ", err)
        return account

    if value > 0:
        account["balance"] += value
        #account["extract"] += f"Depósito: R$ {value:.2f}\n"
        date = datetime.now()
        account["transactions"].append({"type": "deposit", "value": value, "date": date})

    else:
        print("Operação falhou! O valor informado é inválido.")

    return account
