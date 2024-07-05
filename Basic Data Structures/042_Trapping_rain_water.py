def trap_explained(self, height: List[int]) -> int:
        """
        O(n) and O(1)
        two pointers: from left and from right
        need to track the max size from left and from right
        try to store the water from the highest point to maximize the result
        but we're limited by the min height
        """
        l, r, res = 0, len(height) - 1, 0
        l_max, r_max = 0, 0 
        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l] # we found a better candidate, a taller one
                else:
                    res += l_max - height[l] # limited by the left side, take whatever we can
                l += 1 # since it's the limit, we are tied to the smaller one, let's keep moving
            else:
                if height[r] > r_max:
                    r_max = height[r] # better candidate
                else:
                    res += r_max - height[r] # the diff is what we can keep
                r -= 1
        return res 

    def trap_with_space(self, height: List[int]) -> int:
        """
        height = []
        max_left = list of the same size, in each cell contains the max number to the left
        max_right = list of the same size, in each cell contains the max number to the right
        min(max_left, max_right) = same size, obvious
        We can also keep it in variables, thus, saving some space
        """
        l, r = 0, len(height) - 1
        res = 0
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max < r_max: 
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res


def trap(height):
    if not height:
        return 0
    # left -> right
    left_right = []
    left = 0
    for e in height:
        left_right.append(left)
        # keep track of the largest I have seen so far
        if left < e:
            left = e
    # right -> left
    right_left = []
    right = 0
    for i in reversed(range(len(height))):
        right_left.append(right)
        # keep track of the largest I have seen so far
        if right < height[i]:
            right = height[i]
    # compute water volume
    water_volume = 0
    for i, e in enumerate(height):
        # water level contained by the borders
        water_level = min(left_right[i], right_left[~i])
        # water above the current floor
        water_volume += max(water_level - height[i], 0)
    return water_volume


def trap_two_passes(height):  # O(n) both but technically O(2n)
    """
    Need to cover the edge case (important)
    Do two passes: from left to right and vice versa 
    Initialize the first element with the first element in height
    Then choose the max b/w the current height and the previous value in the helper array 
    This way we'll maximize the gains: it's like moving left/right until we hit a taller building, then go to its roof and repeat
    Do the same from right to left
    Finally iterate over two helper arrays, choose the min value (b/c the water will overflow otherwise),
    and subtract the current height from this number to get how much water is in this cell
    """
    if len(height) == 0: return 0
    from_left, from_right = [0] * len(height), [0] * len(height)
    from_left[0] = height[0]
    for i in range(1, len(height)):
        from_left[i] = max(from_left[i - 1], height[i])
    from_right[-1] = height[-1]
    for j in range(len(height) -2, -1, -1):
        from_right[j] = max(from_right[j + 1], height[j])
    for z in range(len(height)):
        res += min(from_left[z], from_right[z]) - height[z]
    return res


def trap_short(height):
    if not height:   return 0
    max_left, max_right = [height[0]], [height[-1]]
    for i in range(1, len(height)):
        max_left.append(max(max_left[-1], height[i]))
        max_right.append(max(max_right[-1], height[-1 - i]))
    return sum(min(l, r) - h for l, r, h in zip(max_left, reversed(max_right), height))


if __name__ == '__main__':
    print(trap_two_passes([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap_two_passes([4, 2, 0, 3, 2, 5]))
