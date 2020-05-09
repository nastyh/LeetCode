class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        result = 0

        for word in words:
            counter = 0
            copy = chars

            for char in word:
                if char not in copy:
                    break
                else:
                    copy = copy.replace(char, '', 1)
                    counter += 1

            if len(word) == counter:
                result += counter

        return result
