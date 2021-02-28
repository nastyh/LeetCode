from random import choice
class RandomizedSet():
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.
        Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.
        To delete a value at arbitrary index takes linear time. The solution here is to always delete the last value:

        Swap the element to delete with the last one.

        Pop the last element out.
        For that, one has to compute an index of each element in constant time, and hence needs a hashmap which stores element -> its index dictionary.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)



class RandomizedSet_another:
    ## RC ##
    ## APPROACH : HASHMAP ##
    #   1. Insertion operation in list is O(1) but not deletion
    #   2. So we create one Hashmap with key,index and other list
    #   3. for deleting we go to hashmap, get index, go to that index in list, swap that element with last element.
    #   4. save the index to last element in hashmap and delete list last element

    def __init__(self):
        self.lists = []
        self.hmap = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if(val in self.hmap):
            return False
        self.hmap[val] = self.length
        self.length += 1
        self.lists.append(val)
        return True

    def remove(self, val: int) -> bool:
        if(val not in self.hmap):
            return False
        index = self.hmap[val]
        self.hmap[self.lists[-1]] = index
        self.lists[index], self.lists[-1] = self.lists[-1], self.lists[index]
        self.lists.pop()
        self.hmap.pop(val)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        ri = random.randint(0, self.length - 1)
        return self.lists[ri]