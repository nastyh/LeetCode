def longestCommonPrefix(strs):
    if not strs:
        return ''
    strs.sort()
    if strs[0]:
        for i, (u, v) in enumerate(zip(strs[0], strs[-1])):
            if u != v:
                return strs[0][:i]
    return strs[0]


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))

