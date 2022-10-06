"""TODO"""

from typing import List

class ListOfNum(List):
    """TODO"""

    def __init__(self, other):
        for value in other:
            if self.is_numeric(value):
                continue

            raise TypeError("numeric value expected")

        super().__init__(other)

    def __setitem__(self, key, value):
        if self.is_numeric(value):
            super().__setitem__(key, value)
        else:
            raise TypeError("numeric value expected")

    def is_numeric(self, value):
        """TODO"""
        if isinstance(value, int):
            return True

        if isinstance(value, float):
            return True

        if isinstance(value, complex):
            return True

        return False

    def extend(self, other):
        for value in other:
            if self.is_numeric(value):
                continue

            raise TypeError("numeric value expected")

        super().extend(other)

    def insert(self, index, value):
        if self.is_numeric(value):
            super().insert(index, value)
        else:
            raise TypeError("numeric value expected")

    def append(self, value):
        if self.is_numeric(value):
            super().append(value)
        else:
            raise TypeError("numeric value expected")


if __name__ == "__main__":
    # A __init__ initializes all the class’s new instances(constructor)
    my_numbers = ListOfNum([1.1, 2, 3j])
    print(my_numbers)

    try:
        ListOfNum([1.1, 2, 3j, "4.2"])
    except TypeError as e:
        print(e)

    # B __setitem__() allows user to assign a new value to an existing item using
    # the item’s index, like in a_list[index] = item.
    my_numbers[0] = 35j
    print(my_numbers)
    try:
        my_numbers[0] = "4.2"
    except TypeError as e:
        print(e)

    # C extend () adds a series of items to the end of the other.
    my_numbers.extend([7, 88, 9.9, 78j])
    print(my_numbers)

    # D insert () allows you to insert a new item at a given position in the
    # underlying other using the item’s index
    my_numbers.insert(0, 95)
    print(my_numbers)

    # E append () adds a single new item at the end of the underlying other.
    my_numbers.append(6.6)
    print(my_numbers)
