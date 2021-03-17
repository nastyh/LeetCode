def largestNumber(nums):
        if set(nums) == set([0]):
            return '0'
        n = map(str, nums)
        for i in range(len(n)):
            for j in range(i, len(n)):
                if n[i] + n[j] < n[j] + n[i]:
                    n[i], n[j] = n[j], n[i]
        return ''.join(n)


def largestNumber1(nums):
    if not any(nums):
        return "0"
    return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1 + n2 > n2 + n1 else (1 if n1 + n2 < n2 + n1 else 0)))

# bubble sort
def largestNumber2(nums):
    def compare(n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
    for i in range(len(nums), 0, -1):
        for j in range(i - 1):
            if not compare(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return str(int("".join(map(str, nums))))


# selection sort
def largestNumber3(nums):
    for i in (len(nums), 0, -1):
        tmp = 0
        for j in (i):
            if not self.compare(nums[j], nums[tmp]):
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return str(int("".join(map(str, nums))))

# insertion sort
def largestNumber4(self, nums):
    for i in range(len(nums)):
        pos, cur = i, nums[i]
        while pos > 0 and not self.compare(nums[pos-1], cur):
            nums[pos] = nums[pos-1]  # move one-step forward
            pos -= 1
        nums[pos] = cur
    return str(int("".join(map(str, nums))))

# merge sort
def largestNumber5(nums):
    nums = mergeSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums))))

def mergeSort(nums, l, r):
    if l > r:
        return
    if l == r:
        return [nums[l]]
    mid = l + (r - l) // 2
    left = self.mergeSort(nums, l, mid)
    right = self.mergeSort(nums, mid + 1, r)
    return self.merge(left, right)

def merge(l1, l2):
    res, i, j = [], 0, 0
    while i < len(l1) and j < len(l2):
        if not compare(l1[i], l2[j]):
            res.append(l2[j])
            j += 1
        else:
            res.append(l1[i])
            i += 1
    res.extend(l1[i:] or l2[j:])
    return res

# quick sort, in-place
def largestNumber(nums):
    def partition(nums, l, r):
        low = l
        while l < r:
            if compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def quickSort(nums, l, r):
        if l >= r:
            return
        pos = partition(nums, l, r)
        quickSort(nums, l, pos - 1)
        quickSort(nums, pos + 1, r)

    quickSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums))))




