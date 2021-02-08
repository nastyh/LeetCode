class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def distanceK(self, root, target, K):  # O(n) both 
        if root is None:
            return []
		# if distance of 0 is asked the return the target node itself
        if K == 0:
            return [target.val]
		# In first BFS iteration we will create a Parent mapping for every node (for root it will be None) 
		# as we also want to traverse up from the target node
        queue = [root]
        next_queue = []
        parent = {}
        parent[root] = None
        while queue:
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                    parent[node.left] = node
                if node.right:
                    next_queue.append(node.right)
                    parent[node.right] = node
            queue = next_queue
            next_queue = [] 
        # Now traditional BFS but taking parent along with left and right child
        queue = [target]
        next_queue = []
        res = []
		# keeping a track of visited nodes 
        seen = set()
        while queue:
            for node in queue:
                seen.add(node)
                if K == 0:
                    res.append(node.val)
                if node.left and node.left not in seen:
                    next_queue.append(node.left)
                if node.right and node.right not in seen:
                    next_queue.append(node.right)
                if parent[node] and parent[node] not in seen:
                    next_queue.append(parent[node])
			# we will decrement K and when it will become 0 we will get to the result, 
			# i.e. we have successfully travelled to K nodes away from target
            K -= 1
            queue = next_queue
            next_queue = []
        return res


    def distanceK_alt(self, root, target, K):  # O(n) both 
        res = []
        def searchNodes(node,dist):
            if node is None:
                return
            if dist ==0:
                res.append(node.val)
            else:
                searchNodes(node.left, dist - 1)
                searchNodes(node.right, dist - 1)
        def distFromRoot(root,target):
            if root is None:
                return -1
            if root is target: 
                return 1
            l = distFromRoot(root.left, target)
            r = distFromRoot(root.right, target)
            if l == -1 and r == -1:
                return -1
            if l!=-1:
                if l == K:
                    res.append(root.val)
                    return -1
                else:
                    searchNodes(root.right,K - l - 1)
                    return l + 1

            if r != -1:
                if r == K:
                    res.append(root.val)
                    return -1
                else:
                    searchNodes(root.left, K - r - 1)
                    return r + 1
        p = distFromRoot(root, target)
        searchNodes(target, K)
        return res