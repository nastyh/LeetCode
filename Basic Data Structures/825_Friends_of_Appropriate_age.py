from collections import Counter
def numFriendRequests_bin_search(ages):  # O(nlogn) and O(n)
    """
    Sort by age
    index i person will not send friend request to ages[i]+1, ages[i]+2 etc
    index i person will not send friend request to elements whose age is less than (0.5 * ages[i] + 7)
    Using binary search we can find upper and lower limit, persons which fall in this range, can send friend requests (remove 1, ith person itself)
    """
    ages.sort()
    count = 0
    for i in range(len(ages)):
        left = bisect.bisect_right( ages, (0.5 * ages[i]) + 7 )
        right = bisect.bisect_right( ages, ages[i])
        count += max(0, right - left - 1)                       # you cannot have negative count
    return count


def numFriendRequests_counter(ages):  # O(n^2) and O(n)
    d = Counter(ages)
    ans = 0
    for ageA, countA in d.items():
        for ageB, countB in d.items():
            if ageA * 0.5 + 7 >= ageB: continue
            if ageA < ageB: continue
            ans += countA * countB
            if ageA == ageB: ans -= countA
    return ans


def numFriendRequests_sliding(ages):  # O(nlogn) b/c of sorting and O(n)
    ages = sorted(Counter(ages).items(), key = lambda x: x[0])
    def calc(arr):
        total = 0
        window = 0
        left = 0
        for right, (age, count) in enumerate(arr):
            while left < right and arr[left][0] <= 0.5 * age + 7:
                window -= arr[left][1]
                left += 1
            total += window * count
            if count > 1 and age > 0.5 * age + 7:
                total += (count - 1) * count
            window += count
        return total
    return calc(ages)


if __name__ == '__main__':
    print(numFriendRequests_counter([16, 16]))
    print(numFriendRequests_counter([16, 17, 18]))
    print(numFriendRequests_counter([20, 30, 100, 110, 120]))
    print(numFriendRequests_sliding([16, 16]))
    print(numFriendRequests_sliding([16, 17, 18]))
    print(numFriendRequests_sliding([20, 30, 100, 110, 120]))


