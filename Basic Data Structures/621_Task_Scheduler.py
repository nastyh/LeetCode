from collections import Counter
def leastInterval(tasks, n):
    char_freq = sorted(Counter(tasks).values() , reverse = True)
    ix, counter, max_freq = 0 , 0 , char_freq[0]
    while ix < len(char_freq) and char_freq[ix] == max_freq:
        counter += 1
        result = (max_freq - 1) * (n + 1) + counter
        ix += 1
    return max(result , len(tasks))

def leastInterval_alt(tasks, n):
    # create list of process occurances
    occurances = list(Counter(tasks).values())

    # base interval calculation = # of groups * size of each group
    intervals = (max(occurances)-1) * (n+1)
    # account for remaining intervals from processes with most occurances
    count_procc_with_max = occurances.count(max(occurances))
    # add these to your total interval count
    intervals += count_procc_with_max

    # return max of calculated intervals and length of initials task list
    return max(intervals, len(tasks))


if __name__ == '__main__':
    print(leastInterval(["A","A","A","B","B","B"], 2))
    print(leastInterval_alt(["A","A","A","B","B","B"], 2))
