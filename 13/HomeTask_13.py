# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.
tuple_int_0 = tuple(range(0, 15))
tuple_int_1 = tuple(range(5, 20))
tuple_int_2 = tuple(range(10, 25))
nums = (elm for elm in tuple_int_0 if elm in tuple_int_1 and elm in tuple_int_2)
print("Элементы, которые есть во всех кортежах:", *nums)

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого кортежа.
tuple_int_0 = tuple(range(0, 10))
tuple_int_1 = tuple(range(5, 20))
tuple_int_2 = tuple(range(15, 25))
nums = (elm for elm in tuple_int_0 if elm in tuple_int_1 and elm in tuple_int_2)
print("Уникальные элементы для списка:")
print("tuple_int_0: ", *(elm for elm in tuple_int_0 if elm not in tuple_int_1 and elm not in tuple_int_2))
print("tuple_int_1: ", *(elm for elm in tuple_int_1 if elm not in tuple_int_0 and elm not in tuple_int_2))
print("tuple_int_2: ", *(elm for elm in tuple_int_2 if elm not in tuple_int_0 and elm not in tuple_int_1))

# Задание 3
# Есть три кортежа целых чисел необходимо найти эле-
# менты, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.
tuple_int_0 = (1, 2, 3, 4, 5)
tuple_int_1 = (1, 3, 2, 4, 6)
tuple_int_2 = (1, 3, 2, 4, 4)
nums_3 = (elm for elm in enumerate(tuple_int_0) if elm in enumerate(tuple_int_1) and elm in enumerate(tuple_int_2))
print("Элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.")
[print(f'элемент с индексом: {elm[0]} и значением:  {elm[1]}') for elm in nums_3]
