def smallestCommonElement(mat):
    d = {}
    for el in mat:
        for i in el:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    if len(mat) not in d.values():
        return -1
    else:
        return [k for k,v in d.items() if v == len(mat)][0]

if __name__ == '__main__':
    print(smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
