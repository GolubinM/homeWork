# 1. Замыкание, которое повторно применяет f к своему выводу, пока p не вернет True
print("\nЗадание 1. Замыкание, которое повторно применяет f " + "=" * 25)


def half(x):
    return x // 2


def is_even(x):
    return x % 2 == 0


def repeat_until(fn1, fn2):
    result = 0

    def check_result(x):
        nonlocal result
        result = fn1(x)
        if fn2(result):
            return result
        else:
            check_result(result)
        return result

    return check_result


repeat_until_half_even = repeat_until(half, is_even)
print(repeat_until_half_even(19))
print(repeat_until_half_even(22))

# 2. Функция make_counter===================================================
print("\nЗадание 2. Функция make_counter " + "=" * 25)


def make_counter(cnt: int):
    count = cnt

    def counter():
        nonlocal count
        if count < 0:
            print("Error: counter has reached 0")
        else:
            print(count)
            count -= 1
        # return count

    return counter


c = make_counter(3)
c()
c()
c()
c()
c()

# 3. Функция print_once===================================================
print("\nЗадание 3. Функция print_once " + "=" * 25)


def hello_world():
    print("Hello, world!")


def print_once(foo1):
    count = 1

    def chek_counter():
        nonlocal count
        if count:
            foo1()
            count = 0

    return chek_counter


hello_once = print_once(hello_world)
hello_once()
hello_once()
hello_once()
