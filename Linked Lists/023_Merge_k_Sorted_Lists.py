import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def mergeKLists_brute_force(self, lists):  # O(nlogn) and O(n) where n is the number of nodes
        """
        Get all values into res
        Create a new Linkedlist using values from res 
        """
        res = []
        for element in lists:
            while element:
                res.append(element.val)
                element = element.next
        res.sort()
        dummy = ListNode(-1)
        curr = dummy
        for num in res:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return curr.next

    
    def mergeKLists_pairs(self, lists): # O(nlogK) where K is the number of linked lists and O(1)
        """
        Implementation of the merged sort algorithm
        Process lists in pairs using the _helper() function that returns a sorted list of two lists
        after the first pairing, k lists are merged into k/2 lists with an average 2N/k length
        Then k/4, k/8 --> thus, logK
        Then do it at most n times and repeat the procedure on average logK times 
        """
        if not lists or len(lists) == 0: return None 

        def _helper(list1, list2):
            dummy = ListNode(-1)
            curr = dummy
            if not list1 and not list2: return None
            if list1 and not list2:
                return list1
            if not list1 and list2:
                return list2
            while list1 and list2:
                if list1.val <= list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next 
            if list1:
                dummy.next = list1
            if list2:
                dummy.next = list2
            return curr.next
        
        while len(lists) > 1:
            merged = []
            for i in range(len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None 
                merged.append(_helper(l1, l2))
            lists = merged
        return lists[0]


    def mergeKLists_heap(self, lists):  # O(nlogK) and O(n) from O(n) to create a new linked list
        heap = []
        for a_list in lists:
            while a_list:
                heapq.heappush(heap, a_list.val)
                a_list = a_list.next
        dummy = head = ListNode(-1)
        for i in range(len(heap)):
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next
        return head.next

    def mergeKLists_alt(self, lists):
        if not lists: return
            n = len(lists)
            if n == 1: return lists[0]
            mid = n//2
            left = mergeKLists_alt(lists[:mid])
            # print(left)
            right = mergeKLists_alt(lists[mid:])

            return self.merge(left, right)

        def merge(self, left, right):
            dummy = ListNode(0)
            cur = dummy
            while left and right:
                if left.val <=right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur=cur.next

            if left:
                cur.next = left
            if right:
                cur.next = right
            return dummy.next
