"""
Comentei tudo desse repositorio que tem a ver com essa função.
Basicamente o gerador de relatorios ja vai ser o suficiente pra expressar extratos de contas.
"""

from decorator import log

@log
def extracts(balance: float, /, *, extract: str) -> None:
    print("\n================ Extrato ================")
    print(f'{extract}\nSaldo: R$ {balance:.2f}')
    print("=========================================")
