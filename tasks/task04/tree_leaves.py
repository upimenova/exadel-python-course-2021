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
                if type(value) is dict:
                    _collect_leaves(value, result)
                else:
                    result.append(value)
        else:
            for i in leaf:
                result.append(i)
    res = list()
    _collect_leaves(leaf, res)
    return res

# def collect_leaves(leaf):
#     if type(leaf) is dict:
#         for key, value in leaf.items():
#             if type(value) is dict:
#                 collect_leaves(value)
#             else:
#                 leaves.append(value)
#     else:
#         for i in leaf:
#             leaves.append(i)
#     return leaves


assert collect_leaves([1, 2, 3]) == [1, 2, 3], 'Your solution is incorrect!'
print(collect_leaves(tree))
# assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9]
