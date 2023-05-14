from abc import ABC, abstractmethod
from enum import Enum

print("Задание 1. Паттерн Command")


# рассчитываем цену на мощение дорожек в зависимости от статуса клиента и сезона выполнения работ
class Season(Enum):
    """Season price grade"""
    SUMMER = 1.5
    AUTUMN = 1.2
    SPRING = 1.3
    WINTER = 1


class Strategy(ABC):
    """Strategy's interface"""

    @abstractmethod
    def check_season(self, season: Season) -> float:
        ...

    @abstractmethod
    def work_processing(self, work_area: int, season) -> str:
        ...


class GoldenClientStrategy(Strategy):
    def __init__(self):
        self.paving_price = 800  # paving - мощение дорожек

    def check_season(self, season: Season) -> float:
        if season is not Season.SUMMER:
            return Season.WINTER.value
        return season.value

    def work_processing(self, work_area: int, season) -> str:
        return f"Work price for GOLDEN client is {work_area * self.check_season(season) * self.paving_price}"


class NormalClientStrategy(Strategy):
    def __init__(self):
        self.paving_price = 810

    def check_season(self, season: Season) -> float:
        return season.value

    def work_processing(self, work_area: int, season) -> str:
        return f"Work price for this client is {work_area * self.check_season(season) * self.paving_price}"


class Manager:
    def __init__(self, strategy: Strategy,
                 season: Season):
        self._strategy = strategy
        self._season = season
        print("-" * 40)
        print(f"For {season.name} season price grade is: {self._strategy.check_season(self._season)}")

    def get_season(self) -> Season:
        return self._season

    def set_season(self, season: Season) -> None:
        print(f"Order's season set as: {season.name}")
        self._season = season

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, work_area: int) -> None:
        print(f"Paving order for {work_area} m2")
        print(self._strategy.work_processing(work_area, self._season))
        print("-" * 40)


antonyG = Manager(NormalClientStrategy(), Season.SPRING)
antonyG.take_order(200)
antonyG = Manager(GoldenClientStrategy(), Season.SPRING)
antonyG.take_order(200)
antonyG = Manager(GoldenClientStrategy(), Season.SUMMER)
antonyG.take_order(200)
antonyG = Manager(NormalClientStrategy(), Season.SUMMER)
antonyG.take_order(200)
antonyG = Manager(NormalClientStrategy(), Season.WINTER)
antonyG.take_order(200)

# ===================================================================================
# ===================================================================================
print("\nЗадание 2. Набор чисел. Логирование")

from random import randint
import pickle


