tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}
leaves = []


def collect_leaves(leaf):
    if type(leaf) is dict:
        for key, value in leaf.items():
            if type(value) is dict:
                collect_leaves(value)
            else:
                leaves.append(value)
    else:
        for i in leaf:
            leaves.append(i)
    return leaves


# assert collect_leaves([1, 2, 3]) == [1, 2, 3], 'Your solution is incorrect!'
print(collect_leaves(tree))
# collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9]
