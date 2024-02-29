def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0: return 1
    product = 1
    for _ in range(k):
        product = n * product
        n -= 1
    return product

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0
    for i in range(1, y):
        dec_place = 10**i
        if dec_place > y*10:
            break
        rem = y % dec_place
        digit = rem*10 // dec_place
        sum += digit
    return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    is_double_eights = 0b00
    while n > 0 and is_double_eights != 0b10:
        rem = n % 10
        if rem == 8:
            is_double_eights += 0b1
        else:
            is_double_eights = 0b00
        n = n // 10
    return True if is_double_eights == 0b10 else False
