def count_of_nodes(root, queries, st):
    def postorder(result, curr, queries, st, parents):
        if curr is not None:
            parents.append(curr.val)
            for child in curr.children:
                postorder(result, child, queries, st, parents)
            for i in range(len(queries)): 
                qRootVal = queries[i][0]
                qChar = queries[i][1]
                if qRootVal in parents and qChar == st[curr.val - 1]:
                    result[i] += 1
            parents.pop()
            
    result = [0] * len(queries)
    postorder(result, root, queries, st, [])
    return result