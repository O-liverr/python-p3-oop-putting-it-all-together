class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            print("Brand must be a string")
            return
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            print("Size must be a positive number")
            return
        self._size = value

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")