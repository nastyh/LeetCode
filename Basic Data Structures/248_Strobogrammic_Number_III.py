def strobogrammaticInRange(low, high):
    pairs = [('8','8'), ('1','1'), ('0','0'), ('6','9'), ('9','6')]
    count = 0
    def dfs(low, high, left, right, s):
        ins = int(''.join(s))
        if (left > right):
            if low <= ins <= high:
                self.count += 1
            return
        for x, y in pairs:
            if len(s) != 1 and left == 0 and x == '0': continue
            if left == right and x != y: continue
            s[left] = x
            s[right] = y
            dfs(low, high, left + 1, right - 1,s)
            
    for i in range(len(low), len(high)+1):
        s = ['0'] * i #initiate an array to store the number
        dfs(int(low), int(high), 0, i - 1, s)
    return count