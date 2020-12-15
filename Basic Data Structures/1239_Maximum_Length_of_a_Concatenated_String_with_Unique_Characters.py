def maxLength(arr):  # O(2^N * s) where s is the maximum length of the input strings.
    def check_valid(curr_li, string):
    d = {}
    new_list = curr_li + list(string)
    for char in new_list:
        if char in d:
            return [], False
        d[char] = True
    return new_list, True

    def try_all_subseq(arr, curr, curr_string_li):
        if curr >= len(arr):
            self.max_res = max(max_res, len(curr_string_li))
            return
        if len(curr_string_li) == 26:
            max_res = 26
            return
    
    new_char_li, is_possible = check_valid(curr_string_li, arr[curr])
    if is_possible:
        try_all_subseq(arr, curr + 1, new_char_li)
            
    try_all_subseq(arr, curr + 1, curr_string_li)

    max_res = 0
    try_all_subseq(arr, 0, [])
    return max_res


def maxLength_dfs(arr):
    def clean(A):
        res = []
        for x in A:
            s = set(x)
            if x and (  len(s)==len(x)  ):
                res.append(s)
        return res
    def connect(A):
        A = clean(A)
        L = len(A)
        # 1) Build Dictionary
        d = dict(zip( range(L), [set() for _ in range(L)]))
        for i in range(L - 1):
            x  = A[i]
            for j in range(i + 1, L):
                y = A[j]
                if x.isdisjoint(y):
                    # d[i]: All connections are formed going forward (avoid back and forth play)
                    d[i].add(j) 
        # 2) Convert A to length array
        A = list(map(len,A))
        return d, A
    d, A = connect(A)
        def dfs(i,use):
            # use: Restrict allowed connections (past actions are preserved)
            use = use.intersection(d[i]) 
            # x: Length of Upcoming Concetenations
            x = 0                        
            for j in use:
                # March Forward (with restrictions imposed)
                x = max( x ,dfs(j, use))  
            return A[i] + x
        res = 0
        for i in range(len(A)):
            # Start concatenations from "i"
            res = max( res , dfs(i, d[i])) 
        return res