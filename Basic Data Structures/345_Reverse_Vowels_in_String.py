class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['e','u','i','o','a', 'E', 'U', 'I', 'O','A']
        l = list(s)
        i, j = 0, len(l) - 1
        while i < j:
            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            if l[i] not in vowels:
                i += 1
            if l[j] not in vowels:
                j -= 1
        return ''.join(q for q in l)

