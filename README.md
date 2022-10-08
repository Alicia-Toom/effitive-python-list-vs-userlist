# List vs UserList

The purpose of this repository is do a comparison assignment for the course effective python course for Teknikhögskolan in Gothenburg. We will be comparing between List and Userlist where will discuss and compare the results between the two in the end. 

## Instructions

Create your own Lists: At many moments in yourmPython coding trip, you may need to create your own list of a data type with modified behavior, new functionalities, or both.In this project we are going to user python built-in data type list and other from collection library to create our own data types. Please answer all these questions, 25 points per each! 

1. Create a class ListOfString() where you need a list to be automatically stores all its items as stringsand inherit from List class. Your class converts all the input values into strings on the fly, so to achievethis you need to modifythese methods and demonstratehow we can use each of them. 

a.__init__ initializes all the class’s new instances(constructor).
b.__setitem__() allows userto assign a new value to an existing item using the item’s index, like in a_list[index] = item.
c.extend () adds a series of items to the end of the list.
d.insert () allows youto insert a new item at a given position in the underlying list using the item’s index.
e.append () adds a single new item at the end of the underlying list.
f.Modify needed Dunder methods to Add concatenation ‘+’ that add, add in place “+=” and with reflected (swapped) operands (a+b is as b+a).

2. Create Class ListOfNum()  where you need a list that accepts numeric data only. Your ListOfNum instance should store onlyinteger, float, and complex. Otherwise raise an error. So,to achieve this you need inheritfrom List again and to modifythese methods and demonstratehow we can use each of themand testwith non-numbers ofvalue.

a.__init__ initializes all the class’s new instances(constructor).
b.__setitem__() allows userto assign a new value to an existing item using the item’s index, like in a_list[index] = item.
c.extend () adds a series of items to the end of the list.
d.insert () allows youto insert a new item at a given position in the underlying list using the item’s index.
e.append () adds a single new item at the end of the underlying list.

3. Now let’s upgrade built in List datatype with new datatype called <your_name>List() example:  AmmarList(). This datatype inherits from List datatype and add extra methods.Writeyour own classand demonstrate the new addedmethodswith best performanceto built-in datatype as next methods:

a..join_it() concatenates all the list’s items in a single string.
b..map_it(action) yields new items that result from applying an action() callable to each item in the underlying list.
c..filter_it(predicate) yields all the items that return True when calling predicate() on them.
d..for_each_item(func) calls func() on every item in the underlying list to generate results!

4. In first question we inherited from List class let’s here inherit fromUserList aclass in collection library,andnameis ListOfUserString()

a.let’s create the same methods (a.,b.,c.,d.and e.)from question#1
b.Let’s use timeit using test_data= range(100_000)with extend()method.
c.Compare the results? and explain why?

# Projects layout

To answer each question, the file name is list_numbers.py respectively. 

## Compare the results? and explain why?

Using time it to compare the run time for List VS UserList are as followed: 

```
Timer for UserList: 0.039800100000000005
Timer for List: 0.02877669999999999
```

UserList is a little bit slower and the reason could be
that collections List is optimised for speed rather than being subclass friendly.

One takeaway from this when deciding which superclass is best for your specific use case, make sure to run a performance test.