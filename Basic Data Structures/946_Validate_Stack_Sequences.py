def validateStackSequences(pushed, popped):  # O(n) both
    """
    Add an i-th element of pushed to the stack
    The element at this index in popped should be the same. 
    Move till the end
    """
    st = []
    i = 0 
    for num in pushed:
        st.append(num)
        while st and i < len(pushed) and st[-1] == popped[i]:
            st.pop()
            i += 1
    return len(st) == 0