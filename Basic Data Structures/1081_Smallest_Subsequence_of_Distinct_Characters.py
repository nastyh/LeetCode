def smallestSubsequence(s):
        stack = []
        seen = set()
        last_occurrence = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    print(smallestSubsequence('bcabc'))
    print(smallestSubsequence('cbacdcbc'))