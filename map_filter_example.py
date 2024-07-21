'''
Написати функцію, яка буде приймати список з користувачів і фільтрувати дні народження, які були цього року
'''
from datetime import datetime

# [{'name': 'John', 'birthday': '21.07.2024'}, {'name': 'Alice', 'birthday': '21.07.2023'}]

# 1 - Перетворити дати-рядки на дати-datetime (map)
# 2 - Відсіяти людей, які народжені не цього року (filter)

def find_users_with_birthday_this_year(users: list[dict]) -> list[dict]: # fuwbty
    # 1 - Перетворити дати-рядки на дати-datetime (map)
    users_with_datetime_dates = []
    for user in users:
        birthday_datetime = datetime.strptime(user['birthday'], '%d.%m.%Y') 
        users_with_datetime_dates.append({'name': user['name'], 'birthday': birthday_datetime})

    # 2 - Відсіяти людей, які народжені не цього року (filter)
    users_with_birthday_this_year = []
    today = datetime.today()
    for user in users_with_datetime_dates:
        if user['birthday'].year != today.year:
            continue
        users_with_birthday_this_year.append(user)

    return users_with_birthday_this_year

# print(find_users_with_birthday_this_year([{'name': 'John', 'birthday': '21.07.2024'}, {'name': 'Alice', 'birthday': '21.07.2023'}]))

def convert_user_birthday_string_to_datetime(user: dict[str, str]) -> dict[str, str]:
    return {'name': user['name'], 'birthday': datetime.strptime(user['birthday'], '%d.%m.%Y')}
    # birthday_datetime = datetime.strptime(user['birthday'], '%d.%m.%Y') 
    # return {'name': user['name'], 'birthday': birthday_datetime}

def is_user_birthday_this_year(user: dict[str, str]) -> bool:
    # return user['birthday'].year == datetime.today().year
    today = datetime.today()
    return user['birthday'].year == today.year

def find_users_with_birthday_this_year_functional(users: list[dict]) -> list[dict]:
    users_with_datetime_dates = map(convert_user_birthday_string_to_datetime, users)
    return list(filter(is_user_birthday_this_year, users_with_datetime_dates))

# print(find_users_with_birthday_this_year_functional([{'name': 'John', 'birthday': '21.07.2024'}, {'name': 'Alice', 'birthday': '21.07.2023'}]))

def find_users_with_birthday_this_year_functional_lambda(users: list[dict]) -> list[dict]:
    users_with_datetime_dates = map(lambda user: {'name': user['name'], 'birthday': datetime.strptime(user['birthday'], '%d.%m.%Y')}, users)
    return list(filter(lambda user: user['birthday'].year == datetime.today().year, users_with_datetime_dates))




def is_user_birthday_this_year_complex(user: dict[str, str]) -> bool:
    # 1 - Перетворити дати-рядки на дати-datetime (map)
    birthday_datetime = datetime.strptime(user['birthday'], '%d.%m.%Y')
    # 2 - Відсіяти людей, які народжені не цього року (filter)
    return birthday_datetime.year == datetime.today().year

def find_users_with_birthday_this_year_functional_filter(users: list[dict]) -> list[dict]:
    return list(filter(is_user_birthday_this_year_complex, users))

print(find_users_with_birthday_this_year_functional_filter([{'name': 'John', 'birthday': '21.07.2024'}, {'name': 'Alice', 'birthday': '21.07.2023'}]))

lambda user: datetime.strptime(user['birthday'], '%d.%m.%Y').year \
                    == datetime.today().year