def removeDuplicates_alt(s, k):  # O(n) both 
    st_char, st_count = [], []
    st_char.append(s[0])
    st_count.append(1)
    for ch in s[1:]:
        if st_char and ch == st_char[-1]:
            st_count[-1] += 1
            if st_count[-1] == k:
                st_count.pop()
                st_char.pop()
        else:
            st_count.append(1)
            st_char.append(ch)
    # return ''.join(i for i in st_char)
    return ''.join(st_char[i] * st_count[i] for i in range(len(st_char)))


def removeDuplicates_alt2(s, k):
    """
    A bit cleaner
    Keep two stacks: for characters and frequencies
    Start with appending the character and one.
    Then make decisions.
    If the coming character isn't the same as the latest, append it and 1
    If it's the same,
    if the counter is still < k, just update the counter
    If the counter == k, time to pop up from both stacks.
    Important to properly build the answer b/c if we just return st, we miss edge cases when the answer should be 'aa' (in this case st = ['a'])
    """
    st, st_count = [], []
    for ch in s:
        if len(st) == 0:
            st.append(ch)
            st_count.append(1)
        else:
            if st[-1] != ch:
                st.append(ch)
                st_count.append(1)
            else:
                if st_count[-1] < k:
                    st_count[-1] += 1
                    if st_count[-1] == k:
                        st.pop()
                        st_count.pop()
    # print(st, st_count)
    return ''.join(st[i] * st_count[i] for i in range(len(st)))
        
   


if __name__ == '__main__':
    # print(removeDuplicates_alt('deeedbbcccbdaa', 3))
    # print(removeDuplicates_alt('abcd', 2))
    # print(removeDuplicates_alt('pbbcggttciiippooaais', 2))
    # print(removeDuplicates_alt('yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy', 4))
    print(removeDuplicates_alt2('deeedbbcccbdaa', 3))