class Base(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Base, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class NumberCollection(metaclass=Base):
    def __init__(self):
        self.name = "SingletonNumberCollection"

    @staticmethod
    def generate_numbers() -> list:
        return [randint(-1000, 1000) for _ in range(randint(10, 500))]

    def save_numbers(self) -> int:
        with open("numbers.pkl", "wb") as f:
            new_numbers = self.generate_numbers()
            pickle.dump(new_numbers, f)
            return len(new_numbers)

    @staticmethod
    def load_numbers() -> list:
        with open("numbers.pkl", "rb") as f:
            return pickle.load(f)


numbers = NumberCollection()
print(numbers.generate_numbers())
numbers.save_numbers()
print(numbers.load_numbers())
numbers.save_numbers()
print(numbers.load_numbers())
numbers.save_numbers()
print(numbers.load_numbers())

# =================================================================

print("Задание 3. Библиотека.")

from datetime import datetime
import json


class Base(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Base, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Library(metaclass=Base):
    def __init__(self):
        self.name = "Town Library 'First and Last'"
        self.library = self.start_init()

    def start_init(self) -> dict:
        library = {"librarians": {"1": "Alex", "2": "Anna"},
                   "readers": {
                       "Vasiliy": {"age": 30, "access level": 1},
                       "Fedor": {"age": 13, "access level": 2},
                       "Olga": {"age": 5, "access level": 5}},
                   "books_in_library": {
                       "1": {"title": "Magic Secrets", "min access level": 5},
                       "2": {"title": "Gone with the Wind", "min access level": 2},
                       "3": {"title": "Logarithmic reference", "min access level": 1}}}
        self.save_status(library)
        return library

    def save_status(self, library):
        self.library = library
        with open('library.json', 'w') as f:
            json.dump(library, f, indent=2, sort_keys=True)

    @staticmethod
    def load_status() -> dict:
        with open('library.json', 'r') as f:
            library = json.load(f)
        return library


class ProxyLibrary():
    def __init__(self, real_subject: Library):
        self.__real_subject = real_subject

    def get_library(self):
        return self.__real_subject.library

    def out_print_log(self, str_to_out, to_print, to_log):
        if to_print: print(str_to_out)
        if to_log: self.__logging(str_to_out)

    def init_library(self, to_print=True, to_log=True):
        self.__real_subject.start_init()
        self.out_print_log("init library", to_print, to_log)

    def __save_library(self, library, to_print=True, to_log=True):
        self.__real_subject.save_status(library)
        self.out_print_log("save library", to_print, to_log)

    def load_library(self, to_print=True, to_log=True):
        library = self.__real_subject.load_status()
        self.out_print_log("load library", to_print, to_log)
        return library

    def find_book(self, book_title, to_print=True, to_log=True, return_access_level=False):
        books = self.get_library()["books_in_library"]
        result = [key for key, val in books.items() if val["title"] == book_title]
        was_found = " not" if not result else ""
        str_out = f"Book with '{book_title}' title was{was_found} found."
        self.out_print_log(str_out, to_print, to_log)
        if return_access_level and result:
            return books[result[0]]['min access level']
        else:
            return bool(result)

    def find_librarian(self, librarian_name, to_print=True, to_log=True):
        librarians = self.get_library()["librarians"]
        result = [val for key, val in librarians.items() if val == librarian_name]
        was_found = " not" if not result else ""
        str_out = f"Librarian with '{librarian_name}' title was{was_found} found."
        self.out_print_log(str_out, to_print, to_log)
        return bool(result)

    def find_reader(self, reader_name, to_print=True, to_log=True):
        readers = self.get_library()["readers"]
        result = [key for key in readers if key == reader_name]
        was_found = " not" if not result else ""
        str_out = f"Reader '{reader_name}' was{was_found} found."
        self.out_print_log(str_out, to_print, to_log)
        return bool(result)

    def delete_reader(self, reader_name, to_print=True, to_log=True):
        library: dict = self.get_library()
        # if readers.pop(reader_name, False):
        if library["readers"].pop(reader_name, False):
            str_out = f"Reader '{reader_name}' was deleted."
            self.__save_library(library)
        else:
            str_out = f"Reader '{reader_name}' was not found."
        self.out_print_log(str_out, to_print, to_log)

    def print_library(self, to_print=True, to_log=True):
        print(self.get_library())
        str_out = "Library was printed out"
        self.out_print_log(str_out, to_print, to_log)

    def print_books(self, to_print=True, to_log=True):
        print(self.get_library()['books_in_library'])
        str_out = "Books were printed out"
        self.out_print_log(str_out, to_print, to_log)

    def print_readers(self, to_print=True, to_log=True):
        print(self.get_library()['readers'])
        str_out = "Readers were printed out"
        self.out_print_log(str_out, to_print, to_log)

    def change_readers(self, reader_to_change, to_print=True, to_log=True):
        if self.find_reader(reader_to_change, False, False):
            library = self.get_library()
            library["readers"][reader_to_change]["age"] = int(input(f"Input new age for {reader_to_change}: "))
            library["readers"][reader_to_change]["access level"] = int(
                input(f"Input access level for {reader_to_change}: "))
            self.__save_library(library, False, False)
            str_out = f"Data for reader {reader_to_change} was changed"
        else:
            str_out = f"Data for {reader_to_change} was not changed. Reader was not found."
        self.out_print_log(str_out, to_print, to_log)

    def check_access_for_book(self, reader, book_title, to_print=True, to_log=True):
        str_out = f"{reader} has not access to book '{book_title}'"
        is_access = False
        if self.find_reader(reader, False, False) and self.find_book(book_title, False, False):
            library = self.get_library()
            is_access = library["readers"][reader]["access level"] <= self.find_book(book_title, False, False,
                                                                                     return_access_level=True)
            if is_access: str_out = f"{reader} has access to book '{book_title}'"
        self.out_print_log(str_out, to_print, to_log)
        return is_access

    def add_book_to_library(self, new_book_title: str, access_level: int, to_print=True, to_log=True):
        library = self.get_library()
        new_key = str(max(map(int, library["books_in_library"])) + 1)
        library["books_in_library"][new_key] = {"title": new_book_title}
        library["books_in_library"][new_key] = {"min access level": access_level}
        self.__save_library(library, to_log=True)
        str_out = f"New book '{new_book_title}' was added to library"
        self.out_print_log(str_out, to_print, to_log)

    @staticmethod
    def __logging(operation=None) -> None:
        with open("log_library.txt", "a") as f:
            f.write(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} : {operation}\n")


my_library = Library()
librarian = ProxyLibrary(my_library)
librarian.init_library()
librarian.find_book("Magic Secrete", to_log=False)
librarian.find_librarian("Alex")
librarian.find_librarian("Alexis")
librarian.find_reader("Vasiliy")
librarian.find_reader("Vasilisa")
librarian.delete_reader("Vasiliy")
librarian.delete_reader("Vasia")
librarian.print_library()
librarian.print_readers()
librarian.change_readers("Fedor")
librarian.check_access_for_book("Olga", "Magic Secrets")
librarian.check_access_for_book("Fedor", "Logarithmic reference")
librarian.add_book_to_library("Ice and Flame", 3)
