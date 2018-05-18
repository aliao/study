"""Submission for CS 61A Homework 4.

Name:
Login:
Collaborators:
"""

# Q1.

# [This problem, as promised, held over from last week.]
# Submit a copy of your hw3.py solution with this hw4.py file.

from hw3 import *

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

#def sum_nonzero_with_for(seq):
    #"""Returns an interval that is the sum of the squares of the non-zero
    #intervals in seq, using a for statement.
    #
    #>>> str_interval(sum_nonzero_with_for(seq))
    #'0.25 to 2.25'
    #"""
    #"*** YOUR CODE HERE ***"

#from functools import reduce
##def sum_nonzero_with_map_filter_reduce(seq):
    #"""Returns an interval that is the sum of the squares of the non-zero
    #intervals in seq, using using map, filter, and reduce.
    #
    #>>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    #'0.25 to 2.25'
    #"""
    #"*** YOUR CODE HERE ***"
#
##def sum_nonzero_with_generator_reduce(seq):
    #"""Returns an interval that is the sum of the squares of the non-zero
    #intervals in seq, using using reducpython str reversee and a generator expression.
    #
    #>>> str_interval(sum_nonzero_with_generator_reduce(seq))
    #'0.25 to 2.25'
    #"""
    #"*** YOUR CODE HERE ***"


# Definitions from lecture.

empty_rlist = None

def make_rlist(first, rest = empty_rlist):
    """A recursive list, r, such that first(r) is 'first' and 
    rest(r) is 'rest,'  which must be an rlist."""
    return first, rest

def first(r):
    """The first item in r."""
    return r[0]

def rest(r):
    """The tail of r."""
    return r[1]

def extend_rlist(left, right):
    """The sequence of items of rlist 'left' followed
    by the items of 'right'."""
    if left == empty_rlist:
         return right
    else:
         return make_rlist(first(left), 
                           extend_rlist(rest(left), right))
    
# Q2.

def is_tuple(x):
    return type(x) is tuple

def to_rlist(items):
    """The sequence of values in 'items', converted into a corresponding
    rlist.  Any tuples among the items also become rlists.
    >>> to_rlist((1, (0, 2), (), 3))
    (1, ((0, (2, None)), (None, (3, None))))
    """
    if not items:
        return empty_rlist
    else:
        if is_tuple(items[0]):
            return make_rlist(to_rlist(items[0]), to_rlist(items[1:]))
        else:
            return make_rlist(items[0], to_rlist(items[1:]))


# Q3.

def could_be_rlist(x):
    """Return true iff x might represent an rlist."""
    return x is None or type(x) is tuple

def to_tuple(L):
    """Assuming L is an rlist, returns a tuple containing the same
    sequence of values.
    >>> x = to_rlist((1, (0, 2), (), 3))
    >>> to_tuple(x)
    (1, (0, 2), (), 3)
    """
    def to_tuple_aux(r, t):
        if r == empty_rlist:
            return t
        else:
            if could_be_rlist(first(r)):
                return to_tuple_aux(rest(r), t + (to_tuple_aux(first(r), ()), ))
            else:
                return to_tuple_aux(rest(r), t + ((first(r), )))
    return to_tuple_aux(L, ())

# Q4.

def inserted_into_all(item, list_list):
    """Assuming that 'list_list' is an rlist of rlists, return the
    rlist consisting of the rlists in 'list_list', but with 
    'item' prepended as the first item in each.
    >>> L0 = to_rlist(((), (1, 2), (3,)))
    >>> L1 = inserted_into_all(0, L0)
    >>> to_tuple(L1)
    ((0,), (0, 1, 2), (0, 3))
    """
    if list_list == empty_rlist:
        return empty_rlist
    else:
        new_first = make_rlist(item, first(list_list))
        return make_rlist(new_first, inserted_into_all(item, rest(list_list)))

