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


def trap_short(height):
    if not height:   return 0
    max_left, max_right = [height[0]], [height[-1]]

    for i in range(1, len(height)):
        max_left.append(max(max_left[-1], height[i]))
        max_right.append(max(max_right[-1], height[-1 - i]))

    return sum(min(l, r) - h for l, r, h in zip(max_left, reversed(max_right), height))
