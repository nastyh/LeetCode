from collections import defaultdict
from random import choice

class RandomizedCollection:
    """
    We will keep a list to store all our elements. In order to make finding the index of elements we want to remove O(1)O(1), we will use a HashMap or dictionary to map values to all indices that have those values. To make this work each value will be mapped to a set of indices. The tricky part is properly updating the HashMap as we modify the list.

    insert: Append the element to the list and add the index to HashMap[element].
    remove: This is the tricky part. We find the index of the element using the HashMap. We use the trick discussed in the intuition
     to remove the element from the list in O(1)O(1). Since the last element in the list gets moved around, we have to update its value in the HashMap. We also have to get rid of the index of the element we removed from the HashMap.
    getRandom: Sample a random element from the list.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.idx = defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.idx[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.lst[-1]
        self.lst[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.lst) - 1)

        self.lst.pop()
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)
