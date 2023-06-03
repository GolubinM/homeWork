# 1. Напишите функцию analysis_and_summarize_file, которая принимает имя файла в
# качестве входных данных. Файл содержит большое количество текстовых данных.
# Функция должна прочитать содержимое файла, проанализировать данные для сбора
# соответствующей информации (например, частота слов, количество строк, средняя длина слова)
# и создать сводный отчет в новом файле.
import json
import re


def analysis_and_summarize_file(filename):
    def get_word_frequency_stat(text_to_analyse):
        regex = r"\b\w+"
        words = re.finditer(regex, text_to_analyse, re.MULTILINE)
        mydict = {}
        for word in words:
            elm = word.group().lower()
            mydict[elm] = mydict.setdefault(elm, 0) + 1
        sorted_dict = dict(sorted(mydict.items(), key=lambda item: item[1], reverse=True))
        return sorted_dict

    def get_average_words_length(words_dict):
        return sum([len(key) * value for key, value in words_dict.items()]) / sum(words_dict.values())

    def save_result(file_name, text_statistic):
        with open(file_name, "w") as jsonf:
            json.dump(text_statistic, jsonf)

    with open(filename, "r") as f:
        file_content = f.readlines()
    statistic_text = {'strings_count': len(file_content)}
    file_content = "".join([line.rstrip() for line in file_content])
    if statistic_text['strings_count']:
        statistic_text['word_frequency'] = get_word_frequency_stat(file_content)
        statistic_text['average_words_length'] = get_average_words_length(statistic_text['word_frequency'])
    statistic_filename = "statistic.json"
    save_result(statistic_filename, statistic_text)


analysis_and_summarize_file("Austin Pride and Prejudice.txt")

# **************************************************************


# Зашифровал простым сдвигом кода символа на N.
from datetime import datetime


def taking_parametrs():
    def taking_function(func):
        def logging(*args, **kwargs):
            func(*args, **kwargs)
            enckey = args[1] if args else kwargs.get("enc_key")
            file_name = args[0] if args else kwargs.get("file_name")
            with open("log_encrypt.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} : filename: '{file_name}', enckey: {enckey}\n")

        return logging

    return taking_function


@taking_parametrs()
def encrypt_file(file_name, enc_key):
    def encrypter(str_list, enc_key):
        encrypt_str_list = []
        for str_elm in str_list:
            encrypt_str = ""
            for sym in str_elm:
                if ord(sym) % 2:
                    encrypt_str += chr(ord(sym) + enc_key + odder)
                else:
                    encrypt_str += chr(ord(sym) + enc_key - 4 + odder)
            encrypt_str_list.append(encrypt_str)
        return encrypt_str_list

    try:
        if (type(enc_key) is int) and (0 < enc_key < 20):
            pass
        else:
            raise ValueError("Ключ неверного формата")
    except ValueError as e:
        print(e)
    with open(file_name, encoding='utf-8') as f:
        content = f.readlines()
    odder = enc_key % 2
    content = [elm.rstrip() for elm in content]
    encrypt_content = encrypter(content, enc_key)
    encrypt_txt = "\n".join(encrypt_content)
    encrypt_filename = file_name.replace(".txt", ".rsa")
    with open(encrypt_filename, "w", encoding='utf-8') as f:
        f.write(encrypt_txt)


@taking_parametrs()
def decrypt_file(file_name, enc_key):
    def decrypter(str_list, enc_key):
        decrypt_str_list = []
        for str_elm in str_list:
            decrypt_str = ""
            for sym in str_elm:
                if ord(sym) % 2:
                    decrypt_str += chr(ord(sym) - enc_key - odder)
                else:
                    decrypt_str += chr(ord(sym) - enc_key + 4 - odder)
            decrypt_str_list.append(decrypt_str)
        return decrypt_str_list

    try:
        if (type(enc_key) is int) and (0 < enc_key < 20):
            pass
        else:
            raise ValueError("Ключ неверного формата")
    except ValueError as e:
        print(e)
    with open(file_name, encoding='utf-8') as f:
        content = f.readlines()
    odder = enc_key % 2
    content = [elm.rstrip() for elm in content]
    decrypt_content = decrypter(content, enc_key)
    decrypt_txt = "\n".join(decrypt_content)
    decrypt_filename = file_name.replace(".rsa", "_a.txt")
    with open(decrypt_filename, "w", encoding='utf-8') as f:
        f.write(decrypt_txt)


encrypt_file("Домашние задачи.txt", 15)
decrypt_file("Домашние задачи.rsa", 15)
encrypt_file("Задачи.txt", 12)
decrypt_file("Задачи.rsa", 12)

# **********************************************************************

# 3. Напишите функцию с именем analysis_file_sizes, которая принимает путь к каталогу
# в качестве входных данных. Функция должна рекурсивно обходить каталог и его подкаталоги и
# вычислять общий размер всех файлов, содержащихся в них. Результат должен быть возвращен в
# удобочитаемом формате, например, в килобайтах (КБ), мегабайтах (МБ) или гигабайтах (ГБ).
# Реализуйте эту функциональность с помощью модуля os в Python.


import os


def get_folders_content(fold_path="", tab=0):
    def get_comfort_size(size):
        if size <= 1000000:
            return f"{size / 1024:.3f}Kb"
        elif 1000000 < size <= 1000000000:
            return f"{size / 1024 ** 2:.3f}Mb"
        elif 1000000000 < size <= 1000000000000:
            return f"{size / 1024 * 3:.3f}Gb"
        elif 1000000000000 < size:
            return f"{size / 1024 * 3:.3f}Tb"

    with os.scandir(fold_path) as files:
        files = sorted(files, key=lambda elm: elm.is_dir())
        files_size = 0
        count_files = 0
        for file in files:
            if file.is_dir():
                print(" " * tab, f"{file.name}\\")
                get_folders_content(file, tab + 5)
            else:
                file_stats = os.stat(file)
                print(" " * tab, file.name, f' {get_comfort_size(file_stats.st_size)}')
                count_files += 1
            files_size += os.path.getsize(file)

        print(" " * tab, "-", f"всего файлов в папке: ", count_files, "размер файлов в папке: ",
              get_comfort_size(files_size))
        return


get_folders_content("C:/test")
