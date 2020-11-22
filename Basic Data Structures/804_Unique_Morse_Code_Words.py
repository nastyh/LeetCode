import string
def uniqueMorseRepresentations(words):
    letters = list(string.ascii_lowercase)
    morze = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d = {i:j for i, j in zip(letters, morze)}
    res, curr = set(), ''
    for word in words:
        for ix in word:
            curr += d[ix]
        res.add(curr)
        curr = ''
    return len(res)  


def uniqueMorseRepresentations_alt(words):  # same idea, slighty different implementation
    letters = [i for i in string.ascii_lowercase]
    symbols = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d = dict(zip(letters, symbols))
    res = []
    for word in words:
        current = ''
        for ch in word:
            current += d[ch]
        res.append(current)
    return len(set(res))


if __name__ == '__main__':
    print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

        