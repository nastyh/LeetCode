def removeDuplicates(S):
    st = []
    for el in S:
        if not st:
            st.append(el)
            continue
        if st[-1] == el:
            st.pop()
        else:
            st.append(el)
    return ''.join(b for b in st)


def removeDuplicates_alt(S):
    st = []
    for ch in S:
        # if not st:
        #     st.append(ch)
        #     continue
        if st and st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    return ''.join(st)


if __name__ == '__main__':
    print(removeDuplicates('abbaca'))
    print(removeDuplicates_alt('abbaca'))
