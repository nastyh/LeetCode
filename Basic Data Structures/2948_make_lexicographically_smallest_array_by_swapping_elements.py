from collections import defaultdict
from typing import List

"""
O(nlogn) due to sortung
O(n) to maintain the union-find structure, the results list, the dict of connected components

Disjoint Set Union (DSU) (also called Union-Find) to efficiently manage the connected components
sort the array nums, but we will also keep track of the original indices of each element.
This is essential because we need to update the original nums array based on the connected components of the sorted array
Use Union-Find (DSU) to group the elements that are "connected". We only need to check if consecutive elements
in the sorted array are within the allowed difference (i.e., |nums[i] - nums[i+1]| <= limit).
If they satisfy the condition, they belong to the same connected component.
ou will have a set of consecutive indices in the sorted array that belong to the same connected component.
These indices are linked together by the union-find structure.
For each connected component, replace the elements at the indices in that component
with the smallest available value from the component. This will ensure the lexicographically smallest arrangement for those elements.
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n # corresponds to the indices in nums
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Step 1: Initialize UnionFind
        uf = UnionFind(n)
        # Step 2: Sort indices by values in nums while keeping track of original indices
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
        
        # Step 3: Union indices that can be swapped based on the limit
        for i in range(1, n):
            if abs(nums[sorted_indices[i]] - nums[sorted_indices[i - 1]]) <= limit:
                uf.union(sorted_indices[i], sorted_indices[i - 1])
        
        # Step 4: Group indices by connected components
        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)
        
        # Step 5: Sort each component and update the result array
        result = nums[:]
        for component in components.values():
            # Get the values of the component, sort them, and assign back to the indices
            values = sorted(nums[i] for i in component)
            component.sort()  # Sort indices
            for i, idx in enumerate(component):
                result[idx] = values[i]
        
        # Step 6: Return the lexicographically smallest array
        return result