def combinationSum2(self, candidates, target): # returns a list of lists
    if not candidates:
            return []

    ret = []

    def fn(nums, tmp):
        if sum(tmp) > target:
            return False
        elif sum(tmp) == target:
            if tmp not in ret:
                ret.append(tmp)
            return True
        else:   # sum(tmp) < target
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]: continue
                fn(nums[i+1:],tmp+[nums[i]])

        candidates.sort()
        fn(candidates,[])
        return ret
