from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b > 0:
        op = add
    else:
        op = sub
    return op(a, b)

def two_of_three(a, b, c):
    """Return x**2 + y**2, where x and y are the two largest of a, b, c."""
    return max(a, b, c) ** 2 + (a + b + c - max(a, b, c) - min(a, b, c)) ** 2

def hailstone(n):
    """Print the hailstone sequence starting at n, returning its length."""
    def iseven(n):
        if n % 2 == 0:
            return True
        else:
            return False

    print(n)
    length = 1
    while n != 1:
        if iseven(n):
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        length += 1
    return length
