from functools import lru_cache  # Decorador, armazena o retorno em cache


@lru_cache(maxsize=None)  # maxsize indica quantas chamadas devem ser armazenadas. "None" significa sem limite
def fib4(n: int) -> int:
    if n < 2:  # caso de base
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursão


if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
