def extracts(balance: float, /, *, extract: str) -> None:
    print("\n================ Extrato ================")
    print(f'{extract}\nSaldo: R$ {balance:.2f}')
    print("=========================================")
