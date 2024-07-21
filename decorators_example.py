'''
Написати декоратор, який буде замірювати час виконання функції
'''
import time
from functools import wraps

# def time_function(func):
#     # def wrapper(*args, **kwargs)
#     def wrapper(numbers):
#         result = func(numbers)
#         return result
#     return wrapper

def time_function(func):
    @wraps(func)
    # Second way to use *
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs) # sum(numbers) # First way to use *
        end_time = time.time()
        print(f'Function {func.__name__} running time: {end_time - start_time}')
        return result
    return wrapper

# time_function(calculate_sum)(numbers)

@time_function
def calculate_sum(numbers: list[int]) -> int:
    return sum(numbers)

@time_function
def square(number: int) -> int:
    return number ** 2

@time_function
def add(number_one: int, number_two: int) -> int:
    return number_one + number_two

# add(number_one=1, number_two=2)
# square(5)
# print(dir(add))
# print(add.__name__)

# First way to use *
def concatenate_strings(str_one, str_two):
    return f'{str_one} {str_two}'

lst = ['Hello', 'world']
my_dict = {'str_one': 'Hello', 'str_two': 'world'}

# print(concatenate_strings(lst[0], lst[1]))
concatenate_strings(*lst)
concatenate_strings(**my_dict)

# Second way to use *
def calculate_sum_two(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(calculate_sum_two(1, 2, 3, 4))

lst = [1, 2, 3, 4, 5]

print(calculate_sum_two(*lst))

def concat_words(**kwargs):
    result = ''
    for key, value in kwargs.items():
        print(key)
        result += ' ' + value
    return result

my_dict = {'str_one': 'Hello', 'str_two': 'world'}

# print(concat_words(first_name='John', last_name='Doe'))
# print(concat_words(**my_dict))

@time_function
def my_function(*args, **kwargs):
    pass

# {**user, ‘birthdate’: birthdate}

print(my_function.__name__)
