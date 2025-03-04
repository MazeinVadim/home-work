a: int = 5
b: str = 'string'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s

print(indent('12', 12))