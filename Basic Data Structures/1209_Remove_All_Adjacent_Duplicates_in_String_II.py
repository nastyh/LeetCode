def removeDuplicates_alt(s, k):
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


if __name__ == '__main__':
    print(removeDuplicates_alt('deeedbbcccbdaa', 3))
    print(removeDuplicates_alt('abcd', 2))
    print(removeDuplicates_alt('pbbcggttciiippooaais', 2))
    print(removeDuplicates_alt('yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy', 4))
    print(removeDuplicates_alt2('deeedbbcccbdaa', 3))