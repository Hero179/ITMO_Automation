def task_1(a: int, b: float, c: str, d: list, e: bool):
    a: int = 1
    print(a, "относится к типу ", type(a))
    b: float = 2.10
    print(b, "относится к типу ", type(b))
    c: str = 'hello'
    print(c, "относится к типу ", type(c))
    d: list = [1, 2, 3]
    print(d, "относится к типу ", type(d))
    e: bool = True
    print(e, "относится к типу ", type(e))
    return a, b, c, d, e


def task_2(a: list):
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[1:3])
    return a
    # Последовательность Фибоначчи


def task_3(a: int = 6):
    return a**2

print(task_3())











