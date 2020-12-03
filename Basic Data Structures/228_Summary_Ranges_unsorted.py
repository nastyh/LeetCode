def summaryRanges(test):
    res = []
    my_set = set(test)
    for i in test:
        if i in my_set:
            my_set.remove(i)
            left, right = None, None
            min_ = i - 1
            max_ = i + 1

            while min_ in my_set or max_ in my_set:
                if min_ in my_set:
                    my_set.remove(min_)
                    left = min_
                    min_ -= 1
                if max_ in my_set:
                    my_set.remove(max_)
                    right = max_
                    max_ += 1
            left = left if left is not None else i
            right = right if right is not None else i
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left) + "->" + str(right))
    return res