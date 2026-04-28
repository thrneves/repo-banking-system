def extracts(account: dict) -> None:
    print("\n================ Extrato ================")
    print(f'{account["extract"]}\nSaldo: R$ {account["balance"]:.2f}')
    print("=========================================")
