"""Creating ListOfNum()a list that accepts integer, float, and complex numbers

2.Create Class ListOfNum()  where you need a list that accepts
numeric data only. Your ListOfNum instance should store onlyinteger,
float, and complex. Otherwise raise an error. So,to achieve this you need
inheritfrom List again and to modifythese methods and demonstratehow we can
use each of themand testwith non-numbers ofvalues
"""

from typing import List

class ListOfNum(List):
    """A class that store only integer, float, and complex numbers inheriting from List class

    Attributes
    ----------
        None
    """

    def __init__(self, other: List) -> None:
        """
        Parameters:
            other (List): A list of integers, float, and complex

        Returns:
            None

        Raise:
            TypeError: In case of parameters contains incompatible types
        """

        for value in other:
            if self.is_numeric(value):
                continue

            raise TypeError("numeric value expected")

        super().__init__(other)

    def __setitem__(self, key: int, value: List) -> None:
        """
        Parameters:
            key (int): Index for new item in the list
            value (List): Value for new item in the list

        Returns:
            None

        Raise:
            TypeError: In case of parameters contains incompatible types
        """

        if self.is_numeric(value):
            super().__setitem__(key, value)
        else:
            raise TypeError("numeric value expected")

    def is_numeric(self, value) -> bool:
        """
        Parameters:
            value (List): A list of integers, float, and complex

        Returns:
            bool: True if value is int, float or complex and false otherwise
        """

        if isinstance(value, int):
            return True

        if isinstance(value, float):
            return True

        if isinstance(value, complex):
            return True

        return False

    def extend(self, other: int) -> None:
        """
        Parameters:
            other (List): A list of integers, float, and complex to extend to list

        Returns:
            None

        Raise:
            TypeError: In case of parameters contains incompatible types
        """

        for value in other:
            if self.is_numeric(value):
                continue

            raise TypeError("numeric value expected")

        super().extend(other)

    def insert(self, index: int, value: List) -> None:
        """
        Parameters:
            index (int): Index to insert in list
            value (List): Value to insert in list

        Returns:
            None

        Raise:
            TypeError: In case of parameters contains incompatible types
        """

        if self.is_numeric(value):
            super().insert(index, value)
        else:
            raise TypeError("numeric value expected")

    def append(self, value: List) -> None:
        """
        Parameters:
            value (List): A value to append a value to list

        Returns:
            None

        Raise:
            TypeError: In case of parameters contains incompatible types
        """

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
