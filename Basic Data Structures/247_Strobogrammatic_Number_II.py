 def findStrobogrammatic(n):
    def recurse_number(n):
        # base case
        if n == 1:
            return ["0", "1" , "8"]
        if n == 2:
            return ["00", "11", "88","69","96" ]
        
        res = []
        for num in recurse_number(n - 2):
            res.append("0" + num + "0")
            res.append("6" + num + "9")
            res.append("9" + num + "6")
            res.append("8" + num + "8")
            res.append("1" + num + "1")
        return res
    if n == 0:
        return [""]
    elif n == 1:
        return ["0", "1" , "8"]
    else:
        return [number for number in recurse_number(n) if number[0] != "0" and number[-1] != "0"]


def findStrobogrammatic_recur(n):
    evenMidCandidate = ["11","69","88","96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = findStrobogrammatic(n - 1), oddMidCandidate
    else: 
        pre, midCandidate = findStrobogrammatic(n-2), evenMidCandidate
    premid = (n - 1) / 2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]


def findStrobogrammatic_iter(n):
    center = ['0','1','8']                      # center in case of odd length only
    ends = ['11','88','69','96']                # 0 cannot be first character
    middle = ['00','11','88','69','96']         # elsewhere in the string but middle and ends
    # initialize the result list
    if n % 2 == 0:
        curr = ['']                               # empty string is strobogrammatic
    else:
        curr = center                             # only odd length has center character
    # We use a growing technique, appending two characters to both ends of current string
    # We use prev to store results of current iteration which will be used to run the next iteration
    prev = None                                 
    m = n // 2                                    # since we attach 2 characters at a time
    while m > 0:
        prev = curr                             # store results of previous iteration
        curr = []                               # empty curr to append all new strings
        arr = ends if m == 1 else middle          # to avoid attaching a '0' to the front
        for itm in arr:
            for wrd in prev:
                curr.append(itm[0] + wrd + itm[1])
        m -= 1
    return curr
