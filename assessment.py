"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    # initialize empty list for storing odd_numbers
    odd_numbers = []

    # # non-list comprehension approach:
    # for item in numbers:
    #     if item % 2 == 1:
    #         odd_numbers.append(item)

    # if list item is odd, modulus value will be 1; adds the list item
    # to odd_numbers while iterating over the input list 'numbers' if
    # '% 2 == 1' evaluates as true
    odd_numbers = [item for item in numbers if item % 2 == 1]

    return odd_numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    # enumerate function take an iterator as its argument
    # syntax for enumerate() allows for i, item to return as
    # index, listitem[index] for a given list
    for i, item in enumerate(items):
        print i, item


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    # convert the two input lists into sets, and create a new set
    # common_foods as their mathematical intersection
    common_foods = set(foods1) & set(foods2)

    # convert common_foods to a list and sort it
    common_foods = list(common_foods)
    common_foods.sort()

    return common_foods


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    # items[::2] will return the whole set, from start to finish, with a
    # step of 2, meaning every other item is returned
    return items[::2]


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    # fail fast: n=0 means the largest 0 integers are queried,
    # which is an empty list
    if n == 0:
        return []
    else:
        # sort the input list; default is from smallest to largest
        items.sort()
        # create new list of n items: [-n:] means the list will be read
        # from left to right (smallest to largest) but will start n positions
        # from the end, meaning only the largest n items are returned
        largest_n_items = items[-n:]

        return largest_n_items


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
