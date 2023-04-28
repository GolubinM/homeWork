def task1():
    # Двусвязный список
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

    class DoubleLinkedList:
        def __init__(self):
            self.head = None

        def append(self, value):
            new_node = Node(value)

            # Если список пустой, делаем новую ноду головой
            if self.head is None:
                self.head = new_node
                return

            # Если список не пустой, перебираем все ноды, пока не дойдём до последней
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            # Добавляем нашу ноду в next последней, делая её новой последней
            current_node.next = new_node
            new_node.prev = current_node

        def delete(self, value):
            # Если список пустой, ничего не делаем
            if self.head is None:
                return True  # возвращаем True если следующих элементов нет

            # Если то, что мы хотим удалить, это голова, то удаляем её
            if self.head.value == value:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                return True  # возвращаем True если следующих элементов нет

            # Если список не пустой, перебираем все ноды, пока не дойдём до искомого value или до конца списка
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.value == value:
                    current_node.next = current_node.next.next
                    if current_node.next is not None:
                        current_node.next.prev = current_node
                    return
                current_node = current_node.next
            return current_node.next is None  # возвращаем True если следующих элементов нет

        def show(self):
            # Если список пустой, выводим сообщение об этом
            if self.head is None:
                print('List is empty!')
                return
            # Если список не пустой, перебираем и выводим все ноды
            current_node = self.head
            is_head = True
            while current_node is not None:
                if is_head:
                    print(current_node.value, end='')
                    is_head = False
                else:
                    print(f" <-> {current_node.value}", end="")
                current_node = current_node.next
            print()

        def there_is(self, value):
            # Если список пустой, возвращаем False
            if self.head is None:
                return False  # возвращаем False
            # Если список не пустой, перебираем все ноды, пока не дойдём до искомого value или до конца списка
            current_node = self.head
            while current_node is not None:
                if current_node.value == value:
                    return True
                else:
                    current_node = current_node.next
            return False

        def subst(self, value, newvalue):
            # Если список пустой, возвращаем False
            if self.head is None:
                return False  # возвращаем False
            # Если список не пустой, перебираем все ноды, пока не дойдём до искомого value или до конца списка
            current_node = self.head
            while current_node is not None:
                if current_node.value == value:
                    current_node.value = newvalue
                    return True
                else:
                    current_node = current_node.next
            return False

        def get_list(self):
            lst = []  # Если список пустой, выводим пустой список
            if self.head is not None:  # Если список не пустой, перебираем и выводим все ноды в виде списка
                current_node = self.head
                while current_node is not None:
                    lst.append(current_node.value)
                    current_node = current_node.next
            return lst

    # *** ввод начального списка ***
    while True:
        try:
            # input_data = map(int, input("Пользователь вводит с клавиатуры набор чисел разделенных запятой: ").split(","))
            input_data = [1, 4, 5, 2, 6, 2, 8, 9]  # Чтобы не вводить каждый раз. (По заданию строка выше)
            break
        except ValueError:
            print("Ошибка ввода!")

    user_list = DoubleLinkedList()
    for elm in input_data:
        user_list.append(elm)

    # *** окончание ввода начального списка ***

    def input_value(invite: str):
        """ функция ввода числового значения со строкой приглашением invite"""
        try:
            val = int(input(invite))
            return val
        except ValueError as ex:
            print("Ошибка ввода", ex)

    while True:
        sel = input("1. Добавить новое уникальное число в список\n"
                    "2. Удалить все вхождения числа из списка\n"
                    "3. Показать содержимое списка c начала\n"
                    "4. Показать содержимое списка c конца\n"
                    "5. Проверить есть ли значение в списке\n"
                    "6. Заменить первое вхождение значения в списке\n"
                    "7. Заменить все вхождения значения в списке\n"
                    "0. Выход из программы: ")
        if sel == "0":
            print("Good buy!")
            break
        elif sel == "1":
            # Добавить новое уникальное число в список
            new_elm = input_value("введите новое число: ")
            # Проверяем существует ли в списке введенное пользователем число
            if new_elm in user_list.get_list():
                print("Такой элемент уже есть в списке")
            else:
                user_list.append(new_elm)
        elif sel == "2":
            # Удалить все вхождения числа из списка
            new_elm = input_value("введите число для удаления: ")
            count_deleted = 0
            while not user_list.delete(new_elm):
                count_deleted += 1
            print(f"Удалено {count_deleted} элементов списка: ")
        elif sel == "3":
            user_list.show()
        elif sel == "4":
            revers_list = DoubleLinkedList()
            for elm in reversed(user_list.get_list()):
                revers_list.append(elm)
            revers_list.show()
            del revers_list
        elif sel == "5":
            # Проверить есть ли значение в списке
            check_elm = input_value("введите число для проверки: ")
            if user_list.there_is(check_elm):
                print(f"Элемент {check_elm} присутствует в списке: ")
            else:
                print(f"Элемент {check_elm} в списке не присутствует: ")

        elif sel == "6":
            # Заменить первое вхождение значения в списке
            value = input_value("введите вхождение которое нужно заменить: ")
            new_value = input_value("введите значение на которое нужно заменить старое: ")
            if user_list.subst(value, new_value):
                print("Значение заменено: ")
            else:
                print("Значение для замены отсутствует в списке: ")
        elif sel == "7":
            # Заменить все вхождения значения в списке
            value = input_value("введите вхождение которое нужно заменить: ")
            new_value = input_value("введите значение на которое нужно заменить старое: ")
            count_subst = 0
            while user_list.subst(value, new_value):
                count_subst += 1
            print(f"Заменено {count_subst} значений списка: ")


