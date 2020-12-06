def getRow(numRows):  # using a traditional solution 
    if numRows   == 0: return [1]
    elif numRows == 1: return [1, 1]
    dp = [[1]]
    for i in range(1, numRows + 1):
        row = [1]
        for j in range(1, i):
            row.append(dp[i - 1][j - 1] + dp[i - 1][j]) 
        row.append(1)
        dp.append(row)
    return dp[-1]


def getRow_alt(rowIndex):
    cache = dict()
    def getNum(rowIndex, colIndex):
        rowCol = (rowIndex, colIndex)
        if cache.get(rowCol) != None:
            return cache[rowCol]
        # base case
        if rowIndex==0 or colIndex==0 or rowIndex==colIndex:
            cache[rowCol] = 1
            return 1
        cache[rowCol] = getNum(rowIndex -1 , colIndex - 1) + getNum(rowIndex - 1, colIndex)
        return cache[rowCol] 
    vals = []
    for i in range(rowIndex + 1):
        vals.append(getNum(rowIndex, i))
    return vals


def getRow_another(rowIndex):
    row = []
    for i in range(rowIndex+1):
        row.insert(0, 1)
        for j in range(1, len(row)-1):
            row[j]= row[j] + row[j+1]
    return row


if __name__ == '__main__':
    print(getRow(3))
    print(getRow(0))
    print(getRow(1))
    print(getRow_alt(3))
    print(getRow_alt(0))
    print(getRow_alt(1))
    print(getRow_another(3))
    print(getRow_another(0))
    print(getRow_another(1))