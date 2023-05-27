import unittest
from int_numbers import Int_numbers
from num_tst import NumTest


class TestIntNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.int_nums = Int_numbers([100, 50, 25, 10, 5])

    def test_sum(self):
        self.assertEqual(190, self.int_nums.summ_numb(),
                         f"Результат с аргументами [100, 50, 25, 10, 5] должен равняться 190!")

    def test_avr(self):
        self.assertEqual(38.0, self.int_nums.average_numbers(),
                         f"Результата с аргументами [100, 50, 25, 10, 5] должен равняться 38.0!")

    def test_max(self):
        self.assertEqual(100, self.int_nums.max_numb(),
                         f"Результата с аргументами [100, 50, 25, 10, 5] должен равняться 100!")

    def test_min(self):
        self.assertEqual(5, self.int_nums.min_numb(),
                         f"Результата с аргументами [100, 50, 25, 10, 5] должен равняться 5!")


class FalseTestIntNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.int_nums = Int_numbers([100, 50, 25, 10, 5])

    def test_sum(self):
        self.assertEqual(191, self.int_nums.summ_numb(),
                         f"Результат с аргументами [100, 50, 25, 10, 5] должен равняться 190!")

    def test_avr(self):
        self.assertEqual(31.0, self.int_nums.average_numbers(),
                         f"Результат с аргументами [100, 50, 25, 10, 5] должен равняться 38.0!")

    def test_max(self):
        self.assertEqual(101, self.int_nums.max_numb(),
                         f"Результат с аргументами [100, 50, 25, 10, 5] должен равняться 100!")

    def test_min(self):
        self.assertEqual(51, self.int_nums.min_numb(),
                         f"Результат с аргументами [100, 50, 25, 10, 5] должен равняться 5!")


class TestNumTest(unittest.TestCase):
    def setUp(self) -> None:
        self.num_test = NumTest()
        self.num_test.set_value(5)

    def test_get_value(self):
        self.assertEqual(5, self.num_test.get_value(),
                         f"Результат должен равняться 5!")

    def test_set_value(self):
        self.num_test.set_value(10)
        self.assertEqual(10, self.num_test.get_value(),
                         f"Результат должен равняться 10!")

    def test_to_oct(self):
        arg = 20
        self.num_test.set_value(arg)
        self.assertEqual('0o24', self.num_test.to_oct(),
                         f"Результат с аргументом 10 должен равняться 0o12!")

    def test_to_hex(self):
        arg = 15
        self.num_test.set_value(arg)
        self.assertEqual('0xf', self.num_test.to_hex(),
                         f"Результат с аргументом 15 должен равняться 0xf!")

    def test_to_bin(self):
        arg = -1
        self.num_test.set_value(arg)
        self.assertEqual('-0b1', self.num_test.to_bin(),
                         f"Результата с аргументами -1 должен равняться -0b1!")

    def test_load_save_num(self):
        arg = 101014
        self.num_test.set_value(arg)
        self.num_test.save_num_to_file('num1.txt')
        self.num_test.set_value(101)  # меняем значение __value для проверки загрузки значения arg
        self.assertEqual(101014, self.num_test.load_num_from_file('num1.txt'),
                         f"Результата с аргументами 101014 должен равняться 101014!")


if __name__ == '__main__':
    unittest.main()
