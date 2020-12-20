def decodeAtIndex(S, K):  # O(n^2) b/c we overwrite a string? And O(SK) in space
    """
    Brute force. Works but LTA
    """
    res = ''
    for k, ch in enumerate(S):
        if not ch.isdigit():
            res += ch
            if len(res) == K:
                return res[K - 1]
        else:
            res += res * (int(ch) - 1)
    return res[K - 1]


def decodeAtIndex_optimized(S, K):  # O(n) and O(K)
    """
    Build a stack of integers. If a respective element in S is a letter, keep incrementing an index
    If it's a number, multiply the previous number by two
    Then it's tricky: go back and do modulo division
    """
    st = [1]
    for ch in S[1:]:
        if st[-1] >= K:
            break
        if ch.isdigit():
            st.append(st[-1] * int(ch))
        else:
            st.append(st[-1] + 1)
    for i in reversed(range(len(st))):
        K %= st[i]
        if not K and S[i].isalpha():
            return S[i]


if __name__ == '__main__':
    print(decodeAtIndex('leet2code3', 10))
    print(decodeAtIndex_optimized('leet2code3', 10))