""" A class of your own name: AiciaList() using built-in datatype

3.Now let’s upgrade built in List datatype with new datatype
called <your_name>List() example:  AmmarList(). This datatype
inherits from List datatype and add extra methods. Writeyour own
classand demonstrate the new addedmethodswith best performanceto
built-in datatype as next methods
"""

from typing import List

class AliciaList(List):
    """A class inheriting from List class using built-in datatype

    Attributes
    ----------
        None
    """

    def join_it(self):
        """
        Parameters:
            None

        Returns:
            None
        """
        return " ".join([str(value) for value in self])

    def map_t(self, action: List) -> None:
        """
        Parameters:
            action (List): A list of integers

        Returns:
            None
        """
        return [action(str(value)) for value in self]

    def filter_it(self, predicate: List) -> None:
        """
        Parameters:
            predicate (List): A list of integers

        Returns:
            None
        """
        return [value for value in self if predicate(str(value))]

    def for_each_item(self, func: List) -> None:
        """
        Parameters:
            func (List): A list of integers

        Yield:
            None
        """
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
