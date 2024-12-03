class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        O(n+m) where n and m are lengths of s and spaces respectively
        O(n+m) incl. the space for the result string or O(1) if only 
        account for the auxiliary space 
        space_ix to keep track where we stand at spaces 
        go over the string
        if we arrive to spot == to the current value from spaces,
        insert a space, increment the counter
        Otherwise, just keep adding chars from s as normal
        """
        res = ''
        space_ix = 0
        for ix, ch in enumerate(s):
            if (space_ix < len(spaces) and ix == spaces[space_ix]):
                res += ' '
                space_ix += 1
            res += ch
        return res


        