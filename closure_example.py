'''
Написати функцію, яка буде генерувати унікальний ідентифікатор для користувачів
'''

id = 0

def get_unique_id() -> int:
    global id
    id += 1
    return id

# print(get_unique_id())
# print(get_unique_id())
# print(get_unique_id())


def get_unique_id_closure() -> int:
    id = 0
    def get_next_id():
        nonlocal id
        id += 1
        return id
    return get_next_id

next_number_function = get_unique_id_closure()
print(next_number_function())
print(next_number_function())
print(next_number_function())
