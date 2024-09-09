def is_prime(n: int) -> bool:
    import math
    if type(n) is not int:
        raise TypeError('must be an integer, but "%s" found' % type(n))
    if n < 2:
        raise ValueError('must be greater than 1, but "%d" found' % n)
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if n % i == 0: return False
    return True
