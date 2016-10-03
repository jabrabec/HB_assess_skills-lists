"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    ## lines 43-47 use a for loop; this approach works,
    ## but was replaced with list comprehension

    # words_over_four = []

    # for word in words:
    #     if len(word) > 4:
    #         words_over_four.append(word)

    words_over_four = [word for word in words if len(word) > 4]

    return words_over_four


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    # words_of_len_n = []

    # for word in words:
    #     if len(word) > n:
    #         words_of_len_n.append(word)

    ## replace the above steps with list comprehension
    words_of_len_n = [word for word in words if len(word) > n]

    return words_of_len_n


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    # fail fast
    if not numbers:
        return None
    else:
        # first input element is set to var 'smallest'
        smallest = numbers[0]
        # iterate over all numbers in input list
        for integer in numbers:
                # if the currently-read element is less than 'smallest'
                # reset smallest = to current element
                if integer < smallest:
                    smallest = integer
        return smallest


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    # fail fast
    if not numbers:
        return None
    else:
        # first input element is set to var 'largest'
        largest = numbers[0]
        # iterate over all numbers in input list
        for integer in numbers:
                # if the currently-read element is grearter than 'largest'
                # reset largest = to current element
                if integer > largest:
                    largest = integer
        return largest


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    # initialize empty list
    half_list = []

    # iterate over all input elements
    for number in numbers:
        # calculate half the input value and add it to half_list
        half_list.append(float(number) / 2)

    return half_list


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    # initialize empty list
    length_list = []

    # iterate over all input elements
    for word in words:
        # calculate input element length and add it to length_list
        length_list.append(len(word))

    return length_list


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    # initialize sum_of_all variable; also allows function to
    # return 0 if empty list is given as function argument
    sum_of_all = 0

    # iterate over all input elements
    for number in numbers:
        # increase sum_of_all by the list element with each iteration
        sum_of_all += number

    return sum_of_all


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    # fail fast; return 1 for empty product
    if not numbers:
        return 1
    else:
        # intialize prod_of_all variable with value of 1
        # because math (value of 1 doesn't impact output,
        # value of 0 will never work)
        prod_of_all = 1

        # iterate over all input elements
        for number in numbers:
            # multiply sum_of_all by the list element with each iteration
            prod_of_all *= number

        return prod_of_all


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    # initialize empty string
    all_strings = ""

    # iterate over all input elements
    for word in words:
        # add the list element to all_strings with each iteration
        all_strings = all_strings + word

    return all_strings


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    # initialize count & total_sum variables as floats = 0
    # since these are floats, the final average returned will also be
    count = float(0)
    total_sum = float(0)

    # fail fast
    if not numbers:
        return None
    else:
        # iterate over all input elements
        for number in numbers:
            # keep track of number of items in list with count
            count += 1
            # calculate the sum of values in the list
            total_sum += number
            # calculate mathmatical average
            average = total_sum / count
        return average


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    return ", ".join(words)


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    # initialize new reversed_list in order to not change original list
    # reversed list is equated to items[] with step -1, which means input list
    # is read backwards
    reversed_list = items[::-1]

    return reversed_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    listself.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    # items[:] specifies the original input is modified in place
    # step -1 reads the items from last to first (i.e. reversed)
    items[:] = items[::-1]


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    # initialize empty sets for tracking items as they're read from input
    # list_of_dupes will be returned as a list at the end of the function, but
    # starts as a set in order to not get duplicate-duplicates
    list_of_dupes = set()
    seen_items = set()

    # iterate over all input elements
    for item in items:
        # if item is new, it goes in the 'seen_items' list
        #  because it has now been observed at least once
        if item not in seen_items:
            seen_items.add(item)
        # items that ARE in seen_items already (implied condition:
        # if item in seen_items) are added to set of duplicates
        else:
            list_of_dupes.add(item)

    # convert list_of_dupes from a set to a list and sort it
    list_of_dupes = list(list_of_dupes)
    list_of_dupes.sort()

    return list_of_dupes


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    # initialize empty list for tracking indices
    index_list = []

    # iterate over all input elements
    for word in words:
        # start index counter outside the while loop
        word_index = 0
        # start a while loop that will iterate over the word until whole
        # individual word is processed
        while word_index < len(word):
            # add the index counter to index_list if word[index] matches
            # 'letter' and break the loop so no further letters are read
            if word[word_index] == letter:
                index_list.append(word_index)
                break
            # increment word_index with every repeat of the while loop until
            # the letter is found or the whole word is read
            word_index += 1
        # if the letter is never found, add None to list for that word in
        # input 'words' list
        if word_index == len(word):
            index_list.append(None)

    return index_list

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
