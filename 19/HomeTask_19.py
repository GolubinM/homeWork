import re


# ============================================================================================
def check(string):
    if (re.search(regx, string)):
        print("Valid:", (re.search(regx, string).string))
    else:
        print("\t\tInvalid:", string)


# ============================================================================================
print("\nЗадание 1. Начало строки - гласная, конец - согласная.")
# Напишите регулярное выражение, которое соответствует
# всем строкам, начинающимся с гласной и заканчивающимся
# на согласную.
vowels = 'аеёоиыуэюяaeiou'
regx = f'(?i)^[{vowels}].*[^{vowels}_\W\d]$'

string = "А лапа упал"
check(string)
string = "Аполлон-13"
check(string)
string = "А лапа упала"
check(string)
string = "А лапа упала! "
check(string)
string = "I'm tall"
check(string)
string = "I'm free"
check(string)
string = "I'm freek_"
check(string)

# ============================================================================================
print("\nЗадание 2. URL.")
# Напишите регулярное выражение, которое соответствует
# всем URL-aдpecaм.
regex = r"https?:\/\/[\w]+((?<=localhost)(:\d+)?|\S+(\.[a-zа-я]{2,6}))(?(3)/(\S+)?(\?/S+)?)"
# Не уверен, что это корректно, но ввел проверку на наличие домена длинной 2-6 символов если в
# адресе не присутствует localhost. Добавил кириллицу в проверку домена. Возможность указывать запрос.
# Исключил возможность наличия пробелов в строке с URL. Смирился с необъятностью задачи.
# Принял за корректные, URL в строках с индексами: 1, 3-5.

test_str = ("https://3dwarehouse\n"
            "https://3dwarehouse.sketchup.com/\n"
            "https://3dwarehouse.sketchupcom/\n"
            "http://localhost:8080\n"
            "https://blog.sketchup.com/article/revit-importer-delivers-flexible-workflows\n"
            "https://www.google.com/search?q=regex\n"
            "https://www.w3 schools.com/python/python_dictionaries.asp")

matches = re.finditer(regex, test_str)
[print("\t", match.group()) for match in matches]

# ============================================================================================
print("\nЗадание 3. Строки, содержащие хотя бы одно слово с большой буквы.")
# Напишите регулярное выражение, которое соответствует
# всем строкам, содержащим хотя бы одно слово,
# начинающееся с заглавной буквы.
regex = r"(^[A-ZА-ЯЁ].*)|(.*\b[A-ZА-ЯЁ]+.*)"

test_str = ("А лапа упала\n"
            "\"А лапа упала\"\n"
            "(А лапа упала)\n"
            "O!...\n"
            "5\n"
            "а Папа упал\n"
            "а лаПа упала\n"
            "see (You) next week\n"
            "so vuLnerable\n"
            "But tomorrow never comes")

matches = re.finditer(regex, test_str)
[print("\t", match.group()) for match in matches]

print("\nЗадание 4. Строки с повторяющейся буквой")
# Напишите Регулярное выражение, которое соответствует
# всем строкам, содержащим повторяющуюся букву (например,
# «book» или «letter»).
regex = r".*([a-zA-Zа-яА-ЯЁё])\1.*"

test_str = ("А лапа упала 11 раз\n"
            "Длинношеее животное\n"
            "next week\n"
            "But tomorrow never comes\n")

matches = re.finditer(regex, test_str)
[print("\t", match.group()) for match in matches]