task1()


# **** Задание 2 ***************************************************************
def task2():
    class Stack:
        def __init__(self, size, iterable: list[str] | tuple[str] | set[str] = None):
            self.size = size
            self.lst = [elm for elm in iterable if isinstance(elm, str)][:size] if iterable else []

        def push(self, value):
            if not self.is_full():
                self.lst.append(value)
            else:
                print('Stack is full!')

        def is_full(self):
            return len(self.lst) == self.size

        def is_empty(self):
            if len(self.lst) == 0:
                return True
            return False

        def pop(self):
            return self.is_empty() or self.lst.pop()

        def peek(self):
            return self.is_empty() or self.lst[-1]

        def len(self):
            return len(self.lst)

        def clear(self):
            self.__init__(self.size, [])

        def __str__(self):
            return ' -> '.join(map(str, self.lst))

    user_list = Stack(2)
    while True:
        sel = input("1. помещение строки в стек\n"
                    "2. выталкивание строки из стека\n"
                    "3. подсчет количества строк в стеке\n"
                    "4. проверка пустой ли стек\n"
                    "5. проверка полный ли стек\n"
                    "6. очистка стека\n"
                    "7. получение значения без выталкивания верхней строки из стека\n"
                    "0. Выход из программы: ")
        if sel == "0":
            print("Good buy!")
            break
        elif sel == "1":
            # помещение строки в стек
            user_list.push(input("введите новую строку: "))
            print(user_list.peek())
            print(user_list.len())
        elif sel == "2":
            # выталкивание строки из стека
            user_list.pop()
        elif sel == "3":
            # подсчет количества строк в стеке
            print(user_list.len())
        elif sel == "4":
            # проверка пустой ли стек
            if user_list.is_empty():
                print("Стек пуст")
            else:
                print("Стек не пуст")
        elif sel == "5":
            # проверка полный ли стек
            if user_list.is_full():
                print("Стек заполнен полностью")
            else:
                print("Стек не заполнен полностью")

        elif sel == "6":
            # очистка стека
            user_list.clear()
        elif sel == "7":
            # получение значения без выталкивания верхней строки из стека
            if user_list.peek() is True:
                print("Список пуст")
            else:
                print(user_list.peek())


task2()


# **** Задание 3 ***************************************************************
def task3():
    class Stack:
        def __init__(self, iterable: list[str] | tuple[str] | set[str] = None):
            self.lst = [elm for elm in iterable if isinstance(elm, str)] if iterable else []

        def push(self, value):
            self.lst.append(value)

        def is_empty(self):
            if len(self.lst) == 0:
                return True
            return False

        def pop(self):
            return self.is_empty() or self.lst.pop()

        def peek(self):
            return self.is_empty() or self.lst[-1]

        def len(self):
            return len(self.lst)

        def clear(self):
            self.__init__([])

        def __str__(self):
            return ' -> '.join(self.lst)

    user_list = Stack()
    while True:
        sel = input("1. помещение строки в стек\n"
                    "2. выталкивание строки из стека\n"
                    "3. подсчет количества строк в стеке\n"
                    "4. проверка пустой ли стек\n"
                    "5. очистка стека\n"
                    "6. получение значения без выталкивания верхней строки из стека\n"
                    "0. Выход из программы: ")
        if sel == "0":
            print("Good buy!")
            break
        elif sel == "1":
            # помещение строки в стек
            user_list.push(input("введите новую строку: "))
        elif sel == "2":
            # выталкивание строки из стека
            user_list.pop()
        elif sel == "3":
            # подсчет количества строк в стеке
            print(user_list.len())
        elif sel == "4":
            # проверка пустой ли стек
            if user_list.is_empty():
                print("Стек пуст")
            else:
                print("Стек не пуст")
        elif sel == "5":
            # очистка стека
            user_list.clear()
        elif sel == "6":
            # получение значения без выталкивания верхней строки из стека
            if user_list.peek() is True:
                print("Стек пуст")
            else:
                print(user_list.peek())


task3()
