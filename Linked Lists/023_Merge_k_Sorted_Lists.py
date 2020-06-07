import heapq
def mergeKLists(self, lists):

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
