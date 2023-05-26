from abc import ABC, abstractmethod
from datetime import datetime
import csv


class PizzaBase(ABC):
    @abstractmethod
    def cost_factor(self):
        pass

    @abstractmethod
    def cost_base(self):
        pass


class PizzaBase25cm(PizzaBase):
    @property
    def cost_factor(self):
        return 1

    @property
    def cost_base(self):
        return 100

    def __str__(self):
        return f'Основа для пиццы 25 см'


class PizzaBase30cm(PizzaBase):
    @property
    def cost_factor(self):
        return 1.44

    @property
    def cost_base(self):
        return 115

    def __str__(self):
        return f'Основа для пиццы 30 см'


class Topping:
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def __str__(self):
        return self.name


class Toppings:
    data = {'Cheese': 15, 'Tomatoes': 15, 'Pepperoni': 20,
            'Bacon': 25, 'Mushrooms': 20, 'Olives': 25,
            'Chicken': 20, 'Pineapple': 20}

    toppings = {}

    @staticmethod
    def init_toppings():
        for key, value in Toppings.data.items():
            Toppings.toppings[key] = (type(key, (Topping,), {'cost_factor': value}))


class Pizza:
    def __init__(self, base, *toppings):
        self.base = base
        self.toppings = toppings

    @property
    def cost(self):
        return sum((top.cost_factor for top in self.toppings)) * self.base.cost_factor + self.base.cost_base

    def __str__(self):
        return f"Pizza: {self.base}; Топинги: {', '.join(map(str, [tp.__name__ for tp in self.toppings]))}; Цена: {self.cost}"


