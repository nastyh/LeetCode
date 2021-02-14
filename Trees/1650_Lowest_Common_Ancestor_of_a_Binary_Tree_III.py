class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def lowestCommonAncestor_set(self, p, q):
        path = set()
        while p:
            path.add(p)
            p = p.parent 
        while q not in path:
            q = q.parent 
        return q

    
    def lowestCommonAncestor_iter(self, p, q):
        """
        values to lists and compare
        """
        p_path = []
        while p:
            p_path.append(p)
            p = p.parent
        q_path = []
        while q:
            q_path.append(q)
            q = q.parent 
        min_length = min(len(p_path), len(q_path))
        i = 1
        while i <= min_length:
            if q_path[-i] != p_path[-i]:
                return q_path[-i + 1]
            i += 1
        return q_path[-i + 1]


    def lowestCommonAncestor_iter_anoter(self, p, q):    
        """
        Same as above but comparing lists differently 
        """
        p_path = []
        while p:
            p_path.append(p)
            p = p.parent
        q_path = []
        while q:
            q_path.append(q)
            q = q.parent
        p_path.reverse()
        q_path.reverse()
        if len(p_path) == len(q_path):
            for i in range(1, len(p_path)):
                if p_path[i] != q_path[i]:
                    return p_path[i - 1]
        else: 
            i, j = 0, 0
            while i < len(p_path) and j < len(q_path):
                if p_path[i] != q_path[j]:
                    return p_path[i - 1]
                i += 1
                j += 1
            return p_path[i - 1]


if __name__ == '__main__':
    l = Node(3)
    l.left = Node(5)
    l.right = Node(1)
    l.parent = None
    l.left.left = Node(6)
    l.left.parent = l
    l.left.right = Node(2)
    l.left.right.parent = l.left
    l.left.right.left = Node(7)
    l.left.right.left.parent = l.left.right
    l.left.right.right = Node(4)
    l.left.right.right.parent = l.left.right
    l.right.left = Node(0)
    l.right.left.parent = l.right
    l.right.right = Node(8)
    l.right.right.parent = l.right

    print(l.lowestCommonAncestor_set(l.left, l.right))


