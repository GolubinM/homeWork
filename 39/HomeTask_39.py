# Задание 1.
class CustomerManager:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, customer_name):
        self.customers.setdefault(customer_id, {"customer_name": customer_name})
        # self.customers.setdefault(customer, {"name": customer})

    def update_customer(self, customer, new_key=None, new_info=None):
        if customer in self.customers:
            self.customers[customer][new_key] = new_info

    def get_customer(self, customer_key):
        if customer_key in self.customers:
            return self.customers[customer_key]
        else:
            return False


maria = CustomerManager()
print(maria.customers)
maria.add_customer("Soap", "Soap")
maria.add_customer("Fork", "Fork")
maria.add_customer("Glass", "Glass")
print(maria.customers)
maria.update_customer("Soap", "price", "mypost1949@gmail.com")
maria.update_customer("Ivan Swan", "price", "mypost1949@gmail.com")
maria.update_customer("Fork", "price", "mypost1986@gmail.com")
maria.update_customer("Fork", "discount", "Moscow")
maria.update_customer("Glass", "price", "mypost2005@gmail.com")
maria.update_customer("Glass", "discount", "London")
print("-*-" * 40)
print(maria.customers)


class ProductInventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, product_name):
        self.products.setdefault(product_id, {"product_name": product_name})
        # self.products.setdefault(product, {"name": product})

    def update_product(self, product, new_key=None, new_info=None):
        if product in self.products:
            self.products[product][new_key] = new_info

    def get_product(self, product_key):
        if product_key in self.products:
            return self.products[product_key]
        else:
            return False


print("-*-" * 40)
inventor1 = ProductInventory()
inventor1.add_product("Soap", "Soap")
inventor1.add_product("Fork", "Fork")
inventor1.add_product("Glass", "Glass")
print(inventor1.products)
inventor1.update_product("Soap", "price", 100)
inventor1.update_product("Ivan Swan", "price", 200)
inventor1.update_product("Fork", "price", 300)
inventor1.update_product("Fork", "discount", 0.85)
inventor1.update_product("Glass", "price", 400)
inventor1.update_product("Glass", "discount", 0.95)
print("-*-" * 40)
print(inventor1.products)


# Задание 2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.publishing = None


class FictionBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.main_hero_name = []

    def get_main_hero_name(self):
        return self.main_hero_name


class NonFictionBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.kind_of_book = []

    def get_kind_of_book(self):
        return self.kind_of_book


class ReferenceBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.industry_type_of = []

    def get_industry_type_of(self):
        return self.industry_type_of


# Задание 3

from abc import ABC, abstractmethod


class Shape(ABC):
    pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 3.14 * self.radius * 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a + self.b

    def calculate_perimeter(self):
        return 2 * (self.a + self.b)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        p = (self.b + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def calculate_perimeter(self):
        return self.a + self.b + self.c


# Задание 4

class Messanger:
    def send_message(self, formatted_message):
        # send TWAIN
        pass

    @staticmethod
    def receive_message():
        # receive TWAIN
        return "message in special format"


class TextMessaging(Messanger):
    def __init__(self):
        self.message_history = []

    def send_text_message(self, sender, receiver, text_message: str):
        message = ([ctime(), sender, receiver, self.convert_message_to_send_format(text_message)])
        self.message_history.append([ctime(), sender, receiver, text_message])
        self.send_message(message)

    @staticmethod
    def convert_message_to_send_format(text_message):
        formatted_msg = f"some convert procedure to comfortable format of: {text_message}"
        return formatted_msg

    @staticmethod
    def convert_message_from_send_format(formatted_message):
        text_message = f"some convert procedure to comfortable format of: {formatted_message}"
        return text_message

    def receive_text_message(self):
        formatted_text_message = self.receive_message()
        self.message_history.append(self.convert_message_from_send_format(formatted_text_message))

    def get_message_history(self):
        print(self.message_history)
        return self.message_history


class MultimediaMessaging(Messanger):
    def __init__(self):
        self.media_gallery = []

    def send_multimedia_message(self, sender, receiver, multimedia_content):
        message = ([ctime(), sender, receiver, self.convert_message_to_send_format(multimedia_content)])
        self.media_gallery.append(multimedia_content)
        self.send_message(message)

    @staticmethod
    def convert_message_to_send_format(multimedia_content):
        formatted_multimedia = f"some convert procedure to comfortable format of: {multimedia_content}"
        return formatted_multimedia

    @staticmethod
    def convert_message_from_send_format(formatted_multimedia):
        multimedia_content = f"back convert procedure to multimedia format of: {formatted_multimedia}"
        return multimedia_content

    def receive_multimedia_message(self):
        formatted_multimedia = self.receive_message()
        self.media_gallery.append(self.convert_message_from_send_format(formatted_multimedia))

    def view_media_gallery(self):
        for media in self.media_gallery:
            print(f"-*{media}*-")


# задание 5
import os
from time import ctime


class Logger:
    def log_info(self, log_msg):
        raise NotImplementedError

    def log_warning(self, log_msg):
        raise NotImplementedError

    def log_error(self, log_msg):
        raise NotImplementedError


class ConsoleLogger(Logger):
    def __init__(self):
        self.counter = 0

    def log_info(self, log_msg):
        self.counter += 1
        print(f"{self.counter} {ctime()} :{log_msg}")
        if "some wrong message" in log_msg:
            self.log_warning(log_msg)
        return True

    def log_warning(self, log_msg):
        print(f"{ctime()}: There is some wrong message. Check it as soon as possible!")
        return True

    def log_error(self, log_msg):
        print(f"{ctime()}: Log is not created. Error 4010")


class FileLogger(Logger):
    def __init__(self, log_filename):
        self.log_filename = log_filename

    def log_info(self, log_msg):
        with open(self.log_filename, 'a', encoding="utf-8") as f:
            f.write(log_msg + "\n")
        if os.path.getsize(self.log_filename) > 1 * 1024 ** 5:
            self.log_warning(log_msg)
        return True

    def log_warning(self, log_msg):
        print("Log file is too big. Please, create log_file copy and reset storage file")

    def log_error(self, log_msg):
        print("It's not possible to write log to file. Err 4020")
        return False


class DatabaseLogger(Logger):
    def __init__(self):
        self.data_base = []

    def log_info(self, log_msg):
        self.data_base.append(log_msg)
        if len(self.data_base) > 1 * 10 ** 8:
            self.log_warning(log_msg)
        return True

    def log_warning(self, log_msg):
        self.data_base.append(log_msg)
        print("Warning! It's necessary to enlarge space to save data.")
        return True

    def log_error(self, log_msg):
        print("It's not possible to create log. Err 4030")
        return False


class LoggingSystem:
    @staticmethod
    def __create_log(logger: Logger, log_msg: str):
        if not log_msg:
            logger.log_error(log_msg)
        else:
            logger.log_info(log_msg)

    def do_log(self, logger: Logger, log_msg: str):
        self.__create_log(logger, log_msg)
