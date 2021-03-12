def hasAllCodes(s, k):  # O(NK) both where N is the length of s and O(K) is to calcuate the hash of each substring
    need = 1 << k
    got = set()
    for i in range(k, len(s) + 1):
        tmp = s[i - k : i]
        if tmp not in got:
            got.add(tmp)
            need -= 1
            # return True when found all occurrences
            if need == 0:
                return True
    return False

def hasAllCodes_another(s, k):  # O(N) to iterate, O(2^K) as there are 2^k elements in the list
    need = 1 << k
    got = [False]*need
    all_one = need - 1
    hash_val = 0

    for i in range(len(s)):
        # calculate hash for s[i-k+1:i+1]
        hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
        # hash only available when i-k+1 > 0
        if i >= k-1 and got[hash_val] is False:
            got[hash_val] = True
            need -= 1
            if need == 0:
                return True
    return False


if __name__ == '__main__':  
    print(hasAllCodes('00110110', 2))