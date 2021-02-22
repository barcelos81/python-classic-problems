# Erro de recursão infinita. Falta a especificação de casos de base

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


if __name__ == "__main__":
    print(fib1(5))
