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


def collect_leaves(leaf):
    leaves = []
    if type(leaf) is dict:
        for key, value in leaf.items():
            if type(value) is dict:
                collect_leaves(value)
            else:
                leaves.append(value)
    else:
        for i in leaf:
            leaves.append(i)
    print(leaves)


assert collect_leaves([1, 2, 3]) == [1, 2, 4], 'Your solution is correct!'
collect_leaves(tree)
# collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9]
#
# # edge case: flat tree, i.e. list
# collect_leaves([1, 2, 3]) == [1, 2, 3]
#
# # assert example
# assert my_pow(5, 3) == 125, “incorrect power implementation”