class PizzaTemplates:
    @staticmethod
    def Margarita(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Tomatoes'])

    @staticmethod
    def Pepperoni(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Pepperoni'])

    @staticmethod
    def BaconAndMushrooms(base=PizzaBase25cm()):
        return Pizza(base,
                     Toppings.toppings['Cheese'],
                     Toppings.toppings['Bacon'],
                     Toppings.toppings['Mushrooms'],
                     Toppings.toppings['Tomatoes'])


class PayForAll:
    def __init__(self):
        self.acquiring = 0
        self.card_pay = CardPay
        self.cash_pay = CashPay

    def make_pay(self):
        while True:
            query = input("Выберете способ оплаты:\n1. Оплата картой\n2. Оплата наличными\n0. Отмена оплаты: \n")
            if query == "0":
                return False
            elif query == "1":
                return self.card_pay().get_money()
            elif query == "2":
                return self.cash_pay().get_money()


class CardPay:
    def __init__(self):
        self.acquiring = 0.02  # комиссия за эквайринг

    def get_money(self):
        pay_factor = 1 - self.acquiring
        return pay_factor


class CashPay:
    def __init__(self):
        self.acquiring = 0  # комиссия за эквайринг

    def get_money(self):
        pay_factor = 1 - self.acquiring
        return pay_factor


class Pizzeria:
    def __init__(self):
        self.sold_pizzas = 0
        self.deal = 0
        self.revenue = 0
        self.profit = 0
        self.pay_service = PayForAll
        Toppings.init_toppings()

    def run(self):
        query = None
        self.clear_basket()
        while query != 'Exit':
            query = input('Введите команду:\n'
                          '1. Добавить пиццу в корзину\n'
                          '2. Удалить пиццу из корзины\n'
                          '3. Просмотреть ваш заказ\n'
                          '4. Очистить корзину\n'
                          '5. Оплатить товары в корзине\n'
                          '6. Посмотреть статистику продаж\n'
                          'Exit - выйти из программы:\n')
            if query == '1':
                self.add_pizza()
            elif query == '2':
                self.remove_pizza()
            elif query == '3':
                print(self.show_order())
            elif query == '4':
                self.clear_basket()
                print("Корзина очищена.")
            elif query == '5':
                if self.basket:
                    self.pay_order()
                else:
                    print("Корзина пуста. Выберете пиццу до оплаты, пожалуйста.")
            elif query == '6':
                self.out_statistics()

    def pay_order(self):
        pay_result = self.pay_service().make_pay()
        if pay_result:
            current_revenue = 0
            for one_pizza in self.basket:
                self.sold_pizzas += 1
                current_revenue += round(one_pizza.cost * pay_result,
                                         2)  # расчет выручки с учетом комиссии за эквайринг
                self.profit += round(one_pizza.base.cost_base * pay_result, 2)
            self.revenue += current_revenue
            self.deal += 1
            print("Ваш заказ:\n")
            print(f"Оплата в размере {round(current_revenue / pay_result, 2)} успешна произведена!")
            self.create_log()
        self.basket = []

    def clear_basket(self):
        self.basket = []

    def out_statistics(self):
        msg = f'СТАТИСТКА ПРОДАЖ:\n\tПродаж: {self.deal}\n\tПродано пицц всего шт.: {self.sold_pizzas}'
        msg += f"\n\tВыручка: {self.revenue}\n\tПрибыль: {self.profit}"
        print(msg)

    def show_order(self):
        if self.basket:
            total_price = "\n" + "-" * 70 + f"\nСумма заказа: {round(sum([pz.cost for pz in self.basket]), 2)}" \
                          + "\n" + "-" * 70
            msg = "В корзине:\n" + "-" * 70 + "\n" + "\n".join(
                map(str, [f'{i}). {item}' for i, item in enumerate(self.basket, 1)])) + total_price
            return msg
        else:
            return "Корзина пуста."

    def create_log(self):
        my_data_list = [datetime.today().strftime('%Y-%m-%d %H:%M:%S')]
        my_data_list.extend(list(map(str, [item for item in self.basket])))
        with open('report_log.csv', 'a', encoding="utf8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(my_data_list)

    def remove_pizza(self):
        if self.basket:
            print(self.show_order())
            to_del = int(input("Выберете какую пиццу удалить из корзины: \n"))
            if to_del and to_del in range(len(self.basket) + 1):
                removed_pizza = self.basket.pop(to_del - 1)
                print(f'Удалена из корзины: {removed_pizza}')
            else:
                print('Корзина пуста.')

    def add_pizza(self):
        query = input('Выберите опцию:\n'
                      '1. Выбрать одну из готовых пицц\n'
                      '2. Собрать пиццу самому!\n')
        if query == '1':
            base = 'Введите номер пиццы, которую вы бы хотели заказать:\n'
            templates = list(PizzaTemplates.__dict__.items())
            for i, pizza in enumerate(templates):
                if isinstance(pizza[1], staticmethod):
                    base += f'{i}. {pizza[0]} - {", ".join(map(str, [top.__name__ for top in pizza[1]().toppings]))}\n'
            choice = int(input(base))
            pizza_maker = templates[choice][1]
            size = int(input('Введите размер пиццы(25 / 30): '))
            if size == 25:
                pizza = pizza_maker(PizzaBase25cm())
            else:
                pizza = pizza_maker(PizzaBase30cm())
        else:
            print('Собираем самостоятельно')
            size = int(input('Введите размер пиццы(25 / 30): '))
            my_toppings = []
            while True:
                # Подготовить список топингов, выбирать топинги в набор(корзину) пока не будет введен Enter
                # После завершения выбора  топингов выход в меню
                for i, topping in enumerate(Toppings.toppings, 1):
                    print(i, topping)
                query = input('Выберете номер топпинга для пиццы,\n Enter - продолжить: ')
                if query == "":
                    break
                elif query in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    my_toppings.append(list(Toppings.toppings)[int(query) - 1])
            topps = [Toppings.toppings[top] for top in my_toppings]
            if size == 25:
                pizza = Pizza(PizzaBase25cm(), *topps)
            else:
                pizza = Pizza(PizzaBase30cm(), *topps)
        self.basket.append(pizza)


def main():
    app = Pizzeria()
    app.run()


if __name__ == '__main__':
    main()
