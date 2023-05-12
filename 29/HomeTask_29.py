print("# Задание 1")
print("# Создайте реализацию паттерна Builder. Протестируйте работу созданного класса.")


class Drink:
    def __init__(self, name):
        self.name = name
        self.hot = False
        self.alcohol = False
        self.spice = []

    def __str__(self):
        string = self.name + '\n'
        if self.hot:
            string += "HOT "
        if self.alcohol:
            string += "ALCOHOL "
        else:
            string += "DRINK\n"
        if self.spice:
            string += "Spice:\n"
        for some in self.spice:
            string += "\t- " + str(some) + "\n"
        return string


class Olive:
    def __str__(self):
        return "olive"


class Lemon:
    def __str__(self):
        return "lemon"


class Sugar:
    def __str__(self):
        return "sugar"


class Pepper:
    def __str__(self):
        return "pepper"


class Ice:
    def __str__(self):
        return "ice"


class Milk:
    def __str__(self):
        return "milk"


class Spice:
    def __str__(self):
        return "super spice"


from abc import ABC, abstractmethod


class Barmen(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_spice(self):
        pass

    @abstractmethod
    def add_ice(self):
        pass


class HotSpiceCoffeeCreator(Barmen):
    def __init__(self):
        self.product = Drink("Turkey coffee")

    def reset(self):
        self.product = Drink()

    def get_product(self):
        return self.product

    def add_spice(self):
        self.product.hot = True
        self.product.spice.append(Pepper())
        self.product.spice.append(Sugar())

    def add_ice(self):
        pass


class BlackCoffeeCreator(Barmen):
    def __init__(self):
        self.product = Drink("Black coffee")

    def reset(self):
        self.product = Drink()

    def get_product(self):
        return self.product

    def add_spice(self):
        self.product.hot = True

    def add_ice(self):
        pass


class IceTeaCreator(Barmen):
    def __init__(self):
        self.product = Drink("Ice sugar tea")

    def reset(self):
        self.product = Drink()

    def get_product(self):
        return self.product

    def add_spice(self):
        self.product.spice.append(Sugar())

    def add_ice(self):
        self.product.spice.append(Ice())


class MartiniCocktail(Barmen):
    def __init__(self):
        self.product = Drink("Martini cocktail")

    def reset(self):
        self.product = Drink()

    def get_product(self):
        return self.product

    def add_spice(self):
        self.product.alcohol = True
        self.product.spice.append(Lemon())
        self.product.spice.append(Olive())

    def add_ice(self):
        self.product.spice.append(Ice())


garcone2 = MartiniCocktail()
garcone2.add_spice()
garcone2.add_ice()
print(garcone2.get_product())

garcone2 = IceTeaCreator()
garcone2.add_spice()
garcone2.add_ice()
print(garcone2.get_product())

garcone2 = BlackCoffeeCreator()
garcone2.add_spice()
print(garcone2.get_product())


class Director:

    def make_martini(self, barmen):
        barmen.add_spice()
        barmen.add_ice()
        return barmen.get_product()

    def make_IceTea(self, barmen):
        barmen.add_spice()
        barmen.add_ice()
        return barmen.get_product()

    def make_BlackCoffee(self, barmen):
        barmen.add_spice()
        return barmen.get_product()

    def make_TurkeyCoffee(self, barmen):
        barmen.add_spice()
        return barmen.get_product()


director = Director()
barmen = HotSpiceCoffeeCreator()
print(director.make_TurkeyCoffee(barmen))

print("\n""# Задание 2")
print("# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.")


# Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

def pasta_restaurant():
    class Pasta:
        def __init__(self, name):
            self.name = name
            self.price = 100
            self.catchup = False
            self.souse = False
            self.ingridients = []

        def __str__(self):
            string = "\n" + "*" * 25 + "\n" + self.name + "\n"
            if self.catchup:
                string += "with catchup\n"
            if self.souse:
                string += "with souse\n "
            string += "-" * 25 + "\n"
            if self.ingridients:
                string += "Ingridients:\n"
            for some in self.ingridients:
                string += "\t- " + str(some) + "\n"
            string += "-" * 25 + "\n" + f"price is {self.price}\n" + "*" * 25 + "\n" * 2
            return string

    class Mushrooms:
        def __str__(self):
            return "mushrooms"

    class Cheese:
        def __str__(self):
            return "Cheese"

    class Shrimps:
        def __str__(self):
            return "shrimps"

    from abc import ABC, abstractmethod

    class Chef(ABC):
        @abstractmethod
        def reset(self):
            pass

        @abstractmethod
        def add_catchup(self):
            pass

        @abstractmethod
        def add_souse(self):
            pass

        @abstractmethod
        def add_ingridients(self):
            pass

    class PastaMushroomCreator(Chef):
        def __init__(self):
            self.product = Pasta("Pasta with mushrooms")
            self.product.price = 190

        def reset(self):
            self.product = Pasta("Pasta with mushrooms")

        def get_product(self):
            return self.product

        def add_ingridients(self):
            self.product.ingridients.append(Mushrooms())

        def add_catchup(self):
            self.product.catchup = True

        def add_souse(self):
            pass

    class PastaWithCheeseCreator(Chef):
        def __init__(self):
            self.product = Pasta("Cheese pasta")
            self.product.price = 210

        def reset(self):
            self.product = Pasta("Cheese pasta")

        def get_product(self):
            return self.product

        def add_ingridients(self):
            self.product.ingridients.append(Cheese())

        def add_catchup(self):
            self.product.catchup = True

        def add_souse(self):
            pass

    class PastaShrimpsCreator(Chef):
        def __init__(self):
            self.product = Pasta("Shrimps pasta")
            self.product.price = 200

        def reset(self):
            self.product = Pasta("Shrimps pasta")

        def get_product(self):
            return self.product

        def add_ingridients(self):
            self.product.ingridients.append(Shrimps())

        def add_souse(self):
            self.product.souse = True

        def add_catchup(self):
            pass

    class Director:

        def make_MushroomPasta(self, chef):
            chef.add_ingridients()
            chef.add_catchup()
            return chef.get_product()

        def make_PastaWithCheese(self, chef):
            chef.add_ingridients()
            chef.add_catchup()
            return chef.get_product()

        def make_PastaShrimps(self, chef):
            chef.add_ingridients()
            chef.add_souse()
            return chef.get_product()

        def make_PastaShrimpsNoSouse(self, chef):
            chef.add_ingridients()
            chef.product.price = 160
            return chef.get_product()

    director = Director()
    greet = "\nВаш заказ готов.\n"
    while True:
        order = input("Какую пасту желаете заказать:\n"
                      "1. Паста с грибами\n"
                      "2. Паста с сыром\n"
                      "3. Паста с креветками\n"
                      "4. Паста с креветками без соуса\n"
                      "q. Выход: ")
        if order == "q":
            print("Good buy!")
            break
        elif order == "1":
            chef = PastaMushroomCreator()
            print(greet, director.make_MushroomPasta(chef))
        elif order == "2":
            chef = PastaWithCheeseCreator()
            print(greet, director.make_PastaWithCheese(chef))
        elif order == "3":
            chef = PastaShrimpsCreator()
            print(greet, director.make_PastaShrimps(chef))
        elif order == "4":
            chef = PastaShrimpsCreator()
            print(greet, director.make_PastaShrimpsNoSouse(chef))


pasta_restaurant()

# ===============================================================================================
print("# Задание 3")
print("# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.")

from abc import ABC, abstractmethod
from copy import deepcopy


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class MyObject(Prototype):
    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2
        self.performed_operation = False

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"{self.__class__} {self.__dict__}"


obj1 = MyObject(100, 50)
obj2 = obj1.clone()
obj3 = obj1.clone()
obj3.field2 = 7
obj4 = obj1.clone()
obj4.field1 = 13

print(obj1, obj2, obj3, obj4, sep="\n")
