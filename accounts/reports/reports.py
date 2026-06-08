def report_generator(account: dict, transaction_type: str = None):
    for transaction in account["transactions"]:
        if transaction_type is None or transaction["type"] == transaction_type:
            yield transaction
