""" 
    interperate list as an integer by 
    summing digits in a given base
    return: @param summed list for base b
"""
def sum_digits(d, b):
    s=0
    for i in range(len(d)):
        s += d[i] * b**i

    return s

"""
    add leading zeros to list
    return: @param original list with leading zeros
"""
def insert_leading_zeros(d, k):
    if len(d) < k:
        d.insert(0, 0)
    return d


"""
    separate int into individual digits
    return: @param list of digits
"""
def get_digits(n, b):
    d = []
    while n > 0:
        d.append(n % b)
        n = n // b
    return d


def verify_id(n):
    if len(n) == 0:
        return False
    if int(n) < 0:
        return False
    return True


"""
    algorithm for cycling
    return: @param current value in cycle
"""
def get_cycle(n, b, k):
    n = int(n)

    digits = get_digits(n, b)
    digits = insert_leading_zeros(digits, k)
    
    digits.sort()
    x = sum_digits(digits, b)

    digits.sort(reverse=True)
    y = sum_digits(digits, b)

    # format task num
    z = x - y
    z = str(z)

    if len(z) < k:
        z = z.zfill(k)

    # compare current value to prev
    if str(n) == z:
        return 1
    else:
        n = z

    return z


"""
    main
    return: @param length of repeated cycle
"""
def solution(n, b):
    # make sure id is OK
    if not verify_id(n):
        print('Invalid ID')
        return

    # convert is to integer using base
    k = len(n)
    n = int(n, b)

    # perform algorithm until constant or loop
    # is detected
    full_cycle = []
    while n not in full_cycle:
        full_cycle.append(n)
        n = get_cycle(n, b, k)
        if n == 1:
            return 1

    # perform algorithm backwards - stoppping once
    # it starts to repeat
    looped_cycle = []
    while n not in looped_cycle:
        looped_cycle.append(n)
        n = get_cycle(n, b, k)

    return len(looped_cycle)
    

sol = solution('210022', 3)
print(sol)