def simplifyPath(path):  # O(n) both 
    stack = []
    path = path.split("/")
    for p in path:
        if p == "." or p == "":
            continue
        elif p == "..":
            if stack:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)


if __name__ == '__main__':
    print(simplifyPath('/home/'))
    print(simplifyPath('/../'))
    print(simplifyPath('/home//foo/'))
    print(simplifyPath('/a/./b/../../c/'))