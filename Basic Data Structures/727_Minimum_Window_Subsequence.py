from collections import deque
def minWindow_queue(S, T):
    candidates = deque([index for index in range(len(S)) if S[index] == T[0]])
    if not candidates:
        return ""
    
    leftovers = [i for i in T[1:]]
    if not leftovers:
        return S[candidates[0]]
    min_left, min_right = 0, -1
    while candidates:
        index = candidates.popleft()
        q = collections.deque(leftovers)
        r_index = index + 1
        while q:
            next_index = S.find(q.popleft(), r_index)
            if next_index == -1:
                break
            r_index = next_index + 1
        else:
            if min_right == -1 or min_right - min_left > r_index - index - 1:
                min_right, min_left = r_index - 1, index   
    return S[min_left : min_right + 1]


def minWindow_pointers(S, T):
    j = 0
    end = 0
    ans = ''
    res = len(S) + 1
    i = 0
    while(i < len(S)):   
        if S[i] == T[j]:
            j += 1
            if j == len(T):
                end = i
                j -= 1 # Bringing J back into bounds
                while(j >= 0):
                    if T[j] == S[i]:
                        j -= 1
                    i -= 1
                
                i += 1
                j = 0
                
                if(end - i + 1) < res:
                    res = end - i
                    ans = S[i:end + 1]
        i += 1                
    return ans


def minWindow_dp(S, T):  # O(ST) and O(S)
    N = len(S)
    nxt = [None] * N
    last = [-1] * 26
    for i in xrange(N-1, -1, -1):
        last[ord(S[i]) - ord('a')] = i
        nxt[i] = tuple(last)

    windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
    for j in xrange(1, len(T)):
        letter_index = ord(T[j]) - ord('a')
        windows = [[root, nxt[i+1][letter_index]]
                    for root, i in windows
                    if 0 <= i < N - 1 and nxt[i + 1][letter_index] >= 0]

    if not windows: return ""
    i, j = min(windows, key = lambda (i, j): j - i)
        return S[i: j + 1]