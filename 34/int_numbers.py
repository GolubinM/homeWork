class Int_numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_numbers(self):
        return self.numbers

    def summ_numb(self):
        return sum(self.numbers)

    def average_numbers(self):
        return round(sum(self.numbers) / len(self.numbers), 0)

    def max_numb(self):
        return max(self.numbers)

    def min_numb(self):
        return min(self.numbers)
