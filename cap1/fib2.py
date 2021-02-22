# Funciona com números pequenos. As chamadas de recursividade aumentam exponencialmente
def fib2(n: int) -> int:
    if n < 2:  # caso de base
        return n
    return fib2(n - 2) + fib2(n - 1)  # recusrsão


if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
