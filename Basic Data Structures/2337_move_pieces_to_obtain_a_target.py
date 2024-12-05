class Solution:
    def canChange_deque(self, start: str, target: str) -> bool:
        """
        O(n) and O(1)
        The relative order of 'L's and 'R's must remain unchanged since they cannot pass through each other.
        An 'L' in the start string must be at the same position or to the right of its target position.
        An 'R' in the start string must be at the same position or to the left of its target position.
        extract the positions of all 'L' and 'R' pieces from both strings and compare them in order.
        creating two queues to store character-position pairs. Next, populate these queues by iterating through
        both the start and target strings, recording only the non-underscore characters along with their positions.
        Once the queues are populated, compare their sizes to ensure they match, as this confirms that both strings
        contain the same number of pieces. Then, process both queues simultaneously, comparing each pair of front characters
        to verify that they are of the same type (both 'L' or both 'R') and that their positions allow for valid moves according
        to the rules. Specifically, for 'L' pieces, ensure that the start position is not to the left of the target position, and for
        'R' pieces, ensure that the start position is not to the right of the target position.
        """
        start_d, target_d = [], []
        for i in range(len(start)):
            if start[i] != '_':
                start_d.append((start[i], i))
            if target[i] != '_':
                target_d.append((target[i], i))
        # edge case
        if len(start_d) != len(target_d):
            return False 
        # compare each type and position
        while not len(start_d) == 0:
            start_char, start_index = start_d.pop(0)
            target_char, target_index = target_d.pop(0)

            # Check character match and movement rules
            if (
                start_char != target_char
                or (start_char == "L" and start_index < target_index)
                or (start_char == "R" and start_index > target_index)
            ):
                return False
        return True
    
    def canChange_two_pointers(self, start: str, target: str) -> bool:
        """
        O(n) and O(1)
        relative positions of the 'L' and 'R' pieces and whether they can move
        to their target positions according to the movement rules. Each time we find an 'L' or 'R'
        in both strings (after skipping underscores), we can immediately check if the movement is
        possible based on their positions:
        pieces can only move left, so their position in the start string must be greater
        than or equal to their position in the target string.
        'R' pieces can only move right, so their position in the start string must be less
        than or equal to their position in the target string.
        Character Matching: Ensure that the sequence of 'L' and 'R' pieces is identical in both strings.
        Position Constraints: Check that 'L' pieces don't need to move right and 'R' pieces don't need to move left.
        """
        start_l = len(start)
        start_ix, target_ix = 0, 0
        while start_ix < start_l or target_ix < start_l:
            while start_ix < start_l and start[start_ix] == '_':
                start_ix += 1
            while target_ix < start_l and target[target_ix] == '_':
                target_ix += 1
            if start_ix == start_l or target_ix == start_l: 
                return (start_ix == start_l and target_ix == start_l)
            # check if the pieces match and follow movement rules
            if (
                start[start_ix] != target[target_ix]
                or (start[start_ix] == "L" and start_ix < target_ix)
                or (start[start_ix] == "R" and start_ix > target_ix)
            ):
                return False

            start_ix += 1
            target_ix += 1
        return True

    def canChange_pythonic(self, start: str, target: str) -> bool:
        """
        O(n) and O(1) 
        using Python generators 
        """
        def _helper(s):
            for i, ch in enumerate(s):
                if ch != '_':
                    yield i 
        for a, b in zip_longest(_helper(start), _helper(target)):
            if a is None or b is None or start[a] != target[b]:
                return False 
            if a < b and start[a] == 'L':
                return False 
            if a > b and start[a] == 'R':
                return False 
        return True 