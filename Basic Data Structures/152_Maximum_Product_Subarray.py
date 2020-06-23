def maxProduct(nums):
    maxval=float('-inf')
    imax,imin=1,1
    for i in range(len(nums)):
        if nums[i]<0:
            imax,imin=imin,imax
        imax=max(imax*nums[i],nums[i])
        imin=min(imin*nums[i],nums[i])
        maxval=max(maxval,imax)
    return maxval

 def maxProduct_alt(nums):
        if not nums: return 0
        cur_max = final_max = cur_min = nums[0]
        for i in range(1 , len(nums)):
            temp = cur_max
            cur_max = max(max(cur_max * nums[i] , cur_min * nums[i]) , nums[i])
            cur_min = min(min(temp * nums[i] , cur_min * nums[i]) , nums[i])
            if cur_max > final_max:
                final_max = cur_max
        return final_max

def maxProduct_brute_force(self, nums: List[int]) -> int:
        res, curr = -math.inf, 1
        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i + 1, len(nums)):
                curr = curr * nums[j]
                res = max(res, curr)
        return res
