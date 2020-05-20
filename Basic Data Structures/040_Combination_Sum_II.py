def combinationSum2(candidates, target): # returns a list of lists
    results=[]
    candidates.sort()
    def backtrack(target,curcan,partial):
        if target==0:
            if partial not in results:
                results.append(partial)
            return
        for item in curcan:
            if item>target:
                break
            elif partial and item<partial[-1]:
                continue
            else:
                renew=copy.copy(curcan)
                renew.remove(item)
                backtrack(target-item,renew,partial+[item])
        backtrack(target,candidates,[])
        return results

if __name__ == '__main__':
    print(combinationSum2([10,1,2,7,6,1,5], 8))
