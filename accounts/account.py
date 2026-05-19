account_number = 1

def create_account(client: dict) -> dict:
    global account_number

    new_account = {
        "agency": "0001",
        "number": account_number,
        "balance": 0,
        "extract": "",
        "withdrawals_count": 0,
        "limit": 1500,
    }

    client["accounts"].append(new_account)
    account_number += 1
    return new_account
