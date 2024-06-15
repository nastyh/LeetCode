class OrderedStream:
    """
     we need to store every incoming value at the given index. And
    with every incoming index, we have to check
    If the current index is less than the incoming index, the we have to return
    an empty list
    Else , we have to return an sliced list from the incoming index to the first index
    where there is no insertion till yet.
    """

    def __init__(self, n: int):
        self.ptr = 1
        self.stream = [None] * (n + 2)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            while self.stream[self.ptr]:
                self.ptr += 1
            return self.stream[idKey:self.ptr]
        return []

class OrderedStream:
    """
    Maintain the current index with self.ptr
    
    """
    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        res = []
        
        if idKey == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
        return res