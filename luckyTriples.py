

"""
    Count the unique lucky triples for a given list.
    Iterate forward counting the num of divisors
    up to that iteration.
"""
def count_lucky_triples(l):
    lucky_triples = 0
    counts = {i: 0 for i in range(len(l))}

    for i in range(1, len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                counts[i] += 1
                lucky_triples += counts[j]
    return lucky_triples


"""
    Main
"""
def solution(l):

    # list is sorted integers
    if l[0] < 1:
        print('Division by zero not allowed!')
        return

    return count_lucky_triples(l)


x = [1,2,3,4,5,6]
y = [1,1,1]

z = []
for i in range(1,2000):
    z.append(i)

sol = solution(z)
print(sol)
