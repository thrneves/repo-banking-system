from clients.customer_menu import customer_menu
from accounts.function_menu import function_menu

menu = """\n\n[c] Cadastrar Cliente\n[l] Listar Clientes\n[a] Ações da Conta\n[q] Sair\n\n=> """

clients_list = []
while True:
    user_input = input(menu)

    match user_input.lower():
        case "c":
            clients_list = customer_menu(clients_list)
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
            else:
                try:
                    account_input = int(input("Número da conta: "))
                except ValueError as err:
                    print("Conta precisa ser numérica!\nError: ", err)
                    continue

                for value in clients_list:
                    if value["account"]["number"] == account_input:
                        functions = function_menu(value["account"])
                        value["account"].update(functions)
                        break
                else:
                    print("Conta não localizada!")     

                continue

        case "q":
            print("Obrigado(a) por utilizar o nosso sistema bancário!")
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")