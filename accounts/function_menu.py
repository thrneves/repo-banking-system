#from accounts.extracts.extracts import extracts
from accounts.deposits.deposits import deposits
from accounts.withdrawals.withdrawals import withdrawals
from accounts.reports.reports import report_generator

def function_menu(account:dict) -> dict:
    menu = "\n\n[d] Depositar\n[s] Sacar\n[r] Relatório\n[q] Sair\n\n=> " #[e] Extrato\n

    while True:
        user_input = input(menu)

        match user_input.lower():
            case "d":
                account = deposits(account)

            case "s":
                account = withdrawals(account=account)

            #case "e":
                #extracts(account["balance"], extract=account["extract"])

            case "r":
                filter_choice = input("Filtrar por (d) depósitos, (s) saques ou Enter p/ todas: ").lower()
                transaction_type = {"d": "deposit", "s": "withdrawal"}.get(filter_choice)
                dict_type = {"deposit": "Depósito", "withdrawal": "Saque"}

                print("\n=============== Relatório ===============")
                for transaction in report_generator(account, transaction_type):
                    if transaction["type"] in dict_type:
                        print(f'{dict_type[transaction["type"]]}: R$ {transaction["value"]:.2f}  Em: {transaction["date"]}')
                print("=========================================")

            case "q":
                return

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
