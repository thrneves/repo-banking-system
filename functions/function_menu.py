from functions.extracts.extracts import extracts
from functions.deposits.deposits import deposits
from functions.withdrawals.withdrawals import withdrawals

def function_menu(account:dict) -> dict:
    menu = """\n\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n\n=> """

    while True:
        user_input = input(menu)

        match user_input.lower():
            case "d":
                account = deposits(account)

            case "s":
                account = withdrawals(account=account)

            case "e":
                extracts(account["balance"], extract=account["extract"])
        
            case "q":
                return account

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
