class NestedIterator:
    """
    To flatten the list recursively, notice that we can look at the input as a tree.
    The integers are the leaf nodes, and the order they should be returned is from left to right.
    """
    def __init__(self, nestedList):  # O(N + L) and space O(L + D) where N is the number of integers, L the total number of nested lists, D max nesting depth
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList()) 
        self._integers = []
        self._position = -1 # Pointer to previous returned.
        flatten_list(nestedList)

    def next(self):  # O(1)
        self._position += 1
        return self._integers[self._position]
        
    def hasNext(self):  # O(1)
        return self._position + 1 < len(self._integers)


class NestedIterator_stack:
    """
    While we could use this algorithm in the constructor like before, a better way would be to store stack on the iterator object
    and progress the algorithm on each call to next() to get the next integer out.
    Notice that if the top of the stack is an integer, then we've already found the next integer.
    Otherwise, if it's a list, then the else is adding the list contents to stack. On the next loop iteration, the same will happen.
    """
    def __init__(self, nestedList):  # O(N + L), space O(N + L)
        self.stack = list(reversed(nestedList))
        
    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()
        
    def hasNext(self) -> bool:  # O(L/N) pr O(1)
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
        
    def make_stack_top_an_integer(self):  # O(L/N) or O(1)
        # While the stack contains a nested list at the top...
        while self.stack and not self.stack[-1].isInteger():
            # Unpack the list at the top by putting its items onto
            # the stack in reverse order.
            self.stack.extend(reversed(self.stack.pop().getList()))


class NestedIterator_2_stacks:
    def __init__(self, nestedList: [NestedInteger]):  # O(1). Space O(D)
        self.stack = [[nestedList, 0]]
        
    def make_stack_top_an_integer(self):  # O(L/N) or O(1)
        
        while self.stack:
            
            # Essential for readability :)
            current_list = self.stack[-1][0]
            current_index = self.stack[-1][1]
            
            # If the top list is used up, pop it and its index.
            if len(current_list) == current_index:
                self.stack.pop()
                continue
            
            # Otherwise, if it's already an integer, we don't need 
            # to do anything.
            if current_list[current_index].isInteger():
                break
            
            # Otherwise, it must be a list. We need to increment the index
            # on the previous list, and add the new list.
            new_list = current_list[current_index].getList()
            self.stack[-1][1] += 1 # Increment old.
            self.stack.append([new_list, 0])
            
    def next(self) -> int:
        self.make_stack_top_an_integer()
        current_list = self.stack[-1][0]
        current_index = self.stack[-1][1]
        self.stack[-1][1] += 1
        return current_list[current_index].getInteger()
    
    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0