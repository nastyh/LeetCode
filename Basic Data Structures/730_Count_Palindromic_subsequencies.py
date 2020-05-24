def countPalindromicSubsequences(S):
    def binary_search(l,target):
        left=0
        right=len(l)-1
        while left<=right:
            mid=(left+right)//2
            if l[mid]==target:
                return mid
            elif l[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left

    def dfs(S,arr,memo,start,end):
        if start>=end:
            return 0
        if memo[start][end]>0:
            return memo[start][end]
        res=0
        for i in chars:
            new_start=None
            new_end=None
            l=arr[ord(i)-ord('a')]

            new_start = binary_search(l,start)
            new_end = binary_search(l,end)-1

            if new_end<0 or new_start>=len(l):
                continue

            new_start = l[new_start]
            new_end = l[new_end]

            if new_start>=end or new_end<start:
                continue

            res+=1
            if new_start!=new_end:
                res+=1
            res+=dfs(S,arr,memo,new_start+1,new_end)
        memo[start][end]=res%mod
        return memo[start][end]

    chars=['a','b','c','d']
    mod=10**9+7
    arr=[[] for i in range(4)]
    for i in range(len(S)):
        arr[ord(S[i])-ord('a')].append(i)
    memo=[[0]*(len(S)+1) for i in range(len(S)+1)]
    return dfs(S,arr,memo,0,len(S))



if __name__ == '__main__':
    print(countPalindromicSubsequences('bcbb'))
