from functions.extracts.extracts import extracts
from functions.deposits.deposits import deposits
from functions.withdrawals.withdrawals import withdrawals

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

account = {}

while True:
    user_input = input(menu)

    match user_input:
        case "d":
            account = deposits(account)

        case "s":
            if not account:
                print("Antes de sacar, você precisa realizar um depósito!")
                continue
            account = withdrawals(account=account)

        case "e":
            if not account:
                print("Você ainda não depositou valores para solicitar extratos!")
                continue
            extracts(account["balance"], extract=account["extract"])
    
        case "q":
            print("Obrigado(a) por utilizar o nosso sistema bancário!")
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
