from collections import Counter, deque
import heapq
def rearrangeString(s, k):  # O(N) + O(26log26) b/c of sorting
    counter = Counter(s)
    items = sorted([(freq, ch) for ch,freq in counter.items()])
    maxFreq = items[-1][0]
    slots = ["" for _ in range(maxFreq)]
    slot = 0
    while items:
        freq, ch = items.pop()
        if( freq == maxFreq ):
            for i in range(maxFreq):
                slots[i] = slots[i] + ch
        else:
            while freq :
                slot = slot % (maxFreq - 1)
                slots[slot] = slots[slot] + ch
                freq -= 1
                slot += 1
    for i in range(maxFreq - 1):  # up until last slot
        if len(slots[i]) < k:
            return ""
    return "".join(slots)


def rearrangeString_heap(s, k):
    """
    use a frequency counter to build a "max" heap of most frequent characters
    keep the character just popped/used from being used again until k steps later
    by dropping it in a k sized queue
    """
    if k < 2: return s
    hp, q, ans = [], deque(), []
    for c, count in Counter(s).items():
      heapq.heappush(hp, (-count, c))
    if (k * (-hp[0][0] - 1)) + 1 > len(s): return '' # not possible if too many of max freq. char
    while hp:
      count, c = heapq.heappop(hp)
      ans += c
      q += ((count + 1, c) if (count < -1) else None),
      if len(q) >= k: 
        cand = q.popleft()
        if cand: heapq.heappush(hp, cand)
    return ''.join(ans) if len(ans) == len(s) else ''


if __name__ == '__main__':
    print(rearrangeString('aabbcc', 3))
    print(rearrangeString_heap('aabbcc', 3))
    print(rearrangeString('aaabc', 3))
    print(rearrangeString_heap('aaabc', 3))
    print(rearrangeString('aaadbbcc', 2))
    print(rearrangeString_heap('aaadbbcc', 2))
