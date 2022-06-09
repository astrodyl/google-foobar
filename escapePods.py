"""
    :: Approach ::
        Determining the number of bunnies that can
        escape is equivalent to determining the max
        flow of a network. A few algorithms can be
        implemented here, but Dinic's will be the
        most efficient.

    :: Multi-Source/Sink Adjustment ::
        Dinic's Algorithm requires there to be a single
        source and a single sink. To handle cases when
        this is not true, I create paths from a super-
        source to every original source, and paths from
        every original sink to the super-sink. These
        paths have infinite capacity.

    :: Analysis ::
        Time Complexity (Dinic's): O(EV^2), where E 
        = # of edges and V = # of vertices. In most
        cases, the time complexity is often much smaller.
"""

# display all nodes and their levels 
def printLevels(level):
    print("Nodes", " ", "Level")
    for i in range(len(level)):
        print(" ",i,  " --> ", level[i])
    print()

# transform multi-source to single source
def transformSource(graph, entrances, V):
        for i in range(V):
            graph[i].insert(0, 0)
        graph.insert(0, ([999999 if (i-1 in entrances) else 0 for i in range(V+1)]))
        return graph, V+1


# transform multi-sink to single sink
def transformSink(graph, exits, V, n):
    for i in range(V):
        if i-n not in exits:
            graph[i].append(0)
        else:
            graph[i].append(999999)
    graph.append([0 for i in range(V)])
    return graph, V+1


# find blocking flow
def dfs(c_graph, f_graph, level, vrtx, r):
    n = len(c_graph)
    r_hold = r

    if vrtx == n - 1:
        return r
    for i in range(n):
        # path must go +1 level and have residual flow
        if (level[i] == level[vrtx]+1) and \
            (f_graph[vrtx][i] < c_graph[vrtx][i]):

            res = min(r_hold, c_graph[vrtx][i] - f_graph[vrtx][i])
            f = dfs(c_graph, f_graph, level, i, res)
            f_graph[vrtx][i] = f_graph[vrtx][i] + f
            f_graph[i][vrtx] = f_graph[i][vrtx] - f
            r_hold -= f

    return r - r_hold


# construct level graph using bfs
def bfs(c_graph, f_graph, s, t):
    n = len(c_graph)
    q = []
    q.append(s)

    level = [None] * n
    level[s] = 0

    seen = [False] * n
    seen[s] = True

    while q:
        vrtx = q.pop(0)
        for i in range(n):
            if (not seen[i]) and (f_graph[vrtx][i] < c_graph[vrtx][i]):
                q.append(i)
                level[i] = level[vrtx] + 1
                seen[i] = True

    return seen[t-1], level


# Driver Code 
def solution(entrances, exits, paths):
    V = len(paths)

    if len(entrances) > 1:
        paths, V = transformSource(paths, entrances, V)
    if len(exits) > 1:
        paths, V = transformSink(paths, exits, V, len(entrances)-1)

    flow = [V*[0] for i in range(V)]
    max_flow = 0

    # Dinic's Algortihm
    while True:
        path, level = bfs(paths, flow, 0, V)

        if not path:
            msg = 'Breaking path reached! '
            msg += 'The max flow is {0}.'.format(max_flow)
            print(msg)
            break
        else:
            printLevels(level)
        max_flow += dfs(paths, flow, level, 0, 10000)
    return max_flow


""" TEST CASES """

# V = 6
# path = [[] for i in range(V)]
# entrances = [0]
# exits = [5]

# path[0] = [0, 10, 10, 0, 0, 0]
# path[1] = [0, 0, 2, 3, 8, 0] 
# path[2] = [0, 0, 0, 0, 9, 0]
# path[3] = [0, 0, 0, 0, 0, 10]
# path[4] = [0, 0, 0, 6, 0, 10]
# path[5] = [0, 0, 0, 0, 0, 0]

entrances = [0,1]
exits = [4,5]
V = 6
path = [[] for i in range(V)]

path[0] = [0, 0, 4, 6, 0, 0]
path[1] = [0, 0, 5, 2, 0, 0]
path[2] = [0, 0, 0, 0, 4, 4]
path[3] = [0, 0, 0, 0, 6, 6]
path[4] = [0, 0, 0, 0, 0, 0]
path[5] = [0, 0, 0, 0, 0, 0]

# Caller
solution(entrances, exits, path)
