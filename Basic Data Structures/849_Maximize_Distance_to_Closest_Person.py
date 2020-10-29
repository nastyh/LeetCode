def maxDistToClosest(seats):
    left, right = 0, len(seats) -1
    left_count = right_count = middle_count = running_count = 0
    
    while left < right:
        if seats[left] == 0:
            left_count += 1
            left += 1
        elif seats[right] == 0:
            right_count  += 1
            right -= 1
        else:
            break
    for i in range (left, right):
        if seats[i] == 0:
            running_count += 1
            middle_count = max(middle_count, running_count)
        else:
            running_count = 0
    return max(left_count, right_count, ((middle_count + 1) // 2))

def maxDistToClosest_another(seats):
    N = len(seats)
    left, right = [N] * N, [N] * N

    for i in range(N):
        if seats[i] == 1: left[i] = 0
        elif i > 0: left[i] = left[i-1] + 1

    for i in range(N-1, -1, -1):
        if seats[i] == 1: right[i] = 0
        elif i < N-1: right[i] = right[i+1] + 1

    return max(min(left[i], right[i])
                for i, seat in enumerate(seats) if not seat)


if __name__ == '__main__':
    print(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    print(maxDistToClosest([1, 0, 0, 0]))
    print(maxDistToClosest_another([1, 0, 0, 0, 1, 0, 1]))