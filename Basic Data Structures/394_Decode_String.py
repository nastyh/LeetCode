def decodeString_recursive(s):
    i = 0
    def helper():
        nonlocal i
        multi = 0
        sub = []
        while i < len(s):
            char = s[i]
            i += 1
            
            if char.isdigit():
                multi = multi*10 + int(char)
                
            elif char == '[':      
                sub += multi * helper()
                multi = 0
                
            elif char == ']':
                return sub
            
            else:
                sub.append(char)
        
        return "".join(sub)
    
    return helper()


def decodeString_iter(s):
    stack_str = []
    stack_vals = []
    curr_val = 0
    
    for val in s:
        if val.isdigit():
            curr_val = curr_val * 10 + int(val)
        elif val == ']':
            if curr_val != 0:
                stack_vals.append(curr_val)
                curr_val = 0
            curr_str = ''
            num_occurences = stack_vals.pop()
            while len(stack_str):
                elem = stack_str.pop()
                if elem == '[':
                    stack_str.append(curr_str * num_occurences); break
                else:
                    curr_str =  elem + curr_str # Important Step
        else:
            if curr_val != 0:
                stack_vals.append(curr_val)
                curr_val = 0
            stack_str.append(val)

    return ''.join(stack_str)


if __name__ == '__main__':
    print(decodeString_recursive('3[a]2[bc]'))
    print(decodeString_iter('3[a]2[bc]'))
