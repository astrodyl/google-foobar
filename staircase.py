

"""
    Count partitions in which no number occurs more 
    than once. I.e., partition with distinct parts or
    Glaisher's theorem.

    I implement the generating function as defined
    on https://mathworld.wolfram.com/PartitionFunctionQ.html
    and use the coefficient of the nth power to determine
    the number of partitions.

    A reccurence relation could be used, though is very slow
    .. as I found out the hard way. ~few minutes for n=200
"""


def determine_coeff(c, p, k):
    if p < k:
        return c[p]
    else:
        print(p, k, c)
        return c[p] + c[p - k]


"""
    Implement generating function for the 
    partition function Q only keeping powers
    up to n
"""
def solution(n):

    coefficients = [0] * (n + 1)
    coefficients[0] = 1 # otherwise always = 0
    print(0,0,coefficients)

    for k in range(1, n):
        temp_coeff = []
        for p in range(n + 1):
            temp_coeff.append(determine_coeff(coefficients, p, k))
        #print(p, k, temp_coeff)
        coefficients = temp_coeff

    return coefficients[n]

print(solution(4))