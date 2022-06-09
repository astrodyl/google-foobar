from itertools import permutations

"""
This was a wild ride. My first idea was to find negative
cycles. This led me to a number of possibilites. E.g.,
the Floyd Warshall, Bellman-Ford, and even Johnson which 
uses the BF algorithm. 

My first attempt at a solution was to use Floyd Warshall
to find a negative cycle. If one existed, return that
all of the bunnies were saved. If not, we had to figure
out the best combinations of the shortest paths.

This is led me to implement the Johnson algorithm. I.e., 
use Bellman-Ford as a means of removing negative weights
and detecting negative cycles (2 for 1, I thought!). After
implementing BF, I would implement Dijkstra's algorithm
to find the shortest paths with the new weights. From here,
I could sum up all combinations and call it a day.

I think that this could work, but towards the end of my 
implementation, it seemed that I was drastically over-
complicating things. For one, I was using the FW algorithm
to detect a negative cycle, but I later implemented the BF
algorithm which could do the same thing rendering the FW
redundant. After mostly implementing Johnson's algoirthm,
I stopped, and re-evaluated the best path forward.

It wasn't a complete waste of time because going down this
path helped me to understand that problem and the algorithms.

I considered whether or not to import itertools here. I've
avoided using imports up until now, but time was short, and 
it was allowed under the constraints.
"""

# use Floyd Warshall to detect negative cycle O(V^3)
def negativeCycle(times):
    V = len(times)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    for i in range(V):
        if times[i][i] < 0:
            return True

    return False


def findPath(s, l):
    return s + [i for i in l] + [-1]


def addTime(t, p):
    k, tt = 0, 0
    while k < len(p)-1:
        tt += t[p[k]][p[k+1]]
        k+=1
    return tt


def solution(time, time_limit):
    num_of_ids = len(time) - 2
    
    if num_of_ids == 0:
        return []

    if negativeCycle(time):
        return [i for i in range(num_of_ids)]

    for i in range(num_of_ids + 1, 0, -1):
        # itertools does all of the heavy lifting
        for perm in permutations(range(1, num_of_ids + 1), i):
            path = findPath([0], perm)

            total_time = addTime(time, path)
            if total_time <= time_limit:
                saved_bunnies = list(i - 1 for i in perm)
                saved_bunnies.sort()
                return saved_bunnies
    return []


times = [[0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]]
time_limit = 3

# times = [[0, 2, 2, 2, -1],
#         [9, 0, 2, 2, -1],
#         [9, 3, 0, 2, -1],
#         [9, 3, 2, 0, -1],
#         [9, 3, 2, 2, 0]]
# time_limit = 1

# times = [[1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1]]
# time_limit = 1

print(solution(times, time_limit))