def subseqs(S):
    """Assuming that S is an rlist, return an rlist of all subsequences
    of S (an rlist of rlists).  The order in which the subsequences
    appear is unspecified.  
    >>> seqs = subseqs(to_rlist((1, 2, 3)))
    >>> show = list(to_tuple(seqs))   # Can only sort lists, not tuples
    >>> show.sort()
    >>> show
    [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    if S == empty_rlist:
        return make_rlist(empty_rlist, empty_rlist)
    else:
        f, r = first(S), rest(S)
        s_r = subseqs(r)
        return extend_rlist(inserted_into_all(f, s_r), s_r)

# Q5.

def inserted_into_all_tuples(item, tuple_tuple):
    """Assuming that 'tuple_tuple' is a tuple of tuples, return the
    tuple consisting of the tuples in 'tuple_tuple', but with 
    'item' prepended as the first item in each.
    >>> inserted_into_all_tuples(0, ((), (1, 2), (3, )))
    ((0,), (0, 1, 2), (0, 3))
    """
    result = ()
    for t in tuple_tuple:
       result = result + (((item,) + t), )
    return result

def subseqs_tuples(S):
    """Assuming that S is a tuple, return tuple of all subsequences
    of S (a tuple of tuples).  The order in which the subsequences
    appear is unspecified.  
    >>> seqs = subseqs_tuples((1, 2, 3))
    >>> show = list(seqs)
    >>> show.sort()
    >>> show
    [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    if not S:
        return ((),)
    else:
        f, r = S[0], S[1:]
        s_r = subseqs_tuples(r)
        return inserted_into_all_tuples(f, s_r) + s_r

# Q6.

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("acme", "madam", "pivot", "pip"))
    2
    """
    return len(tuple((filter(lambda string: string == string[::-1], L))))

# Q7.

def alt_filter(pred, L):
    """The tuple containing all elements, x, of L such that pred(x).
    >>> alt_filter(lambda x: x%2 == 0, (0, 1, 3, 8, 4, 12, 13))
    (0, 8, 4, 12)
    """
    return reduce(lambda a_tuple, i: a_tuple + (i,) if pred(i) else a_tuple, L, ())

# Q8.

def capitalize_sentences(S):
    """The sequence of words (strings) S, with all initial words in 
    sentences capitalized, and all others unchanged.  A word begins a 
    sentence if it is either the first word in S, or the preceding word 
    in S ends in a period.
    >>> capitalize_sentences(("see", "spot", "run.", "run", "spot", "run."))
    ('See', 'spot', 'run.', 'Run', 'spot', 'run.')
    """
    return tuple(map(lambda w1, w2: w1.capitalize() if w2.endswith('.') else w1, S, ('.',) + S))


        
# Q9.

def repeat(f, x, n):
     """Apply f to x n times.  When n is 0, the result is x; when n is
     1, the result is f(x); when n is 2, f(f(x)), etc.
     >>> repeat(lambda x: x+1, 1, 5)
     6
     """
     fx = lambda x, f: f(x)
     n_fs = (f for _ in range(n))
     return reduce(fx, n_fs, x)



# Q10.  Extra for experts.

def sortit(S):
    """The sequence of strings S sorted into lexicographic order 
    (the < operator).
    >>> sortit(("The", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
    ...         "dog."))
    ('The', 'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the')
    """
    max_of_two_string = lambda s1, s2: s1 if s1 >= s2 else s2
    max_of_strings = lambda S: reduce(max_of_two_string, S)
    def f(two_strings):
        if not two_strings[0]:
            return (two_strings[1],)
        elif len(two_strings) == 1:
            return two_strings
        else:
            S, S1_sorted = two_strings[0], two_strings[1]
            m = max_of_strings(S)
            is_not_equal = lambda s: s != m
            S_new = tuple(filter(is_not_equal, S))
            S1_sorted_new = ((m,) * S.count(m)) + S1_sorted
            return S_new, S1_sorted_new
    return repeat(f, (S, ()), len(S) + 2)[0]

