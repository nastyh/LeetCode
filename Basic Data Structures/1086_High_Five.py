from collections import defaultdict
import heapq
def highFive(items):  # O(nlogn) and O(n)
    """
    collect in a dictionary: student id: [their scores]
    Then heapify every list with scores, take the top 5, average, build the answer
    """
    res = []
    d = defaultdict(list)
    for item in items:
        d[item[0]].append(item[1])
    for k, v in d.items():
        h = v
        for i in range(len(h)):
            h[i] *= -1
        curr_pair = [k]
        heapq.heapify(h)
        curr_sum = 0
        for _ in range(5):
            curr_sum += -heapq.heappop(h)
        curr_pair.append(curr_sum // 5)
        res.append(curr_pair)
    return sorted(res, key = lambda x: x[0])


def highFive_alt(items):  # O(nlog5) and O(n)
    """
    More precise w/ keeping a heap of size 5 but slower for some reason
    """
    res = []
    d = defaultdict(list)
    for item in items:
        d[item[0]].append(item[1])
    for k, v in d.items():
        curr_pair = [k]
        h = []
        for num in v:
            if len(h) < 5:
                heapq.heappush(h, num)
            else:
                heapq.heappushpop(h, num)
        curr_sum = 0
        for _ in range(5):
            curr_sum += heapq.heappop(h)
        curr_pair.append(curr_sum // 5)
        res.append(curr_pair)
    return sorted(res, key = lambda x: x[0])

        

if __name__ == '__main__':
    print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
    print(highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
    print(highFive([[5, 91],[5, 92],[3, 93],[3, 97],[5, 60],[3, 77],[5, 65],[5, 87],[5, 100],[3, 100],[3, 76]]))
    print(highFive_alt([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
    print(highFive_alt([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
    print(highFive_alt([[5, 91],[5, 92],[3, 93],[3, 97],[5, 60],[3, 77],[5, 65],[5, 87],[5, 100],[3, 100],[3, 76]]))