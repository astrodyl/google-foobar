

"""
    :: THE CHALLENGE ::
    This problem was mainly a challenge in optimizing. I
    was able to find a brute force method rather quickly, 
    but it took very long (and I didn't even try 10^50)!

    :: BRUTE FORCE ::
    The brute force methods involves creating a tree of
    all valid paths until either the end value is reached,
    or both values exceed the end values. Not bad for small
    trees, but it quickly gets out of hand.

    :: AN ATTEMPT AT AN ALGORITHM ::
    For my first attempt at finding an optimized algorithm,
    I thought I had a great solution. However, it failed 
    for any value pair that contained an even number. I found
    ways around it, but the number of edge cases was a red flag
    that there was a much simpler solution. 

    :: MY OPTIMAL SOLUTION ::
    I'm not surre if this is the very best solution, but it 
    is the best that I could conjure up! It was pretty cool 
    once I realized that I could start with the end values and 
    work my way to the start values (1,1).

    I originally subtracted the smaller number from the larger number
    until the larger number became the smaller number. Then repeated.
    This works but it is too slow for cases x >> y. I realized that 
    I could break up the difference into segments (e.g. (x-y)/y)
    and count those segments as generations.
"""


def solution(M, F):

    # boundary conditions
    x = int(M)
    y = int(F)

    # the algorithm can handle two even inputs,
    # but why bother when I know that there is
    # no possible solution a priori
    if x%2==0 and y%2==0:
        return 'impossible'

    generation = 0
    while x != y:

        if x > y:
            # Division of ints changed from Python2 -> Python3
            gen = (x - y)//y
            if gen == 0: 
                gen+=1

            x = x - gen * y
            generation += int(gen)

        if x < y:
            gen = (y-x)//x
            if gen == 0:
                gen+=1

            y = y - gen * x
            generation += int(gen)

    # return statement handles cases when x=y but not (1,1)
    # can easily be modified for any starting combinations of bombs
    return str(generation) if (x, y) == (1, 1) else 'impossible'
