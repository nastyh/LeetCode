def replace_with_max(l):
# replaces each value in the list with the largest value to the right
    max_right = l[-1] # last element
    for i in range(len(l)-2, -1, -1): # from the second last element to the beginning
        if max_right >= l[i]:
            l[i] = max_right
            
        else:
            max_right = l[i]
    return l



            
