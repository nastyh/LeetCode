from collections import deque
def validateBinaryTreeNodes(n, leftChild, rightChild):  # O(n) both 
    # find the root node, assume root is node(0) by default
    # a node without any parent would be a root node
    # note: if there are multiple root nodes => 2+ trees
    root = 0
    childrenNodes = set(leftChild + rightChild)
    for i in range(n):
        if i not in childrenNodes:
            root = i
    # keep track of visited nodes
    visited = set()
    # queue to keep track of in which order do we need to process nodes
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node in visited:
            return False
        # mark visited
        visited.add(node)
        # process node
        if leftChild[node] != -1:
            queue.append(leftChild[node])
        if rightChild[node] != -1:
            queue.append(rightChild[node]) 
    # number of visited nodes == given number of nodes
    # if n != len(visited) => some nodes are unreachable/multiple different trees
    return len(visited) == n


def validateBinaryTreeNodes_topological(n, leftChild, rightChild):
    indegree = [0] * n
    for left, right in zip(leftChild, rightChild):
        if left > -1: indegree[left] += 1
        if right > -1: indegree[right] += 1
        if indegree[left] > 1 or indegree[right] > 1: return False
    queue = collections.deque(i for i, d in enumerate(indegree) if d == 0)
    if len(queue) > 1: return False
    while queue:
        node = queue.popleft()
        for child in leftChild[node], rightChild[node]:
            if child == -1: continue
            indegree[child] -= 1
            if indegree[child] == 0: queue.append(child)
    return sum(indegree) == 0


def validateBinaryTreeNodes_another(n, leftChild, rightChild):
    indegree = [0] * n
    for l, r in zip(leftChild, rightChild):
        if l != -1:
            indegree[l] += 1
            # if there are nodes that has more than 2+ parents, return false.
            if indegree[l] > 1:
                return False
        if r != -1:
            indegree[r] += 1
            if indegree[r] > 1:
                return False
    # a valid tree only has 1 root. 
    if indegree.count(0) != 1:
        return False
    # count nodes from root, if the total number is not n, it means there are islands, then return false.
    root = indegree.index(0)
    def count_nodes(root):
        if root == -1:
            return 0
        return 1 + count_nodes(leftChild[root]) + count_nodes(rightChild[root])
    return count_nodes(root) == n


def validateBinaryTreeNodes_dict(n, leftChild, rightChild):
    nodes = {0: TreeNode(0)}
    for i in range(len(leftChild)):
        if i not in nodes: return False
        if leftChild[i] >= 0 and leftChild[i] in nodes: return False
        if rightChild[i] >= 0 and rightChild[i] in nodes: return False
        if i in nodes:
            n = nodes[i]
            if leftChild[i] >= 0:
                n.left = TreeNode(leftChild[i])
                nodes[leftChild[i]] = n.left
            if rightChild[i] >= 0:
                n.right = TreeNode(rightChild[i])
                nodes[rightChild[i]] = n.right
    return True

