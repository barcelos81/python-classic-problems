def fib5(n: int) -> int:
    if n == 0:
        return n  # caso especial
    last: int = 0  # fib5(0)
    next: int = 1  # fib5(1)
    for _ in range(1, n):
        last, next = next, last + next  # Desempacotamento de tuplas
    return next

# last é definido com valor anterior de next
# next é definido com valor anterior de last + valor anterior de next


if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))
