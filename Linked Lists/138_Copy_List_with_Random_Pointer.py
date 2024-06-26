def copyRandomList_dict(self, head):  # O(n) and O(n) with a dictionary
    if not head: return
    # first pass copy the normal chain, remember the nodes
    memory = {None: None}
    new_root = ListNode(-1)
    new_node, node = new_root, head
    while node:
        # append new node
        new_node.next = ListNode(node.val)
        new_node = new_node.next
        # save to memory
        memory[node] = new_node
        # move forward
        node = node.next
    # second pass add random pointers
    new_node, node = new_root.next, head
    while node:
        random = node.random
        new_node.random = memory[random]
        # move forward
        node = node.next
        new_node = new_node.next
    return new_root.next


def copyRandomList_short(self, head): # O(n) both
    """
    Create a dictionary. Has to be with None, won't work otherwise 
    It will have elements: node from the original list : newly created node with this value
    Keys (or new nodes) in this dictionary have "next" and "random." Need to fill them out
    At the end, return the key that corresponds to the head of the new list
    """
    d = {None : None}
    ptr = head
    while ptr:
        d[ptr] = ListNode(ptr.val)
        ptr = ptr.next
    ptr = head
    while ptr:
        d[ptr].next = d[ptr.next]
        d[ptr].random = d[ptr.random]
        ptr = ptr.next
    return d[head]


def copyRandomList_recursive(self, head): # O(n) and O(n)
    if head == None:
        return None
    # If we have already processed the current node, then we simply return the cloned version of it.
    if head in self.visitedHash:
        return self.visitedHash[head]
    # create a new node
    # with the value same as old node.
    node = Node(head.val, None, None)
    # Save this value in the hash map. This is needed since there might be
    # loops during traversal due to randomness of random pointers and this would help us avoid them.
    self.visitedHash[head] = node
    # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
    # Thus we have two independent recursive calls.
    # Finally we update the next and random pointers for the new node created.
    node.next = self.copyRandomList(head.next)
    node.random = self.copyRandomList(head.random)
    return node


def copyRandomList_iter(self, head): # O(n) and O(n)
    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary          
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None
    if not head:
        return head
    old_node = head
    # Creating the new head node.       
    new_node = Node(old_node.val, None, None)
    self.visited[old_node] = new_node
    # Iterate on the linked list until all nodes are cloned.
    while old_node != None:
        # Get the clones of the nodes referenced by random and next pointers.
        new_node.random = self.getClonedNode(old_node.random)
        new_node.next = self.getClonedNode(old_node.next)
        # Move one step ahead in the linked list.
        old_node = old_node.next
        new_node = new_node.next
    return self.visited[head]


def copyRandomList_iter_efficient(self, head):  # O(n) and O(1)
    if not head:
        return head
    # Creating a new weaved list of original and copied nodes.
    ptr = head
    while ptr:
        # Cloned node
        new_node = Node(ptr.val, None, None)

        # Inserting the cloned node just next to the original node.
        # If A->B->C is the original linked list,
        # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        new_node.next = ptr.next
        ptr.next = new_node
        ptr = new_node.next
    ptr = head
    # Now link the random pointers of the new nodes created.
    # Iterate the newly created list and use the original nodes random pointers,
    # to assign references to random pointers for cloned nodes.
    while ptr:
        ptr.next.random = ptr.random.next if ptr.random else None
        ptr = ptr.next.next
    # Unweave the linked list to get back the original linked list and the cloned list.
    # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    ptr_old_list = head # A->B->C
    ptr_new_list = head.next # A'->B'->C'
    head_old = head.next
    while ptr_old_list:
        ptr_old_list.next = ptr_old_list.next.next
        ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
        ptr_old_list = ptr_old_list.next
        ptr_new_list = ptr_new_list.next
    return head_old