

"""
    recursively search for leaf above
    the leaf of interest
"""
def binary_search(h, q, root):

    # root node has no element above
    if q == root:
        return -1

    left_node = root - 2**(h-1)
    right_node = root - 1

    if q == left_node or q == right_node:
        return root
    else:
        if q < left_node:
            return binary_search(h-1, q, left_node)
        else:
            return binary_search(h-1, q, right_node)


"""
    main caller
"""
def solution(h, q):
    root = sum([2**row for row in range(h)])
    p = []

    for val in q:
        if val > root:
            print('Flux converter {0} not found in the flux chain!'.format(val))
            p.append(None)
        else:
            p.append(binary_search(h, val, root))

    return p
