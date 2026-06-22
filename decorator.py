import functools
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def log(function):
    @functools.wraps(function)
    def pack_log(*args, **kwargs):
        arguments = None
        date = datetime.now()
        response = function(*args, **kwargs)

        if args and kwargs:
            arguments = args + kwargs
        elif args:
            arguments = args
        elif kwargs:
            arguments = kwargs
        else:
            arguments = "No arguments"

        log = f"Running: {function.__name__} on {date} - Arguments: \
            {arguments} - Type: {type(response)}. Return: {response}\n"
        try:
            with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as data:
                data.write(log)
        except IOError as err:
            print(f"Erro ao manipular o arquivo: {err}")

        return response

    return pack_log
