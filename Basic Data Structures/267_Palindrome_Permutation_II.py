from collections import Counter
def generatePalindromes(s):
    if not s:
        return [""]
    # preprocess
    countS = Counter(s)
    odd = False
    chars = ''
    pivot = ''
    for k, v in countS.items():
        if v % 2 == 0:
            chars += k * (v//2)
        elif v == 1 and not odd:
            pivot = k
            odd = True
            continue
        elif v % 2 != 0 and not odd:
            pivot = k
            chars += k*(v // 2)
            odd = True
        elif v % 2 != 0 and odd:
            return []
    def permute(path, visited):
        if len(path) == (len(s)//2):
            if pivot:
                res.append(path[::-1] + pivot + path)
            else:
                res.append(path[::-1] + path)
            return
        else:
            for i in range(len(chars)):
                if visited[i] or (i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                permute(path + chars[i], visited)
                visited[i] = False
    res = []
    visited = [False] * (len(s) // 2)
    permute('', visited)
    return res

if __name__ == '__main__':
    print(generatePalindromes('aabb'))