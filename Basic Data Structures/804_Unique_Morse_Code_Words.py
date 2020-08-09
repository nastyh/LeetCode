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


if __name__ == '__main__':
    print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

        