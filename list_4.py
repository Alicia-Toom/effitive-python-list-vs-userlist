"""A ListOfUserString() class that inherit from Userlist

    4. In first question we inherited from List class let’s here inherit
    from UserList a class in collection library, and name is ListOfUserString()
"""

import timeit
from collections import UserList
from list_1 import ListOfString


class ListOfUserString(UserList):
    """A class that represent example of inheriting from List class

    Attributes
    ----------
        None
    """

    def __init__(self, other: UserList) -> None:
        """
        Parameters:
            other (UserList): A list of integers

        Returns:
            None
        """

        super().__init__([str(i) for i in other])

    def append(self, item: UserList) -> None:
        """
        Parameters:
            item (UserList): A list of integers

        Returns:
            None
        """

        self.data.append(str(item))

    def __setitem__(self, index: int, item: str) -> None:
        """
        Parameters:
            index (int): Index to assigning a value value in the list
            item (str): A value to assigning a value to list

        Returns:
            None
        """

        self.data[index] = str(item)

    def extend(self, other: UserList) -> None:
        """
        Parameters:
            other (Userlist): A list of integers

        Returns:
            None
        """

        self.data.extend([str(i) for i in other])

    def insert(self, i: int, item: str) -> None:
        """
        Parameters:
            index (int): Index to insert value in the list
            value (str): A value to insert to list

        Returns:
            None
        """

        self.data.insert(i, str(item))

    def __add__(self, other: UserList) -> UserList:
        """
        Parameters:
            other (List): A list of integers

        Returns:
            UserList
        """

        self_copy = ListOfUserString(self)
        self_copy.extend(other)
        return self_copy

    def __iadd__(self, other: UserList) -> UserList:
        """
        Parameters:
            other (UserList): A list of integers

        Returns:
            UserList
        """

        self.extend(other)
        return self


if __name__ == "__main__":
    # 4(A) let’s create the same methods (a.,b.,c.,d.and e.)from question#1
    # A __init__ initializes all the class’s new instances(constructor)
    data = ListOfUserString([11, 2, 22, 4, 105])
    print(data)
    # B __setitem__() allows user to assign a new value to an existing
    # item using the item’s index, like in a_list[index] = item.
    data[0] = 99
    print(data)
    # C extend () adds a series of items to the end of the list
    data.extend([4, 66, 90, 78])
    print(data)
    # D  insert () allows you to insert a new item at a given position
    # in the underlying list using the item’s index
    data.insert(0, 55)
    print(data)
    # E append () adds a single new item at the end of the underlying list
    data.append(6)
    print(data)
    # F . Modify needed Dunder methods to Add concatenation ‘+’ that add,
    # add in place “+=” and with reflected (swapped) operands (a+b is as b+a).
    #print([100, 200] + data)
    a = ListOfUserString([100, 200])
    b = data
    print(a + b)
    print(b + a)
    a += b
    print(a)

if __name__ == "__main__":
    # 4(B) Let’s use timeit using test_data = range(100_000) with extend() method.
    test_data = range(100_000)

    timer = timeit.Timer(lambda: data.extend(test_data))
    print(f"Timer for UserList: {timer.timeit(number=1)}")

    string_list = ListOfString([])
    timer = timeit.Timer(lambda: string_list.extend(test_data))
    print(f"Timer for List: {timer.timeit(number=1)}")

    # 4(C) Compare the results? and explain why?
    #Checkout README.md
