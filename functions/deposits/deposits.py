def deposits(account: dict | None = None) -> dict:
    value = float(input("Informe o valor do depósito: "))

    if not account:
        account = {"balance": 0, "extract": ""}

    if value > 0:
        account["balance"] += value
        account["extract"] += f"Depósito: R$ {value:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return account
