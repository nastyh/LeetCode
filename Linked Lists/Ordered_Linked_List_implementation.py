# Implementation of ordered linked List:
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self,val):
        self.head = Node(val)

    def isEmpty(self):
        self.head == None

    def length(self):
        l = 0
        curr = self.head
        while curr:
            l += 1
            curr = curr.next
        return l

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next

    def search(self, item):
        curr = self.head
        found, stop = False, False
        while curr and not found and not stop:
            if curr.val == item:
                found = True
            else:
                if curr.val > item:
                    stop = True
                else:
                    curr = curr.next
        return found

     def delete(self, delElement):
        if not self.head:
            return None
        prev, curr = None, self.head
        if curr and curr.val == delElement: # if the node to be deleted is the head node
            self.head = curr.next
            curr = None
            return
        while curr and curr.val != delElement: # moving through the list
            prev = curr
            curr = curr.next
        if not curr:
            return False
        prev.next = curr.next
        curr = None

    def add(self, element):
        prev, curr, stop = None, self.head, False
        while curr and not stop:
            if curr.val > element:
                stop = True
            else:
                prev = curr
                curr = curr.next
        t = Node(element)
        if not prev:  # if we have to insert in the beginning of the list
            t.next = self.head
            self.head = t
        else:
            prev.next = t
            t.next = curr


if __name__ == '__main__':
    l = LinkedList(4)
    l.add(2)
    l.add(9)
    l.print()
