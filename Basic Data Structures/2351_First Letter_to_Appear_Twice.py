class Solution:
    def repeatedCharacter(self, s: str) -> str:  # O(n) and O(1)
        storage = set()  # if the element is in the set, return, otherwise add
        for ch in s:
            if ch in storage:
                return ch
            else:
                storage.add(ch)

    def repeatedCharacter_dict(self, s: str) -> str:  # O(n) and O(n)
        d = dict()
        # build a dict character: how often it has been seen
        for element in s:
            if element not in d.values():
                d[element] = 1
            else:
                d[element] += 1
        for element in s:  # iterate over the string
            if d[element] == 2:  # if this char has been seen twice, return it 
                return element
            else:
                d[element] += 1