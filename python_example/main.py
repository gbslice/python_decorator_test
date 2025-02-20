from functools import wraps
from typing import Concatenate
from collections.abc import Callable

class Client:
    def __init__(self) -> None:
        self.data = "some_data"

def decorate[**P, R](func: Callable[Concatenate[Client, P], R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(Client(), *args, **kwargs)
        except Exception as e:
            # handle exception
            raise e

    return wrapper


@decorate
def func_1(client: Client) -> None:
    print(client.data)

# # Will throw type error
# @decorate
# def func_2() -> None:
#     print("rad")

@decorate
def func_3(client: Client, value: int) -> int:
    return value * 2

func_1()
# func_2()
func_3(10)
