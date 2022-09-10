def findBuildings(heights):  # O(nlog(n)) and O(1)
    """
    start from the right. The last one always has a view
    curr_max contains the highest building so far if we go from the right
    If the left building is taller than the right building, we check whether we've seen
    even a taller building to the right. If no, then the left building has a view. 
    Need to sort at the end 
    """
    res = [len(heights) - 1]
    curr_max = heights[-1]
    for i in range(len(heights) - 2, -1, - 1):
        if heights[i] > heights[i + 1]:
            if heights[i] > curr_max:
                res.append(i)
                curr_max = heights[i]
    return sorted(res)


def findBuildings_improved(heights): # O(n) and O(1)
    """
    exactly as above
    We don't have to sort, it's enough to just reverse the list
    """
    res = [len(heights) - 1]
    curr_max = heights[-1]
    for i in range(len(heights) - 2, -1, - 1):
        if heights[i] > heights[i + 1]:
            if heights[i] > curr_max:
                res.append(i)
                curr_max = heights[i]
    return res[::-1]
    

def findBuildings_stack(heights): # O(n) and O(1)
    """
    stack allows to avoid sorting
    """
    stack = []
    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        stack.append(i)
    return stack


if __name__ == '__main__':
    print(findBuildings([4,2,3,1]))    
    print(findBuildings([4,3,2,1])) 
    print(findBuildings([1,3,2,4]))
    print(findBuildings_stack([4,2,3,1]))    
    print(findBuildings_stack([4,3,2,1])) 
    print(findBuildings_stack([1,3,2,4]))