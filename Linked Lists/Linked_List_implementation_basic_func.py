# Implementation of general Linked List and basic functions

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

    def addItem(self, newitem): # adding to the beginning of the list
        temp = Node(newitem)
        temp.next = self.head
        self.head = temp

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

    def search(self, searchVal):
        curr = self.head
        if not curr:
            return False
        while curr:
            if curr.val == searchVal:
                return True
            else:
                curr = curr.next
        return False

    def elementIx(self, searchval): # returns index of the given element
        curr, ix = self.head, 0
        if not curr:
            return None
        while curr:
            if curr.val == searchVal:
                return ix
            else:
                curr = curr.next
                ix += 1

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


    def delAtPos(self, ix): #deleting a node at position ix. ix starts with 0
        if not self.head:
            return False
        curr = self.head
        if ix == 0:
            self.head = curr.next
            curr = None
            return
        prev, counter = None, 1
        while curr and counter != ix:
            prev = curr
            curr = curr.next
            counter += 1

        if curr is None:
            return False   # went to the end of the list and haven't reached the ix
        prev.next = curr.next # deletion
        curr = None


    def insertAt(self, newvalue, ix): # insert newvalue at the spot ix
        prev, curr, counter = None, self.head, 0
        if curr is None: # if there is nothing, we'll insert in the beginning no matter what ix is passed
            curr = Node(newvalue)
        while curr and counter != ix:
            prev = curr
            curr = curr.next
            counter += 1
        temp = Node(newvalue)
        prev.next = temp
        temp.next = curr







if __name__ == '__main__':
    l = LinkedList(7)
    l.addItem(6)
    l.addItem(3)
    l.print()
