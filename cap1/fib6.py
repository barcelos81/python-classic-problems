# Gerador da sequência de Fibonacci
from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # caso especial
    if n > 0: yield 1  #caso especial
    last: int = 0  # fib6(0)
    next: int = 1  # fib6(1)
    for _ in range(1, n):
        last, next = next, last + next  # Desempacotamento de tuplas
        yield next

# last é definido com valor anterior de next
# next é definido com valor anterior de last + valor anterior de next


if __name__ == "__main__":
    for i in fib6(50):
        print(i)
