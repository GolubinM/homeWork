from functools import wraps

print("\nЗадание 1. Декоратор ограничивающий кол-во функций")


def taking_parametrs(count):
    def taking_function(func):
        @wraps(func)
        def taking_arguments():
            nonlocal count
            if count > 0:
                func()
                count -= 1
            else:
                raise ValueError("Ошибка")

        return taking_arguments

    return taking_function


@taking_parametrs(4)
def hello_world():
    """Function prints 'Hello, world!'"""
    print("Hello, world!")


print(f"Called function name is {hello_world.__name__}. {hello_world.__doc__}")
hello_world()
hello_world()
hello_world()
hello_world()


@taking_parametrs(4)
def goodbye_winter():
    """Function prints 'Goodbye, Winter'"""
    print("Goodbye, Winter!")


print(f"Called function name is {goodbye_winter.__name__}. {goodbye_winter.__doc__}")
goodbye_winter()
goodbye_winter()
goodbye_winter()
goodbye_winter()
goodbye_winter()

# Задание 2. Декоратор validate_args ===================================================
print("\nЗадание 2. Декоратор validate_args")


def validate_args(*types, **kwtypes):
    def taking_function(func):
        def taking_arguments(*args, **kwargs):
            if [*types] + [*kwtypes.values()] == list(map(type, [*args] + [*kwargs.values()])):
                func(*args, **kwargs)
            else:
                raise TypeError

        return taking_arguments

    return taking_function


@validate_args(int, a=str)
def print_range_days(days, period):
    print(f"period {days} days is {period}")


print_range_days(7, "week")  # period 7 days is week
print_range_days(365, "year")  # period 365 days is year
print_range_days(365, True)  # Выдаст ошибку TypeError


@validate_args(int, float, int, s=str, flag=bool)
def print_beauty_sqr(num, per, precise, decor, flag):
    result = num ** per
    if flag:
        print(decor * 15, round(result, precise), decor * 15)
    else:
        print(result)


print_beauty_sqr(2, 0.3, 2, "~", True)  # ~~~~~~~~~~~~~~~ 1.23 ~~~~~~~~~~~~~~~
print_beauty_sqr(2, 0.3, 2, "~", False)  # 1.2311444133449163
print_beauty_sqr(2.0, 0.3, 2, "~", False)  # Выдаст ошибку TypeError
