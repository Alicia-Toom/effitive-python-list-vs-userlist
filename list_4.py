"""4. In first question we inherited from List class let’s here inherit
    from UserList a class in collection library, and name is ListOfUserString()
"""

import timeit
from collections import UserList
from list_1 import ListOfString


class ListOfUserString(UserList):
    """TODO"""
    def __init__(self, other):
        super().__init__([str(i) for i in other])

    def append(self, item):
        self.data.append(str(item))

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def extend(self, other):
        self.data.extend([str(i) for i in other])

    def insert(self, i, item):
        self.data.insert(i, str(item))

    def __add__(self, other):
        self_copy = ListOfUserString(self)
        self_copy.extend(other)
        return self_copy

    def __iadd__(self, other):
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

    # 4(B) Let’s use timeit using test_data = range(100_000) with extend() method.
    test_data = range(100_000)

    timer = timeit.Timer(lambda: data.extend(test_data))
    print(f"Timer for UserList: {timer.timeit(number=1)}")

    string_list = ListOfString([])
    timer = timeit.Timer(lambda: string_list.extend(test_data))
    print(f"Timer for List: {timer.timeit(number=1)}")

    # 4(C) Compare the results? and explain why?
    #Timer for UserList: 0.039800100000000005
    #Timer for List: 0.02877669999999999
    #
    # UserList is a little bit slower and the reason could be
    # that UserList is with the Python standard library while List is wriiten in C
    # and potimized for performance.
    #
    # One takeaway from this when deciding which superclass is best for your specific use case,
    # make sure to run a performance test.
    #
    #
    # For more information to read further and
    # for references: https://realpython.com/inherit-python-list/
