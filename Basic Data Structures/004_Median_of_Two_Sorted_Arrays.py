def findMedianSortedArrays(nums1, nums2):
    # Get the lengths of both lists
    l1,l2 = len(nums1), len(nums2)
    # Determine the middle
    middle = (l1 + l2) / 2
    
    # EDGE CASE:
    # If we only have 1 value (e.g. [1], []), return nums1[0] if the length of
    # that list is greater than the length of l2, otherwise return nums2[1]
    if middle == 0.5: return float(nums1[0]) if l1 > l2 else float(nums2[0])

    # Initialize 2 pointers
    x =  y = 0
    # Initialize 2 values to store the previous and current value (in case of an even
    # amount of values, we need to average 2 values)
    cur = prev = 0
    # Determine the amount of loops we need. If the middle is even, loop that amount + 1:
    # eg: [1, 2, 3, 4, 5, 6]        6 values, middle = 3, loops = 3+1
    #            ^  ^ 
    #            |  +-- cur
    #            +----- prev
    # If the middle is odd, loop that amount + 0.5
    # eg: [1, 2, 3, 4, 5]           5 values, middle = 2.5, loops = 2.5+0.5
    #            ^
    #            +--- cur
    loops = middle + 1 if middle % 1 == 0 else middle + 0.5

    # Walk forward the amount of loops
    for _ in range(int(loops)):
        # Store the value of cur in prev
        prev = cur
        # If the x pointer is equal to the amount of elements of nums1 (l1 == len(nums1))
        if x == l1:
            # Store nums2[y] in cur, 'cause we hit the end of nums1
            cur =  nums2[y]
            # Move the y pointer one ahead
            y += 1
        # If the y pointer is equal to the amount of elements of nums2 (l2 == len(nums2))
        elif y == l2:
            # Store nums1[x] in cur, 'cause we hit the end of nums2
            cur =  nums1[x]
            # Move the x pointer one ahead
            x += 1
        # If the value in nums1 is bigger than the value in nums2
        elif nums1[x] > nums2[y]:
            # Store nums2[y] in cur, because it's the lowest value
            cur =  nums2[y]
            # Move the y pointer one ahead
            y += 1
        # If the value in nums2 is bigger than the value in nums1
        else:
            # Store nums1[x] in, because it's the lowest value
            cur =  nums1[x]
            # Move the x pointer one ahead
            x += 1
    # If middle is even
    if middle % 1 == 0.0:
        # Return the average of the cur + prev values (which will return a float)
        return (cur+prev)/2
    # If middle is odd
    else:
        # Return the cur value, as a float
        return float(cur)


def findMedianSortedArrays_alt(nums1, nums2):
    overall=[]
    m = len(nums1)
    n = len(nums2)
    tot = m + n
    answer_ind = []
    if(tot % 2 == 0):
        answer_ind = [(tot // 2) - 1, (tot // 2)]
    else:
        answer_ind = [(tot // 2)]
        
    pnt1 = 0
    pnt2 = 0
    while(pnt1 < m or pnt2 < n):
        if(pnt1 < m and pnt2 < n):
            if(nums1[pnt1] <= nums2[pnt2]):
                overall.append(nums1[pnt1])
                pnt1 += 1
            else:
                overall.append(nums2[pnt2])
                pnt2 += 1
        elif(pnt1 < m):
            overall.append(nums1[pnt1])
            pnt1 += 1
        elif(pnt2 < n):
            overall.append(nums2[pnt2])
            pnt2 += 1
        
        if(len(overall)-1 == answer_ind[-1]):
            sm = 0
            for k in answer_ind:
                sm += overall[k]
            
            return sm / float(len(answer_ind))
        return -1


def findMedianSortedArrays_brute_force(nums1, nums2):  # O((m+n) * log(m+n)) both 
    both = sorted(nums1 + nums2)
    l = len(both)
    if l % 2 == 1:
        return both[l // 2]
    else:
        m_ix = l // 2
        return (both[m_ix - 1] + both[m_ix]) / 2