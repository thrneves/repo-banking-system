from clients.client import MakeClient

def customer_menu(clients_list: list) -> list:
    menu = "\n\n[c] Cadastrar\n[q] Sair\n\n\n=> "

    while True:
        user_input = input(menu)

        match user_input.lower():
            case "c":
                client = MakeClient(clients_list)

                if not client.name():
                    continue
                elif not client.cpf():
                    continue
                elif not client.birth():
                    continue
                elif not client.address():
                    continue

                clients_list.append(client.client)

            case "q":
                return clients_list
            
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")