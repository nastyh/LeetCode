class Solution:
    def equalFrequency(self, word: str) -> bool:
        # doesn't work for 'bac'
        d = Counter(word)
        return sum(v for k, v in d.items()) - 1 == len(d)

    def equalFrequency_working(self, word: str) -> bool:  # O(n + k * logk) where k is the max of 26
        """
        It's about calculating the count of counts
        decrementing the largest frequency by 1 allows to equalize the frequencies
        the smallest frequency minus 1 is 0, and all other frequencies are equal
        decrementing the smallest frequency allows to equalize the frequencies
        """
        freq = sorted(list(Counter(word).values()), reverse = True)
        if len(set(freq)) > 2: return False
        # check if decrementing the largest frequency allows to equalize char frequencies
        freq[0] -= 1
        if len(set(freq)) == 1:
            return True
        freq[0] += 1
        # check if decrementing the smallest frequency either gives frequency 0 with all other
    # frequencies equal or allows to equalize char frequencies
        freq[-1] -= 1
        if freq[-1] == 0:
            freq.pop()
        if len(set(freq)) == 1:
            return True
        return False

    def equalFrequency_similar(self, word: str) -> bool:  # O(n + k * logk) where k is the max of 26
        # Sort the frequencies of (unique) letters:
        freq = sorted(Counter(word).values())  # O(n + k*log(k))
        freq[0] -= 1  # remove a letter from the least freq
        if len(set(filter(None, freq))) == 1:  # O(k)
            return True

        freq[0] += 1  # add back for following
        freq[-1] -= 1  # remove a letter from the most freq
        return len(set(filter(None, freq))) == 1  # O(k)