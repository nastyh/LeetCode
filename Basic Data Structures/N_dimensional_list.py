"""
You are given an N-Dimensional list with 2 methods:
i) getDim -> returns the dimensions .e.g [5,4,3].
ii) getElement([i,j,k]) -> return list[i][j][k] . You have to implement a method to sum all elements in the list.
"""
dims = getDim()
def get_all_elements(dims):
    def get_perms(dims):
        if len(dims) == 1:
            return map(lambda x: [x], list(range(dims[0])))
        else:
            res = []
            for head in range(dims[0]):
                for sub_arr in get_perms(dims[1:]):
                    res.append([head] + sub_arr)
        return res
    elements = [getElement(pos) for pos in get_perms(dims)]
    return elements