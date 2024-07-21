'''
Написати функцію, яка буде рахувати обʼєм, за допомогою карування
'''
from typing import Callable

# fn(3)(4)(5) -> 3 * 4 * 5 -> 60

def calculate_volume(a: int) -> Callable[[int], Callable[[int], Callable[[int], int]]]:
    def receive_height(b: int) -> Callable[[int], int]:
        def receive_width(c: int) -> int:
            return a * b * c
        return receive_width
    return receive_height

print(calculate_volume(3)(4)(5))

# [{'name': 'John'}, {'name': 'Jack'}]
# fn(2, 3)('J')