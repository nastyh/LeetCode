from heapq import heappush, heappop
def closestKValues(target, k):  # NlogN and O(N)
    """
    easiest:
    traverse inorder, build a list, sort, return k values
    """
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    nums = inorder(root)
    nums.sort(key = lambda x: abs(x - target))
    return nums[:k]


def closestKValues_heap(target, k):  # NlogK, O(K + h)
    """
    traverse in order, add to heap, take out k elements
    """
    def inorder(r):
        if not r:
            return
        inorder(r.left)
        heappush(heap, (- abs(r.val - target), r.val))
        if len(heap) > k:
            heappop(heap)
        inorder(r.right) 

    heap = []
    inorder(root)
    return [x for _, x in heap]


def closestKValues_quicksort(r, target): # O(n) or O(n^) in the worst; O(N) to store
    """
    Traverse the tree and convert it into array nums.
    Function to compute the distance to the target. Note that the distance is not unique. That means we need a partition algorithm that works fine with duplicates.
    Work with nums array. Use a partition scheme (please check the next section) to place the pivot into its perfect position pivot_index in the sorted array,
    move more close elements to the left of the pivot, and less close or of the same distance - to the right.    
    Compare pivot_index and k.
    If pivot_index == k, the pivot is the kth less close element, and all elements on the left are the kk closest elements to the target. Return these elements.
    Otherwise, choose the side of the array to proceed recursively.
    """
    def inorder(r: TreeNode):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
    def partition(pivot_idx, left, right):
        pivot_dist = dist(pivot_idx)
        
        # 1. move pivot to end
        nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
        store_idx = left
        
        # 2. move more close elements to the left
        for i in range(left, right):
            if dist(i) < pivot_dist:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
                
        # 3. move pivot to its final place
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        
        return store_idx
        
    def quickselect(left, right):
        """
        Sort a list within left..right till kth less close element
        takes its place.
        """
        # base case: the list contains only one element
        if left == right:
            return 
        
        # select a random pivot_index
        pivot_idx = randint(left, right)
        
        # find the pivot position in a sorted list
        true_idx = partition(pivot_idx, left, right)
        
        # if the pivot is in its final sorted position
        if true_idx == k:
            return
        
        if true_idx < k:
            # go left
            quickselect(true_idx, right)
        else:
            # go right
            quickselect(left, true_idx)
    
    nums = inorder(root)
    dist = lambda idx : abs(nums[idx] - target)
    quickselect(0, len(nums) - 1)
    return nums[:k]