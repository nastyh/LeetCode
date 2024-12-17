class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
        O(nlogk), n = len(s), k is the number of unique characters
        O(k) to maintain the heap
        in the heap we put pairs in the shape of (ord(character), its count in string s)
        z has a higher ord, so we can build a max heap by negating this value
        then we start taking letter by letter 
        we append it the min(repeatLimit, how many of this letter we have)
        update the counts
        if we aren't finished, pop the next candidate, do the whole thing again,
        update the counts 
        if after all of this, some characters are still left, readd to the heap
        return the res at the end 
        """
        res = []
        d = Counter(s)
        max_h = [(-ord(c), cnt) for c, cnt in d.items()]
        heapq.heapify(max_h)

        while max_h:
            char_number, char_count = heapq.heappop(max_h)
            actual_char = chr(-char_number)
            res.extend([actual_char] * min(char_count, repeatLimit))

            if char_count > min(char_count, repeatLimit) and max_h:
                next_char_number, next_char_count = heapq.heappop(max_h)
                res.extend(chr(-next_char_number))
                if next_char_count > 1:
                    heapq.heappush(max_h, (next_char_number, next_char_count - 1))
                heapq.heappush(max_h, (char_number, char_count - min(char_count, repeatLimit)))
        return ''.join(res)