class NumTest:

    def __init__(self):
        self.__value = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def to_oct(self):
        return str(oct(self.__value))

    def to_hex(self):
        return str(hex(self.__value))

    def to_bin(self):
        return str(bin(self.__value))

    def save_num_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.__value))

    def load_num_from_file(self, filename):
        with open(filename, "r") as f:
            self.__value = int(f.readline())
            return self.__value
