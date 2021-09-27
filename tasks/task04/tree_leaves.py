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
    def _collect_leaves(leaf, result):
        if type(leaf) is dict:
            for key, value in leaf.items():
                _collect_leaves(value, result)
        else:
            result += leaf
    res = list()
    _collect_leaves(leaf, res)
    return res


print(collect_leaves(tree))
assert collect_leaves([1, 2, 3]) == [1, 2, 3], 'Your solution is incorrect!'
assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9], 'Your solution is incorrect!'
