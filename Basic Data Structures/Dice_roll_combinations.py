"""
Given an integer n, return all possible combinations of numbers 
one can get when rolling n 6-side dices
Input: n = 2
Output: [[1, 1], [1, 2], [1, 3],..., [6, 6]]
"""
def dice_combo(n):
    res = []
    def _helper(n, curr_res):
        if len(curr_res) == n:
            res.append(curr_res[:])
            return
        for i in range(1, 7):
            curr_res.append(i)
            _helper(n, curr_res)
            curr_res.pop()
    _helper(n, [])
    return res
    

if __name__ == '__main__':
    print(dice_combo(2))