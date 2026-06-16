class AccountIterator:
    def __init__(self, clients_list: list):
        self._accounts = [
            (client["name"], account)
            for client in clients_list
            for account in client["accounts"]
        ]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> dict:
        try:
            owner, account = self._accounts[self._index]
        except IndexError:
            raise StopIteration

        self._index += 1
        return {
            "owner": owner,
            "agency": account["agency"],
            "number": account["number"],
            "balance": account["balance"],
        }
