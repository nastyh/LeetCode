from heapq import heappush, heappop
from collections import deque
import math
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


    def closestKValues(self, root, target, k):  # NlogN and O(N)
        """
        easiest:
        traverse inorder, build a list, sort, return k values
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        nums = inorder(root)
        nums.sort(key = lambda x: abs(x - target))
        return nums[:k]


    def closestKValues_heap(self, root, target, k):  # NlogK, O(K + h)
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

    
    def closestKValues_bfs(self, root, target, k):
        """
        Traverse the tree in a BFS manner, keep track of the difference, as well
        Build a heap in parallel: first element is the difference, second element is a node's value
        Return first k values from the heap. It will give tuples. You need the second element from the tuple
        """
        h, d, res = [], deque(), []
        d.append((root, abs(root.val - target)))
        while d:
            t, diff = d.popleft()
            heappush(h, (diff, t.val))
            if t.left:
                d.append((t.left, abs(t.left.val - target)))
            if t.right:
                d.append((t.right, abs(t.right.val - target)))
        for _ in range(k):
            res.append(heappop(h))
        return [j for i, j in res]

    
    def closestKValues_bfs_improved(self, root, target, k):  # O(Nlogk) time, O(k + D) space, where k is for the heap, and D is the tree's widest level 
        """
        Slightly improved solution compared to the previous one: always keep k elements in the heap, thus, taking less space
        """
        h, d = [], deque()
        d.append((root, abs(root.val - target)))
        while d:
            t, diff = d.popleft()
            if len(h) < k:
                heappush(h, (-diff, t.val))
            else:
                heappush(h, (-diff, t.val))
                heappop(h)
            if t.left:
                d.append((t.left, abs(t.left.val - target)))
            if t.right:
                d.append((t.right, abs(t.right.val - target)))
        return [j for _, j in h]


    def closestKValues_quicksort(self, r, target): # O(n) or O(n^) in the worst; O(N) to store
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


    def closestKValues_sides(self, root, target, k):  # worst time is O(n) vs quicksort's O(n^2)
        """
        Do inorder, save values
        Iterate thru the list, find the closest value to target
        Have two pointers expanding to the left and right sides from this value
        If the left value is closer to the target, expand the left pointer
        Otherwise, expand the right pointer
        """
        sorted = []
        def _traverse(node):
            if node is None:
                return
            _traverse(node.left)
            sorted.append(node.val)
            _traverse(node.right)
        _traverse(root)
        lo, hi = 0, len(sorted)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if sorted[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        left, right = lo - 1, lo
        res = []
        while k:
            left_delta = math.inf
            if left >= 0:
                left_delta = abs(sorted[left] - target)
            right_delta = math.inf
            if right < len(sorted):
                right_delta = abs(sorted[right] - target)
            if left_delta < right_delta:
                res.append(sorted[left])
                left -= 1
            else:
                res.append(sorted[right])
                right += 1
            k -= 1
        return res


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(5)
    l.left.left = TreeNode(1)
    l.left.right = TreeNode(3)
    # print(l.closestKValues_heap(l, 3.714286, 2))
    print(l.closestKValues_bfs(l, 3.714286, 2))
    print(l.closestKValues_bfs_improved(l, 3.714286, 2))
    print(l.closestKValues_sides(l, 3.714286, 2))