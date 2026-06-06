import re

from clients.customer_menu import customer_menu
from accounts.account import create_account
from accounts.function_menu import function_menu

menu = "\n\n[c] Cadastrar Cliente\n[n] Nova Conta\n[l] Listar Clientes\n[a] Ações da Conta\n[q] Sair\n\n=> "

clients_list = []
while True:
    user_input = input(menu)

    match user_input.lower():
        case "c":
            clients_list = customer_menu(clients_list)
            continue

        case "n":
            if not clients_list:
                print("Cadastre um cliente!")
                continue

            cpf_input = re.sub(r"\D", "", input("CPF do cliente: "))

            if not cpf_input:
                print("Digite o CPF!")
                continue

            if len(cpf_input) != 11:
                print("CPF inválido! Digite os 11 digitos (000.000.000-00)!")
                continue

            for client in clients_list:
                if client["cpf"] == cpf_input:
                    new_account = create_account(client)
                    print(f"Conta {new_account['number']} criada para {client['name']} (agência {new_account['agency']}).")
                    break
            else:
                print("Cliente não localizado!")
            continue

        case "l":
            if clients_list:
                print(clients_list)
            else:
                print("Cadastre um cliente!")
            continue

        case "a":
            if not clients_list:
                print("Cadastre um cliente!")
                continue

            cpf_input = re.sub(r"\D", "", input("CPF do cliente: "))

            client_found = None
            for client in clients_list:
                if client["cpf"] == cpf_input:
                    client_found = client
                    break

            if not client_found:
                print("Cliente não localizado!")
                continue

            if not client_found["accounts"]:
                print("Este cliente não possui contas. Use a opção [n] para criar uma.")
                continue

            print(f"\nContas de {client_found['name']}:")
            for acc in client_found["accounts"]:
                print(f"  - Conta {acc['number']} | Agência {acc['agency']} | Saldo R$ {acc['balance']:.2f}")

            try:
                account_input = int(input("Número da conta: "))
            except ValueError as err:
                print("Conta precisa ser numérica!\nError: ", err)
                continue

            for account in client_found["accounts"]:
                if account["number"] == account_input:
                    function_menu(account)
                    break
            else:
                print("Conta não localizada para este cliente!")

            continue

        case "q":
            print("Obrigado(a) por utilizar o nosso sistema bancário!")
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
