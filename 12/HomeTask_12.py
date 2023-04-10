print("Задание 1. Копия строки с удаленными гласными")
consonants_str = lambda x: "".join([symb
                                    for symb in x if symb.lower() not in (
                                        "а", "е", "ё", "о", "и", "ы", "у", "э", "ю", "я", "a", "e", "i", "o", "u")])

print(consonants_str("sosdufaaU96aa"))
# =================================================================================================================
print("Задание 2. Возврат True если строка содержит только буквы алфавита")
test_string = "100 грамм сыра пошехонского, порежь, да... и апельсин мне"
is_alphabet = lambda x: x.isalpha()
print(is_alphabet(test_string))
test_string = "Вооочередь"
print(is_alphabet(test_string))
test_string = "123\n"
print(is_alphabet(test_string))
# =================================================================================================================
print("Задание 3. Принимает список целых чисел, возвращает произведение чисел из списка.")
numbers = [2, 5, 3, 10]
# proud_from_list = lambda x: []
proud_from_list = lambda x: x[0] * proud_from_list(x[1:]) if x else 1
print(proud_from_list(numbers))
# =================================================================================================================
print("Задание 4. Из списка строк вернуть строки являющиеся палиндромами")
strings = ["тамамат", "в утро ртув", "кедровые орешки", "А буду я у дуба"]
poly_only = lambda x: [poly for poly in x if
                       [symb.lower() for symb in poly if symb.isalpha() and \
                        not symb.isspace()] == [symb.lower() for symb in poly if \
                                                symb.isalpha() and not symb.isspace()][::-1]]

print(poly_only(strings))
# =================================================================================================================
print("Задание 5. Вернуть True если число простое")
is_simple = lambda x: ((x > 1) and all([(x % div) for div in range(2, x // 2 + 1)]))
# is_simple = lambda x: [(x % div) for div in range(2, x // 2 + 1)]
print(is_simple(3))
print(is_simple(51))
print(is_simple(1))
print(is_simple(6))
print(is_simple(-17))
print(is_simple(16791))
# =================================================================================================================
print("Задание 6. Вернуть факториал числа")
# factorial = lambda x: [num[0] * factorial([num[1:]]) for num in enumerate(range(1, x + 1))]
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
print(factorial(11)) # 39916800
print(factorial(0)) # 1
print(factorial(5)) # 120
