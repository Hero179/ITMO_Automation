# a: int = 5
# b: str = 'hello'
# c: list = [1, 2, 3]
#
# def indet(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s
#
# print(indet('123', 123))

def lenstr(s: str = '') -> int:
    return len(s)

def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))



