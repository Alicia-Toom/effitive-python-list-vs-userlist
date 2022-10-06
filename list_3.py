"""TODO"""

from typing import List

class AliciaList(List):
    """TODO"""

    def join_it(self):
        """TODO"""
        return " ".join([str(value) for value in self])

    def map_t(self, action):
        """TODO"""
        return [action(str(value)) for value in self]

    def filter_it(self, predicate):
        """TODO"""
        return [value for value in self if predicate(str(value))]

    def for_each_item(self, func):
        """TODO"""
        for value in self:
            yield func(str(value))


if __name__ == "__main__":
    # A .join_it() concatenates all the list’s items in a single string.
    stmt = AliciaList(["Welcome", 2, "Python", ",", "Welcome", "to", "Göt"])
    print(stmt.join_it())

    # B .map_it(action) yields new items that result from applying an action()
    # callable to each item in the underlying list.
    print(stmt.map_t(str.upper))

    # C.filter_it(predicate) yields all the items that return True when calling predicate() on
    print(stmt.filter_it(lambda item: item.startswith("P")))

    # D for_each_item(func) calls func() on every item in the underlying list
    # to generate results!
    print(list(stmt.for_each_item(lambda item: item.lower())))
