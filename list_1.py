"""1.Create a class ListOfString() where you need a list to be automatically
    stores all its items as stringsand inherit from List class. Your class converts
    all the input values into strings on the fly, so to achievethis you need to
    modifythese methods and demonstratehow we can use each of themas example here:
"""

from typing import List

class ListOfString(List):
    """TODO"""

    def __init__(self, other):
        super().__init__([str(i) for i in other])

    def append(self, value):
        super().append(str(value))

    def __setitem__(self, key, value):
        super().__setitem__(key, str(value))

    def extend(self, other):
        super().extend([str(i) for i in other])

    def insert(self, index, value):
        super().insert(index, str(value))

    def __add__(self, other):
        self_copy = ListOfString(self)
        self_copy.extend(other)
        return self_copy

    def __iadd__(self, other):
        self.extend(other)
        return self


if __name__ == "__main__":
    # A __init__ initializes all the class’s new instances(constructor)
    data = ListOfString([11, 2, 22, 4, 105])
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
    a = ListOfString([100, 200])
    b = data
    print(a + b)
    print(b + a)
    a += b
    print(a)
